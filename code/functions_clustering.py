import os

import pandas as pd 
import numpy as np

from math import pi
from scipy import stats, spatial, optimize

import matplotlib.pyplot as plt

from itertools import combinations

from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples, davies_bouldin_score, adjusted_rand_score

from IPython.display import display

keys = ["player_id", "team_id", "position_group"]

suffix_labels = {'': 'raw', '_adj': 'adj', '_subcluster_adj': 'subcluster_adj'}

def safe_name(division):
    return division.replace(' ', '_')  # matches what you originally saved with

def time_to_minutes(t):
    if pd.isna(t):
        return np.nan
    mm, ss = t.split(':')
    return int(mm) + int(ss) / 60

def build_match_time_anchors(events_dfs):
    events_all = pd.concat(
        [df[['match_id', 'period', 'minute', 'second', 'type']] for df in events_dfs],
        ignore_index=True
    )
    events_all['clock_min'] = events_all['minute'] + events_all['second'] / 60

    half_end = events_all[events_all['type'] == 'Half End']

    period1_end = (half_end[half_end['period'] == 1]
                   .groupby('match_id')['clock_min'].first())
    period2_offset = period1_end - 45

    match_end_raw = (half_end[half_end['period'] == 2]
                     .groupby('match_id')['clock_min'].first())
    match_end = match_end_raw + match_end_raw.index.map(period2_offset).fillna(0)
    match_end = match_end.dropna()

    return period1_end, match_end, match_end_raw, period2_offset

def add_elapsed_time(df, period2_offset_map):
    df = df.copy()
    raw_time = df['minute'] + df['second'] / 60
    offset = df['match_id'].map(period2_offset_map).fillna(0)
    df['elapsed_min'] = np.where(df['period'] == 2, raw_time + offset, raw_time)
    return df

# --------------------------------------------------------------------------- #
# 1. Timeline + stints (your code, with the NEW lines)
# --------------------------------------------------------------------------- #
def build_formation_timeline(match_id, team_id, events_df, all_position_slots):
    team_events = events_df[
        (events_df["match_id"] == match_id) & (events_df["team_id"] == team_id)
    ].sort_values("index")
 
    timeline_rows = []
    current_state = {slot: None for slot in all_position_slots}
    current_formation = None                                                    # NEW
 
    for _, row in team_events.iterrows():
        if row["type"] in ["Starting XI", "Tactical Shift"]:
            lineup = row["tactics"]["lineup"]
            current_formation = row["tactics"]["formation"]                     # NEW
            current_state = {slot: None for slot in all_position_slots}
            sent_off_ids = team_events[
                (team_events["type"] == "Red Card") & (team_events["elapsed_min"] <= row["elapsed_min"])
            ]["player_id"].tolist()
 
            for entry in lineup:
                if entry["player"]["id"] not in sent_off_ids:
                    current_state[entry["position"]["name"]] = entry["player"]["id"]
 
        elif row["type"] == "Substitution":
            outgoing_id = row["player_id"]
            incoming_id = row["substitution_replacement_id"]
            for slot, occupant in current_state.items():
                if occupant == outgoing_id:
                    current_state[slot] = incoming_id
                    break
 
        elif row["type"] in ["Player Off", "Red Card"]:  # both remove a player from the pitch
            for slot, occupant in current_state.items():
                if occupant == row["player_id"]:
                    current_state[slot] = None
                    break
 
        elif row["type"] == "Player On":
            current_state[row["position"]] = row["player_id"]
 
        snapshot = current_state.copy()
        snapshot["timestamp"] = row["elapsed_min"]
        snapshot["event_type"] = row["type"]
        snapshot["formation"] = current_formation                               # NEW
        timeline_rows.append(snapshot)
 
    return pd.DataFrame(timeline_rows)

def build_final_stints(formation_timeline, all_position_slots, match_end):
    """Your stint code, wrapped. Returns (final_stints, formation_timeline_with_checkpoints)."""
    ft = formation_timeline.sort_values(["match_id", "team_id", "timestamp"]).reset_index(drop=True)
    ft["checkpoint_id"] = ft.groupby(["match_id", "team_id"]).cumcount() + 1
    ft["end_time"] = ft.groupby(["match_id", "team_id"])["timestamp"].shift(-1)
    ft["end_time"] = ft["end_time"].fillna(ft["match_id"].map(match_end))
    # NEW: groupby silently drops NaN keys, so check formation here, before melt/groupby
    assert ft["formation"].notna().all(), "checkpoints without a formation (team-match with no Starting XI?)"
    ft["formation"] = ft["formation"].astype(int)
 
    formation_long = ft.melt(
        id_vars=["match_id", "team_id", "checkpoint_id", "timestamp", "end_time", "event_type",
                 "formation"],                                                  # NEW: formation
        value_vars=all_position_slots,
        var_name="position_name", value_name="player_id",
    ).dropna(subset=["player_id"])
    formation_long = formation_long.sort_values(["match_id", "team_id", "player_id", "checkpoint_id"])
    grp = ["match_id", "team_id", "player_id"]
    formation_long["prev_position"] = formation_long.groupby(grp)["position_name"].shift(1)
    formation_long["prev_checkpoint"] = formation_long.groupby(grp)["checkpoint_id"].shift(1)
    formation_long["prev_formation"] = formation_long.groupby(grp)["formation"].shift(1)   # NEW
    formation_long["new_stint"] = (
        formation_long["prev_checkpoint"].isna()
        | (formation_long["position_name"] != formation_long["prev_position"])
        | (formation_long["checkpoint_id"] != formation_long["prev_checkpoint"] + 1)
        | (formation_long["formation"] != formation_long["prev_formation"])                # NEW
    )
    formation_long["stint_id"] = formation_long.groupby(grp)["new_stint"].cumsum()
 
    final_stints = (formation_long
                    .groupby(["match_id", "team_id", "player_id", "position_name", "formation", "stint_id"])  # NEW: formation
                    .agg(from_min=("timestamp", "min"), to_min=("end_time", "max"))
                    .reset_index())
    final_stints["duration"] = final_stints["to_min"] - final_stints["from_min"]
 
    return final_stints, ft

# --------------------------------------------------------------------------- #
# 2. Team formation usage (clock time, counted once per team-match)
# --------------------------------------------------------------------------- #
def team_formation_minutes(formation_timeline: pd.DataFrame, regular_share: float = 0.10) -> pd.DataFrame:
    """Team clock-minutes per formation. Needs the timeline returned by build_final_stints
    (checkpoint durations = end_time - timestamp, so a formation is counted once per team-match,
    not once per player). `regular_share` flags formations used for >= that share of team minutes."""
    ft = formation_timeline.copy()
    ft["minutes"] = ft["end_time"] - ft["timestamp"]
    out = ft.groupby(["team_id", "formation"], as_index=False).agg(
        minutes=("minutes", "sum"), n_matches=("match_id", "nunique"))
    out["share"] = out["minutes"] / out.groupby("team_id")["minutes"].transform("sum")
    out["is_regular"] = out["share"] >= regular_share
    return out.sort_values(["team_id", "minutes"], ascending=[True, False]).reset_index(drop=True)
 
 
# --------------------------------------------------------------------------- #
# 3. Player slot profiles (overall and per formation)
# --------------------------------------------------------------------------- #
def player_slot_profile(final_stints: pd.DataFrame, league_map=None):
    """Overall slot split within each (player, team, position_group).
    Returns (long, wide). Shares sum to 1 per (player, team, position_group)."""
    fs = final_stints[final_stints["duration"] > 0]
    slot = (fs.groupby(keys + ["position_name"])["duration"].sum()
              .reset_index(name="minutes_at_slot"))
    slot["minutes_at_position"] = slot.groupby(keys)["minutes_at_slot"].transform("sum")
    slot["slot_share"] = slot["minutes_at_slot"] / slot["minutes_at_position"]
 
    wide = slot.pivot_table(index=keys, columns="position_name", values="slot_share", fill_value=0.0)
    wide.columns = [f"slot_share_{c}" for c in wide.columns]
    assert np.allclose(wide.sum(axis=1), 1.0)
 
    top = (slot.sort_values("minutes_at_slot", ascending=False, kind="mergesort")
               .drop_duplicates(keys).set_index(keys)[["position_name", "slot_share"]]
               .rename(columns={"position_name": "dominant_slot", "slot_share": "dominant_slot_share"}))
    base = slot.groupby(keys).agg(minutes_at_position=("minutes_at_slot", "sum"),
                                  n_slots=("position_name", "nunique"))
    out = base.join(top).join(wide).reset_index()
    if league_map is not None:
        out["league"] = out["team_id"].map(league_map)
    return slot, out
 
 
def player_slot_by_formation(final_stints: pd.DataFrame, min_formation_minutes: float = 180.0):
    """Long table, one row per (player, team, position_group, formation, position_name).
      slot_share_in_formation = minutes at this slot / her position-group minutes in this formation
      formation_share         = her position-group minutes in this formation / all her group minutes
    `reliable` flags cells with enough minutes in the formation to read the slot split."""
    fs = final_stints[final_stints["duration"] > 0]
    kf = keys + ["formation"]
    g = (fs.groupby(kf + ["position_name"])["duration"].sum().reset_index(name="minutes_at_slot"))
    g["minutes_in_formation"] = g.groupby(kf)["minutes_at_slot"].transform("sum")
    g["slot_share_in_formation"] = g["minutes_at_slot"] / g["minutes_in_formation"]
    g["minutes_at_position"] = g.groupby(keys)["minutes_at_slot"].transform("sum")
    g["formation_share"] = g["minutes_in_formation"] / g["minutes_at_position"]
    g["reliable"] = g["minutes_in_formation"] >= min_formation_minutes
    return g
 
 
def team_slot_occupancy(final_stints: pd.DataFrame) -> pd.DataFrame:
    """Team-centric view: for each team x formation x slot, who played there.
    share_of_slot = player's minutes / all minutes at that slot in that formation."""
    fs = final_stints[final_stints["duration"] > 0]
    k = ["team_id", "formation", "position_group", "position_name"]
    occ = fs.groupby(k + ["player_id"])["duration"].sum().reset_index(name="minutes")
    occ["slot_minutes"] = occ.groupby(k)["minutes"].transform("sum")
    occ["share_of_slot"] = occ["minutes"] / occ["slot_minutes"]
    occ["rank_in_slot"] = occ.groupby(k)["minutes"].rank(method="first", ascending=False).astype(int)
    return occ.sort_values(k + ["rank_in_slot"]).reset_index(drop=True)
 
 
# --------------------------------------------------------------------------- #
# 4. Join to clustering results
# --------------------------------------------------------------------------- #
def attach_cluster_info(table: pd.DataFrame, cluster_df: pd.DataFrame, cluster_cols: list[str],
                        validate: str) -> pd.DataFrame:
    """Left-join cluster label + similarity columns on (player_id, team_id, position_group).
    validate='1:1' for the overall profile, 'm:1' for per-formation / occupancy tables.
    Players without a cluster (below minutes threshold, other position group) keep NaN."""
    cl = cluster_df
    if set(keys).issubset(set(cl.index.names)):
        cl = cl.reset_index()
    cl = cl[keys + list(cluster_cols)]
    assert not cl.duplicated(keys).any(), "cluster table must be unique on keys"
    out = table.merge(cl, on=keys, how="left", validate=validate)
    out["has_cluster"] = out[cluster_cols[0]].notna()
    return out
 
 
def cluster_slot_mix(profile_wide: pd.DataFrame, cluster_col: str, position_group: str) -> pd.DataFrame:
    """Minutes-weighted mean slot shares per cluster: which roles each archetype occupies."""
    p = profile_wide[(profile_wide["position_group"] == position_group) & profile_wide[cluster_col].notna()]
    cols = [c for c in p.columns if c.startswith("slot_share_")]
    cols = [c for c in cols if p[c].abs().sum() > 0]
    w = p["minutes_at_position"]
    num = p[cols].mul(w, axis=0).groupby(p[cluster_col]).sum()
    return num.div(w.groupby(p[cluster_col]).sum(), axis=0)

def has_overlap(group):
    group = group.sort_values(['from_min', 'to_min']).reset_index(drop=True)
    for i in range(len(group) - 1):
        if group.loc[i, 'to_min'] > group.loc[i+1, 'from_min']:
            return True
    return False

def build_eligible_pool(position_group, minutes_by_position):
    return minutes_by_position[
        (minutes_by_position['position_group'] == position_group) &
        (minutes_by_position['position_eligible'])
    ].copy()

x_scale = 105 / 120
y_scale = 68 / 80
goal_x, goal_y = 120, 40

def in_own_box(x, y):
    return (x <= 18) & (y >= 18) & (y <= 62)

def in_opposition_box(x, y):
    return (x >= 102) & (y >= 18) & (y <= 62)

def distance_to_goal_meter(x, y):
    dx = (goal_x - x) * x_scale
    dy = (goal_y - y) * y_scale
    return np.sqrt(dx**2 + dy**2)

def distance_meter(x1, y1, x2, y2):
    dx = (x1 - x2) * x_scale
    dy = (y1 - y2) * y_scale
    return np.sqrt(dx**2 + dy**2)

post_y_top, post_y_bottom = 36, 44

def compute_shot_angle(x, y):
    x_m = 120 - x 
    y_top_m = post_y_top - y 
    y_bottom_m = post_y_bottom - y 
    angle = np.abs(np.arctan2(y_top_m, x_m) - np.arctan2(y_bottom_m, x_m))
    return angle  # in radians; convert to degrees with np.degrees() if preferred

def in_opposing_half(x):
    return x >= 60

def simplify_body_part(bp, position_group):
    if bp in ['Right Foot', 'Left Foot']:
        return bp
    elif bp == 'Head':
        return 'Head'
    elif position_group == 'Goalkeeper' and bp in ['Keeper Arm', 'Drop Kick']:
        return bp
    else:
        return 'Other/Unknown'

def build_subtype_completion_rate(events_df, stat_name, group_keys=['player_id', 'team_id', 'position_group']):
    return (events_df[events_df[stat_name]]
        .groupby(group_keys)
        .agg(**{f'{stat_name}_completion_pct': ('pass_completed', 'mean')})
        .reset_index())

def build_category_completion_rate(events_df, cat_col, cat_value, stat_name, group_keys=['player_id', 'team_id', 'position_group']):
    subset = events_df[events_df[cat_col] == cat_value]
    return (subset
        .groupby(group_keys)
        .agg(**{f'{stat_name}_completion_pct': ('pass_completed', 'mean')})
        .reset_index())

def windowed_possession_frac(match_id, team_id, from_min, to_min, poss_seq):
    match_chains = poss_seq[poss_seq['match_id'] == match_id]

    overlapping = match_chains[
        (match_chains['start_time'] < to_min) & (match_chains['chain_end'] > from_min)
    ].copy()

    if len(overlapping) == 0:
        return np.nan

    overlapping['overlap_start'] = overlapping['start_time'].clip(lower=from_min)
    overlapping['overlap_end'] = overlapping['chain_end'].clip(upper=to_min)
    overlapping['overlap_duration'] = overlapping['overlap_end'] - overlapping['overlap_start']

    total = overlapping['overlap_duration'].sum()
    if total <= 0:
        return np.nan

    team_total = overlapping.loc[overlapping['possession_team_id'] == team_id, 'overlap_duration'].sum()
    return team_total / total

def get_possession_frac_final(row, poss_seq, team_duration):
    # try the windowed calculation first (correct for both partial and full appearances)
    windowed = windowed_possession_frac(row['match_id'], row['team_id'], row['from_min'], row['to_min'], poss_seq)
    if pd.notna(windowed):
        return windowed

    # fallback: whole-match possession for this team
    match = team_duration[(team_duration['match_id'] == row['match_id']) & (team_duration['possession_team_id'] == row['team_id'])]
    if len(match):
        return match['possession_frac'].iloc[0]

    # final fallback: no data available at all for this match/team — assume neutral 0.5
    return 0.5

def assign_stint(row, stints_df):
    candidates = stints_df[
        (stints_df['player_id'] == row['player_id']) &
        (stints_df['match_id'] == row['match_id']) &
        (stints_df['from_min'] <= row['elapsed_min']) &
        (row['elapsed_min'] < stints_df['to_min'])
    ]
    return candidates.index[0] if len(candidates) else np.nan

def build_padj_feature(events_subset, stat_name, final_stints, minutes_by_position):
    # mark each player's final stint (the one with no successor) so we can treat its end as inclusive
    final_stints = final_stints.copy()
    last_stint_end = final_stints.groupby(
        ['player_id', 'match_id', 'team_id', 'league', 'position_group']
    )['to_min'].transform('max')
    final_stints['is_last_stint'] = final_stints['to_min'] == last_stint_end

    events_with_stint = events_subset.merge(
        final_stints[['player_id', 'match_id', 'team_id', 'league', 'position_group',
                      'from_min', 'to_min', 'is_last_stint', 'padj_factor']],
        on=['player_id', 'match_id', 'team_id', 'league', 'position_group'],
        how='left'
    )

    within_window = (
        (events_with_stint['elapsed_min'] >= events_with_stint['from_min']) &
        (
            (events_with_stint['elapsed_min'] < events_with_stint['to_min']) |
            (events_with_stint['is_last_stint'] & (events_with_stint['elapsed_min'] <= events_with_stint['to_min']))
        )
    )
    events_with_stint = events_with_stint[within_window]

    # --- validation: every original event should be matched to exactly one stint ---
    match_counts = events_with_stint.groupby(events_with_stint.index).size()
    n_matched = events_with_stint.index.nunique()
    n_original = len(events_subset)
    n_duplicated = (match_counts > 1).sum()
    print(f"{stat_name}: {n_original} raw events, {n_matched} matched to exactly one stint, "
          f"{n_original - n_matched} unmatched, {n_duplicated} matched to more than one stint")

    events_with_stint[f'{stat_name}_padj'] = events_with_stint['padj_factor']

    season = (events_with_stint.groupby(['player_id', 'team_id', 'league', 'position_group'])
              .agg(**{
                  f'{stat_name}_total': (f'{stat_name}_padj', 'size'),
                  f'{stat_name}_total_padj': (f'{stat_name}_padj', 'sum'),
              }).reset_index())

    season = season.merge(
        minutes_by_position[['player_id', 'team_id', 'league', 'position_group', 'minutes_at_position']],
        on=['player_id', 'team_id', 'league', 'position_group'],
        how='left'
    )
    season[f'{stat_name}_per_90'] = season[f'{stat_name}_total'] / season['minutes_at_position'] * 90
    season[f'{stat_name}_padj_per_90'] = season[f'{stat_name}_total_padj'] / season['minutes_at_position'] * 90

    return season

def find_unmatched_events(events_subset, final_stints):
    events_subset = events_subset.copy()
    events_subset['_original_idx'] = events_subset.index  # explicitly carry the original index as a real column

    events_with_stint = events_subset.merge(
        final_stints[['player_id', 'match_id', 'team_id', 'league', 'position_group',
                      'from_min', 'to_min', 'padj_factor']],
        on=['player_id', 'match_id', 'team_id', 'league', 'position_group'],
        how='left'
    )

    events_with_stint['is_last_stint'] = events_with_stint.groupby(
        ['player_id', 'match_id', 'team_id', 'league', 'position_group']
    )['to_min'].transform('max') == events_with_stint['to_min']

    within_window = (
        (events_with_stint['elapsed_min'] >= events_with_stint['from_min']) &
        (
            (events_with_stint['elapsed_min'] < events_with_stint['to_min']) |
            (events_with_stint['is_last_stint'] & (events_with_stint['elapsed_min'] <= events_with_stint['to_min']))
        )
    )

    matched_original_indices = set(events_with_stint.loc[within_window, '_original_idx'])
    unmatched = events_subset[~events_subset['_original_idx'].isin(matched_original_indices)]
    return unmatched.drop(columns='_original_idx')

def compare_raw_counts(new_feature_df, new_count_col, original_feature_df, original_count_col, stat_name):
    comparison = new_feature_df[['player_id', 'team_id', 'position_group', new_count_col]].merge(
        original_feature_df[['player_id', 'team_id', 'position_group', original_count_col]],
        on=['player_id', 'team_id', 'position_group'], how='outer', indicator=True
    )
    comparison['diff'] = comparison[new_count_col] - comparison[original_count_col]
    comparison['stat'] = stat_name
    return comparison

def get_fill_strategy(feat, feature_tags, form_to_fill_strategy):
    form = feature_tags[feat].get("form")
    return form_to_fill_strategy.get(form, "group_mean")  # default to the safer option if form is missing

def fill_feature_nans(df, feature_cols, feature_tags, form_to_fill_strategy, group_cols=('league', 'position_group')):
    df = df.copy()
    for feat in feature_cols:
        strategy = get_fill_strategy(feat, feature_tags, form_to_fill_strategy)
        if strategy == 'zero':
            df[feat] = df[feat].fillna(0)
        else:
            group_means = df.groupby(list(group_cols))[feat].transform('mean')
            df[feat] = df[feat].fillna(group_means).fillna(0)
    return df

def safe_standardize(x):
    std = x.std(ddof=0)
    if std == 0 or pd.isna(std):
        return x - x.mean()  # every value already equals the mean here, so this is 0 for the whole group
    return (x - x.mean()) / std

def residualize(df, feature_cols, covariate_col, group_cols, robust=False):
    df = df.copy()
    for feat in feature_cols:
        resid_col = feat + '_adj'
        df[resid_col] = np.nan
        for _, idx in df.groupby(group_cols).groups.items():
            sub = df.loc[idx]
            X = sub[[covariate_col]].to_numpy()
            y = sub[feat].to_numpy()
            model = HuberRegressor() if robust else LinearRegression()
            model.fit(X, y)
            df.loc[idx, resid_col] = y - model.predict(X)
        df[resid_col] = df.groupby(["league"] + list(group_cols))[resid_col].transform(safe_standardize)
    return df

def pc1_context_correlation(df, feature_cols, context_col="context_score"):
    sub = df[feature_cols + [context_col]].dropna()
    pc1 = PCA(n_components=1).fit_transform(sub[feature_cols])
    r, _ = stats.pearsonr(pc1.ravel(), sub[context_col])
    return r

def select_position(df, position_group, level='position_group'):
    return df.xs(position_group, level=level, drop_level=False)

def plot_histogram_grid(df, cols, n_cols=6):
    n_rows = -(-len(cols) // n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols*3, n_rows*2.5))
    for ax, col in zip(axes.flatten(), cols):
        df[col].hist(ax=ax, bins=30)
        ax.set_title(col, fontsize=8)
    plt.tight_layout()
    plt.show()

def detect_outliers_zscore(df, feature_cols, player_id_to_player, team_id_to_team, z_thresh=3):
    outlier_report = {}
    for col in feature_cols:
        z = np.abs(stats.zscore(df[col], nan_policy='omit'))
        outlier_idx = df.index[z > z_thresh]
        if len(outlier_idx) > 0:
            outlier_report[col] = df.loc[outlier_idx, ['league', col]].copy()
            outlier_report[col]['player_id'] = outlier_report[col].index.get_level_values('player_id')
            outlier_report[col]['team_id'] = outlier_report[col].index.get_level_values('team_id')
            outlier_report[col]['z_score'] = z[z > z_thresh]
            outlier_report[col]['player'] = outlier_report[col]['player_id'].map(player_id_to_player)
            outlier_report[col]['team'] = outlier_report[col]['team_id'].map(team_id_to_team)
    return outlier_report

def detect_outliers_iqr(df, feature_cols, player_id_to_player, team_id_to_team, k=1.5):
    outlier_report = {}
    for col in feature_cols:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - k*iqr, q3 + k*iqr
        mask = (df[col] < lower) | (df[col] > upper)
        if mask.sum() > 0:
            rows = df.loc[mask, ['league', col]].copy()
            rows['player_id'] = rows.index.get_level_values('player_id')
            rows['team_id'] = rows.index.get_level_values('team_id')
            rows['player'] = rows['player_id'].map(player_id_to_player)
            rows['team'] = rows['team_id'].map(team_id_to_team)
            # add a signed "how far outside the bound" measure, analogous to z_score
            rows['bound_distance'] = np.where(
                rows[col] > upper,
                rows[col] - upper,
                lower - rows[col]
            )
            outlier_report[col] = rows.sort_values('bound_distance', ascending=False)
    return outlier_report

def winsorize(series, lower=0.01, upper=0.99):
    lo, hi = series.quantile([lower, upper])
    return series.clip(lo, hi)

def winsorize_partial_group(df, cols, lower=0.01, upper=0.99):
    # store original sum of just these members, per row, before winsorizing
    original_sum = df[cols].sum(axis=1)

    for col in cols:
        df[col] = winsorize(df[col], lower, upper)

    # rescale so the winsorized pair preserves the SAME total the row originally had
    # (not 1.0, but whatever this player's forward+sideway share actually was)
    new_sum = df[cols].sum(axis=1)
    scale_factor = (original_sum / new_sum).replace([np.inf, -np.inf], np.nan).fillna(1.0)
    for col in cols:
        df[col] = df[col] * scale_factor

    return df

def impute_unreliable_rate_stat(
    all_players_stats, target_df, position_group, pct_col,
    attempted_col=None, derive_from=None, min_quantile=None, min_count=None,
):
    pos_df = all_players_stats.xs(position_group, level='position_group', drop_level=False)

    if derive_from is not None:
        total_col, rate_col = derive_from
        raw_count = pos_df[total_col] * pos_df[rate_col]
    elif attempted_col is not None:
        raw_count = pos_df[attempted_col]
    else:
        raise ValueError("Provide attempted_col or derive_from")

    threshold = raw_count.quantile(min_quantile) if min_quantile is not None else min_count
    eligible = pos_df[raw_count >= threshold]
    ineligible = pos_df[raw_count < threshold]

    league_means = eligible.groupby('league')[pct_col].mean()
    imputed = ineligible['league'].map(league_means).rename('imputed_value')

    target_df = target_df.join(imputed, how='left')  # aligns on the shared index automatically
    mask = target_df['imputed_value'].notna()
    target_df.loc[mask, pct_col] = target_df.loc[mask, 'imputed_value']
    return target_df.drop(columns='imputed_value')

def run_seed_stability_test(X, k, n_seeds=10, algorithm='kmeans', random_state_base=42):
    np.random.seed(random_state_base)
    seeds = np.random.randint(0, 100000, size=n_seeds).tolist()

    all_labels = {}
    for seed in seeds:
        model = KMeans(n_clusters=k, random_state=seed, n_init=10)
        labels = model.fit_predict(X)
        all_labels[seed] = labels

    return all_labels, seeds

def compute_pairwise_stability(all_labels):
    seeds = list(all_labels.keys())
    results = []
    for s1, s2 in combinations(seeds, 2):
        ari = adjusted_rand_score(all_labels[s1], all_labels[s2])
        results.append({'seed_1': s1, 'seed_2': s2, 'ari': ari})
    return pd.DataFrame(results)

def get_mean_stability(all_labels):
    seeds = list(all_labels.keys())
    aris = [adjusted_rand_score(all_labels[s1], all_labels[s2]) for s1, s2 in combinations(seeds, 2)]
    return np.mean(aris)

def to_percentile(df, cols, group_cols=("league", "position_group")):
    df = df.copy()
    for col in cols:
        df[col + "_pctile"] = df.groupby(list(group_cols))[col].rank(pct=True) * 100
    return df

def _series_for(source, features, suffix):  # no default, no special-casing — forces an explicit, literal value
    pct_cols = [f + suffix + '_pctile' for f in features]
    raw_cols = [f + suffix for f in features]
    if isinstance(source, pd.Series):
        pct_vals, raw_vals = source[pct_cols], source[raw_cols]
    else:
        pct_vals, raw_vals = source[pct_cols].mean(), source[raw_cols].mean()
    pct_vals.index = features
    raw_vals.index = features
    return pct_vals, raw_vals

def suffix_label(suffix):
    return suffix_labels.get(suffix, suffix.lstrip('_'))

def pca_top_features(pca, feature_names, n_top=8):
    """Top n_top raw features per retained component, by |loading|, sign preserved."""
    loadings = pca.components_
    out = {}
    for i, comp in enumerate(loadings):
        idx = np.argsort(-np.abs(comp))[:n_top]
        out[f'PC{i+1}'] = pd.DataFrame({
            'feature': [feature_names[j] for j in idx],
            'loading': comp[idx],
            'explained_var_ratio': pca.explained_variance_ratio_[i]
        })
    return out

def pca_feature_importance_overall(pca, feature_names):
    """Overall contribution of each feature across all retained PCs (sums to 1)."""
    sq = pca.components_ ** 2
    weighted = (sq.T * pca.explained_variance_ratio_).T
    importance = weighted.sum(axis=0)
    importance /= importance.sum()
    return (pd.DataFrame({'feature': feature_names, 'importance': importance})
            .sort_values('importance', ascending=False)
            .reset_index(drop=True))

def compute_f_stats_with_p(df, feature_list, cluster_col='cluster', method='welch'):
    """
    F-oneway stat/p-value per feature, or Welch-type ANOVA (alexandergovern)
    if method='welch' -- recommended given your clusters have unequal sizes
    (e.g. n=7 vs n=31), which violates standard ANOVA's equal-variance assumption.
    """
    rows = []
    for col in feature_list:
        groups = [g[col].dropna() for _, g in df.groupby(cluster_col)]
        if method == 'welch':
            try:
                res = stats.alexandergovern(*groups)
                stat, p_val = res.statistic, res.pvalue
            except AttributeError:
                # scipy < 1.7 fallback
                stat, p_val = stats.f_oneway(*groups)
        else:
            stat, p_val = stats.f_oneway(*groups)
        rows.append({'feature': col, 'f_stat': stat, 'f_pvalue': p_val})
    return pd.DataFrame(rows).set_index('feature')

def backproject_cluster_centroids(pca, cluster_centers_pca, feature_names):
    """
    Reconstruct cluster centroids in standardized raw-feature space,
    using only retained components. Works for kmeans.cluster_centers_
    or gmm.means_.
    """
    reconstructed = cluster_centers_pca @ pca.components_
    df = pd.DataFrame(reconstructed, columns=feature_names)
    df.index = [f'Cluster_{i}' for i in range(len(df))]
    return df

def rank_cluster_driving_features(centroid_df, n_top=50):
    """Rank features by spread across cluster centroids (higher = more separating)."""
    spread = centroid_df.std(axis=0)
    ranked = spread.sort_values(ascending=False).head(n_top)
    return pd.DataFrame({'feature': ranked.index, 'cross_cluster_std': ranked.values})

def pairwise_cluster_deltas(centroid_df, cluster_a, cluster_b, n_top=50):
    """For a specific pair (most useful at your k=2/k=3), rank by signed difference."""
    delta = centroid_df.loc[cluster_a] - centroid_df.loc[cluster_b]
    ranked = delta.reindex(delta.abs().sort_values(ascending=False).index).head(n_top)
    return pd.DataFrame({
        'feature': ranked.index,
        'delta': ranked.values,
        'higher_in': np.where(ranked.values > 0, cluster_a, cluster_b)
    })

def select_top_features_per_category_pca(centroid_df, category_pools, n_per_category,
                                           method='spread', cluster_a=None, cluster_b=None):
    """
    Select top N differentiating features per category from PCA-backprojected
    cluster centroids, instead of raw F-oneway stats.

    method='spread'   -> cross-cluster std per feature (same logic as
                          rank_cluster_driving_features). Works for any k;
                          use this as the default, especially for k>2.
    method='pairwise' -> signed delta between two specific clusters (same logic
                          as pairwise_cluster_deltas). Requires cluster_a/cluster_b
                          (e.g. 'Cluster_0', 'Cluster_1'). Useful when you want to
                          isolate one specific split within k=3 (e.g. the small
                          cluster vs. the rest) rather than overall 3-way spread.
    """
    selected = {}
    for category, pool in category_pools.items():
        valid_pool = [c for c in pool if c in centroid_df.columns]
        sub = centroid_df[valid_pool]

        if method == 'spread':
            ranked = sub.std(axis=0).sort_values(ascending=False)
        elif method == 'pairwise':
            if cluster_a is None or cluster_b is None:
                raise ValueError("cluster_a and cluster_b required for method='pairwise'")
            delta = sub.loc[cluster_a] - sub.loc[cluster_b]
            ranked = delta.reindex(delta.abs().sort_values(ascending=False).index)
        else:
            raise ValueError("method must be 'spread' or 'pairwise'")

        n = n_per_category.get(category, 2)
        selected[category] = ranked.head(n).index.tolist()

    return selected

def select_features_combined(df, centroid_df, category_pools, n_per_category,
                               cluster_col='cluster', alpha=0.05,
                               weight_f=0.5, weight_pca=0.5,
                               require_significant=True, anova_method='welch'):
    """
    Select radar features per category using a blended rank of:
      - F-oneway/Welch statistic (raw-value group separation, variance-aware)
      - PCA-backprojected cross-cluster std (mechanistic driver of the actual
        clustering, computed in the same reduced space KMeans/GMM used)

    Combined via percentile rank averaging so the two incompatible scales
    don't need manual normalization.

    require_significant=True: only features with p < alpha are eligible.
    If fewer than n_per_category pass, backfills from the combined ranking
    and prints a warning -- so you're never silently short a feature, but
    you can see when that happened.

    No redundancy pruning -- intentionally correlated features you want to
    keep (e.g. multiple pass-completion variants) are left untouched.
    """
    selected = {}
    diagnostics = {}

    for category, pool in category_pools.items():
        valid_pool = [c for c in pool if c in df.columns and c in centroid_df.columns]
        if not valid_pool:
            selected[category] = []
            continue

        f_df = compute_f_stats_with_p(df, valid_pool, cluster_col, method=anova_method)
        pca_spread = centroid_df[valid_pool].std(axis=0).rename('pca_spread')

        combo = f_df.join(pca_spread)
        combo['f_rank_pct'] = combo['f_stat'].rank(pct=True)
        combo['pca_rank_pct'] = combo['pca_spread'].rank(pct=True)
        combo['combined_score'] = (weight_f * combo['f_rank_pct']
                                    + weight_pca * combo['pca_rank_pct'])
        combo['significant'] = combo['f_pvalue'] < alpha
        combo = combo.sort_values('combined_score', ascending=False)

        n = n_per_category.get(category, 2)

        if require_significant:
            sig_pool = combo[combo['significant']]
            chosen = sig_pool.head(n).index.tolist()
            if len(chosen) < n:
                backfill = combo[~combo.index.isin(chosen)].head(n - len(chosen)).index.tolist()
                if backfill:
                    print(f"[{category}] only {len(chosen)}/{n} features significant "
                          f"(p<{alpha}); backfilled: {backfill}")
                chosen += backfill
        else:
            chosen = combo.head(n).index.tolist()

        selected[category] = chosen
        diagnostics[category] = combo

    return selected, diagnostics

def get_display_name(player_id, team_id, player_id_to_player, team_id_to_team):
    name = player_id_to_player.get(player_id, f"Unknown ({player_id})")
    team = team_id_to_team.get(team_id, f"Unknown ({team_id})")
    return f"{name} ({team})"

def get_folder_name(player_id, team_id, player_id_to_player, team_id_to_team):
    name = player_id_to_player.get(player_id, f"Unknown_{player_id}")
    team = team_id_to_team.get(team_id, f"Unknown_{team_id}")
    # strip parentheses, replace spaces and slashes with underscores
    safe_name = name.replace('/', '-').replace(' ', '_')
    safe_team = team.replace('/', '-').replace(' ', '_')
    return f"{safe_name}_{safe_team}"

def chunk_features(feature_list, max_features_per_plot, radar_sets=None, prefix=None):
    """
    Split feature_list into consecutive chunks of at most max_features_per_plot,
    preserving order. Last chunk may be smaller.

    If radar_sets and prefix are given, each chunk is also registered into
    radar_sets under a generated key (f'{prefix}_1', f'{prefix}_2', ...), and
    the function returns those keys instead of the raw chunks — so they can be
    fed straight into the existing chart_name-based functions with no changes
    to those functions.
    """
    chunks = [
        feature_list[i:i + max_features_per_plot]
        for i in range(0, len(feature_list), max_features_per_plot)
    ]

    if radar_sets is None or prefix is None:
        return chunks

    chart_names = []
    for i, chunk in enumerate(chunks, start=1):
        key = f'{prefix}_{i}'
        radar_sets[key] = chunk
        chart_names.append(key)
    return chart_names

def save_radar_chart(fig, position, n_clusters, folder_name, chart_name, base_dir='radar_charts'):
    folder = os.path.join(base_dir, position, f'k{n_clusters}', folder_name)
    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, f'{chart_name}.png')
    fig.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return filepath

def _draw_similarity_strip(fig, similarity_scores, highlight_label=None, label_threshold=0.06):
    labels = list(similarity_scores.keys())
    values = list(similarity_scores.values())
    strip_colors = plt.cm.Set2.colors

    strip_ax = fig.add_axes([0.12, 0.83, 0.76, 0.08])  # slightly taller than before, for the callouts
    strip_ax.set_xlim(0, 1)
    strip_ax.set_ylim(-1.6, 1.6)  # extra vertical room above/below the bar itself
    strip_ax.axis('off')

    left = 0
    callout_side = 1  # alternates above (+1) / below (-1) for consecutive narrow segments
    for i, (label, val) in enumerate(zip(labels, values)):
        color = strip_colors[i % len(strip_colors)]
        is_hers = (label == highlight_label)
        center = left + val / 2

        strip_ax.barh(0.5, val, left=left, height=1.0, color=color,
                      edgecolor='black' if is_hers else 'white',
                      linewidth=2.0 if is_hers else 0.5)

        text = f"{label}\n{val:.0%}"
        if val >= label_threshold:
            strip_ax.text(center, 0.5, text, ha='center', va='center', fontsize=6,
                          fontweight='bold' if is_hers else 'normal')
        else:
            y_edge = 1.0 if callout_side > 0 else 0.0
            y_label = 1.45 if callout_side > 0 else -0.45
            strip_ax.plot([center, center], [y_edge, y_label], color='gray', linewidth=0.6, zorder=1)
            strip_ax.text(center, y_label + (0.1 if callout_side > 0 else -0.1), text,
                          ha='center', va='bottom' if callout_side > 0 else 'top',
                          fontsize=6, fontweight='bold' if is_hers else 'normal')
            callout_side *= -1  # next narrow segment goes the opposite direction

        left += val

def build_radar_chart(feature_list, pct_series_dict, title, raw_series_dict=None, fmt='.2f',
                       save=False, position=None, n_clusters=None, folder_name=None, chart_name=None,
                       similarity_scores=None, highlight_label=None):
    N = len(feature_list)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    has_strip = similarity_scores is not None
    fig = plt.figure(figsize=(7, 8.2 if has_strip else 7.4))  # extra height for the legend now, too
    polar_rect = [0.1, 0.12, 0.8, 0.69] if has_strip else [0.1, 0.12, 0.8, 0.78]
    ax = fig.add_axes(polar_rect, projection='polar')

    colors = plt.cm.tab10.colors
    lw = 1.5

    for i, (label, pct_vals) in enumerate(pct_series_dict.items()):
        norm_vals = [pct_vals[f] / 100 for f in feature_list]
        norm_vals += norm_vals[:1]

        is_baseline = (i == 0)
        color = 'gray' if is_baseline else colors[(i - 1) % len(colors)]

        ax.plot(angles, norm_vals, label=label, linewidth=lw, color=color)
        if is_baseline:
            ax.fill(angles, norm_vals, alpha=0.08, color=color)

        annotate_vals = raw_series_dict[label] if raw_series_dict else pct_vals
        for angle, norm_val, feat in zip(angles[:-1], norm_vals[:-1], feature_list):
            ax.annotate(f"{annotate_vals[feat]:{fmt}}", xy=(angle, norm_val),
                        fontsize=7, color=color, ha='center', va='bottom')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(feature_list, fontsize=8)
    ax.set_yticklabels([])

    # below the plot now, not above-right -- guaranteed clear of the strip regardless of
    # how many series or how long the labels are, since nothing else occupies this space
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), fontsize=9)

    fig.suptitle(title, y=0.97, fontsize=13)
    if has_strip:
        _draw_similarity_strip(fig, similarity_scores, highlight_label)

    if save:
        return save_radar_chart(fig, position, n_clusters, folder_name, chart_name)
    plt.show()

def plot_cluster_comparison(chart_name, radar_sets, stats_df, column_name='cluster', suffix='_adj'):
    features = radar_sets[chart_name]
    pct_dict, raw_dict = {}, {}
    for c in sorted(stats_df[column_name].unique()):
        members = stats_df[stats_df[column_name] == c]
        pct_vals, raw_vals = _series_for(members, features, suffix)
        label = f'{column_name} {c}'
        pct_dict[label], raw_dict[label] = pct_vals, raw_vals

    build_radar_chart(features, pct_dict,
                       f'{chart_name.title()} — {column_name} comparison ({"raw" if suffix == "" else suffix})',
                       raw_series_dict=raw_dict)

def plot_player_vs_cluster(chart_name, radar_sets, player_id, team_id, stats_df, player_id_to_player,
                            team_id_to_team, column_name='cluster', suffix='_adj', n_clusters=None):
    features = radar_sets[chart_name]
    player_row = stats_df.xs(key=(player_id, team_id), level=('player_id', 'team_id')).iloc[0]
    cluster_id = player_row[column_name]
    cluster_members = stats_df[stats_df[column_name] == cluster_id]
    display_name = get_display_name(player_id, team_id, player_id_to_player, team_id_to_team)

    cluster_pct, cluster_raw = _series_for(cluster_members, features, suffix)
    player_pct, player_raw = _series_for(player_row, features, suffix)

    pct_dict = {f'{column_name} {cluster_id} avg': cluster_pct, display_name: player_pct}
    raw_dict = {f'{column_name} {cluster_id} avg': cluster_raw, display_name: player_raw}

    similarity_scores = highlight_label = None
    if n_clusters is not None:
        similarity_scores = {
            f'Cluster {i}': player_row[f'sim_cluster_{i}_k{n_clusters}'] for i in range(n_clusters)
        }
        highlight_label = f'Cluster {int(cluster_id)}'

    build_radar_chart(features, pct_dict,
                       f'{chart_name.title()} — {display_name} ({"raw" if suffix == "" else suffix})',
                       raw_series_dict=raw_dict,
                       similarity_scores=similarity_scores, highlight_label=highlight_label)

def plot_player_vs_league_cluster(chart_name, radar_sets, player_id, team_id, stats_df, player_id_to_player,
                                   team_id_to_team, column_name='cluster', suffix='_adj', n_clusters=None):
    features = radar_sets[chart_name]
    player_row = stats_df.xs(key=(player_id, team_id), level=('player_id', 'team_id')).iloc[0]
    cluster_id = player_row[column_name]
    league = player_row['league']

    league_cluster_members = stats_df[(stats_df['league'] == league) & (stats_df[column_name] == cluster_id)]
    display_name = get_display_name(player_id, team_id, player_id_to_player, team_id_to_team)

    cluster_pct, cluster_raw = _series_for(league_cluster_members, features, suffix)
    player_pct, player_raw = _series_for(player_row, features, suffix)

    pct_dict = {f'{column_name} {cluster_id} avg ({league})': cluster_pct, display_name: player_pct}
    raw_dict = {f'{column_name} {cluster_id} avg ({league})': cluster_raw, display_name: player_raw}

    similarity_scores = highlight_label = None
    if n_clusters is not None:
        similarity_scores = {
            f'Cluster {i}': player_row[f'sim_cluster_{i}_k{n_clusters}'] for i in range(n_clusters)
        }
        highlight_label = f'Cluster {int(cluster_id)}'

    build_radar_chart(features, pct_dict,
                       f'{chart_name.title()} — {display_name} vs {league} peers ({"raw" if suffix == "" else suffix})',
                       raw_series_dict=raw_dict,
                       similarity_scores=similarity_scores, highlight_label=highlight_label)

def export_cluster_comparison_charts(stats_df, position, n_clusters, chart_names, radar_sets,
                                      column_name='cluster', suffixes=('_adj', '')):
    """
    One radar chart per (chart_name, suffix), comparing all clusters' average stats.
    '_adj' keeps the original plain filename; '' (raw) gets a '_raw' tag, e.g.:
        radar_charts/Goalkeeper/k3/passing.png       <- adj (default)
        radar_charts/Goalkeeper/k3/passing_raw.png   <- raw
    """
    for suffix in suffixes:
        file_tag = f'_{suffix_label(suffix)}'
        for chart_name in chart_names:
            features = radar_sets[chart_name]
            pct_dict, raw_dict = {}, {}
            for c in sorted(stats_df[column_name].unique()):
                cluster_pct, cluster_raw = _series_for(stats_df[stats_df[column_name] == c], features, suffix)
                pct_dict[f'{column_name} {c}'] = cluster_pct
                raw_dict[f'{column_name} {c}'] = cluster_raw

            build_radar_chart(
                features, pct_dict,
                f'{chart_name.title()} — {column_name} comparison ({suffix_label(suffix)})',
                raw_series_dict=raw_dict,
                save=True, position=position, n_clusters=n_clusters,
                folder_name='', chart_name=f'{chart_name}{file_tag}'
            )

def export_cluster_comparison_charts_by_league(stats_df, position, n_clusters, chart_names, radar_sets,
                                                column_name='cluster', suffixes=('_adj', '')):
    """
    One radar chart per (league, chart_name, suffix), cluster averages computed
    within that league only:
        radar_charts/Goalkeeper/k3/passing_(EPL).png
        radar_charts/Goalkeeper/k3/passing_(EPL)_raw.png
    """
    for suffix in suffixes:
        file_tag = f'_{suffix_label(suffix)}'
        for league in stats_df['league'].dropna().unique():
            league_subset = stats_df[stats_df['league'] == league]
            safe_league = str(league).replace('/', '-').replace(' ', '_').replace("'", "")

            for chart_name in chart_names:
                features = radar_sets[chart_name]
                pct_dict, raw_dict = {}, {}
                for c in sorted(league_subset[column_name].unique()):
                    cluster_pct, cluster_raw = _series_for(league_subset[league_subset[column_name] == c], features, suffix)
                    pct_dict[f'{column_name} {c} ({league})'] = cluster_pct
                    raw_dict[f'{column_name} {c} ({league})'] = cluster_raw

                build_radar_chart(
                    features, pct_dict,
                    f'{chart_name.title()} — {column_name} comparison ({league}, {suffix_label(suffix)})',
                    raw_series_dict=raw_dict,
                    save=True, position=position, n_clusters=n_clusters,
                    folder_name='', chart_name=f'{chart_name}{file_tag}_{safe_league}'
                )

def export_all_player_charts(stats_df, position, n_clusters, chart_names, radar_sets, cluster_col,
                              player_id_to_player, team_id_to_team, suffixes=('_adj', ''),
                              include_similarity=True):
    similarity_available = include_similarity and f'sim_cluster_0_k{n_clusters}' in stats_df.columns

    for suffix in suffixes:
        file_tag = f'_{suffix_label(suffix)}'
        for idx, row in stats_df.iterrows():
            idx_map = dict(zip(stats_df.index.names, idx))
            player_id, team_id = idx_map['player_id'], idx_map['team_id']
            cluster_id = row[cluster_col]
            display_name = get_display_name(player_id, team_id, player_id_to_player, team_id_to_team)
            folder_name = get_folder_name(player_id, team_id, player_id_to_player, team_id_to_team)
            cluster_members = stats_df[stats_df[cluster_col] == cluster_id]

            similarity_scores = highlight_label = None
            if similarity_available:
                similarity_scores = {
                    f'Cluster {i}': row[f'sim_cluster_{i}_k{n_clusters}'] for i in range(n_clusters)
                }
                highlight_label = f'Cluster {int(cluster_id)}'

            for chart_name in chart_names:
                features = radar_sets[chart_name]
                cluster_pct, cluster_raw = _series_for(cluster_members, features, suffix)
                player_pct, player_raw = _series_for(row, features, suffix)

                build_radar_chart(
                    features,
                    {f'Cluster {cluster_id} avg': cluster_pct, display_name: player_pct},
                    f'{chart_name.title()} — {display_name} ({suffix_label(suffix)})',
                    raw_series_dict={f'Cluster {cluster_id} avg': cluster_raw, display_name: player_raw},
                    save=True, position=position, n_clusters=n_clusters,
                    folder_name=folder_name, chart_name=f'{chart_name}{file_tag}',
                    similarity_scores=similarity_scores, highlight_label=highlight_label,
                )

def export_all_player_charts_league_aware(stats_df, position, n_clusters, chart_names, radar_sets, cluster_col,
                                           player_id_to_player, team_id_to_team, suffixes=('_adj', ''),
                                           include_similarity=True):
    similarity_available = include_similarity and f'sim_cluster_0_k{n_clusters}' in stats_df.columns

    for suffix in suffixes:
        file_tag = f'_{suffix_label(suffix)}'
        for idx, row in stats_df.iterrows():
            idx_map = dict(zip(stats_df.index.names, idx))
            player_id, team_id = idx_map['player_id'], idx_map['team_id']
            league, cluster_id = row['league'], row[cluster_col]
            display_name = get_display_name(player_id, team_id, player_id_to_player, team_id_to_team)
            folder_name = get_folder_name(player_id, team_id, player_id_to_player, team_id_to_team)
            league_cluster_members = stats_df[(stats_df['league'] == league) & (stats_df[cluster_col] == cluster_id)]

            similarity_scores = highlight_label = None
            if similarity_available:
                similarity_scores = {
                    f'Cluster {i}': row[f'sim_cluster_{i}_k{n_clusters}'] for i in range(n_clusters)
                }
                highlight_label = f'Cluster {int(cluster_id)}'

            for chart_name in chart_names:
                features = radar_sets[chart_name]
                cluster_pct, cluster_raw = _series_for(league_cluster_members, features, suffix)
                player_pct, player_raw = _series_for(row, features, suffix)

                build_radar_chart(
                    features,
                    {f'Cluster {cluster_id} avg ({league})': cluster_pct, display_name: player_pct},
                    f'{chart_name.title()} — {display_name} vs {league} peers ({suffix_label(suffix)})',
                    raw_series_dict={f'Cluster {cluster_id} avg ({league})': cluster_raw, display_name: player_raw},
                    save=True, position=position, n_clusters=n_clusters,
                    folder_name=folder_name, chart_name=f'{chart_name}{file_tag}_league_relative',
                    similarity_scores=similarity_scores, highlight_label=highlight_label,
                )

def match_clusters(centroids_a, centroids_b):
    """Hungarian-algorithm pairing between two sets of centroids (labels are arbitrary between runs)."""
    dist = np.linalg.norm(centroids_a[:, None, :] - centroids_b[None, :, :], axis=2)
    row, col = optimize.linear_sum_assignment(dist)
    return dict(zip(row, col))

def cosine_sim(a, b):
    """Direction/shape similarity between two centroid vectors."""
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return np.dot(a, b) / denom if denom else np.nan

def get_feature_order(X_std, candidate_features, method="pca", n_components=3):
    """
    method='pca':   order by summed abs. loading on top n_components (adds
                    the most-separating features first).
    method='given': returns candidate_features unchanged, for manual/domain order.
    """
    if method == "given":
        return list(candidate_features)
    pca = PCA(n_components=n_components).fit(X_std[candidate_features])
    loading_strength = np.abs(pca.components_).sum(axis=0)
    return list(np.array(candidate_features)[np.argsort(-loading_strength)])

def stability_vs_baseline(X_std, feature_order, k, baseline_n, test_ns, seed=42, n_init=10):
    """
    Fits ONE baseline clustering at baseline_n features. Every n in test_ns
    is compared directly against that same baseline -- not against the
    previous step -- so a single noisy transition can't cascade. One seed
    throughout, no multi-seed averaging needed.
    """
    feats_base = feature_order[:baseline_n]
    km_base = KMeans(n_clusters=k, random_state=seed, n_init=n_init).fit(X_std[feats_base].values)
    base_labels, base_centroids = km_base.labels_, km_base.cluster_centers_
    base_sizes = pd.Series(base_labels).value_counts()

    curve_rows = []
    tracking_df = pd.DataFrame(index=X_std.index)
    tracking_df["baseline_cluster"] = base_labels

    for n in test_ns:
        feats = feature_order[:n]
        km = KMeans(n_clusters=k, random_state=seed, n_init=n_init).fit(X_std[feats].values)
        labels, centroids = km.labels_, km.cluster_centers_

        ic = [feats.index(f) for f in feats_base]        # feats_base is always a prefix of feats
        match = match_clusters(base_centroids, centroids[:, ic])          # {base_idx: new_idx}
        remap = {new_idx: base_idx for base_idx, new_idx in match.items()}
        remapped_labels = np.array([remap[l] for l in labels])

        ari = adjusted_rand_score(base_labels, remapped_labels)
        pct_switched = float((remapped_labels != base_labels).mean())
        sims = [cosine_sim(base_centroids[i, :], centroids[j, ic]) for i, j in match.items()]

        remapped_sizes = pd.Series(remapped_labels).value_counts()
        size_diffs = [
            abs(remapped_sizes.get(i, 0) - base_sizes.get(i, 0)) / max(base_sizes.get(i, 0), 1)
            for i in base_sizes.index
        ]

        curve_rows.append(dict(
            n_features=n, pct_players_switched=pct_switched, ari=ari,
            prototype_sim=np.mean(sims), min_prototype_sim=np.min(sims),
            mean_size_drift=np.mean(size_diffs),
        ))
        tracking_df[f"cluster_at_{n}"] = remapped_labels

    cluster_cols = [c for c in tracking_df.columns if c.startswith("cluster_at_")]
    tracking_df["switched_from_baseline"] = tracking_df[cluster_cols].ne(tracking_df["baseline_cluster"], axis=0).any(axis=1)

    return pd.DataFrame(curve_rows), tracking_df

def plot_stability_vs_baseline(curve_df, position, k, baseline_n):
    fig, axes = plt.subplots(4, 1, figsize=(9, 10), sharex=True)

    axes[0].plot(curve_df["n_features"], curve_df["pct_players_switched"], marker="o", color="crimson")
    axes[0].axhline(0.05, color="gray", linestyle="--", alpha=0.4)
    axes[0].set_ylabel("% players switched\n(vs baseline)")

    axes[1].plot(curve_df["n_features"], curve_df["ari"], marker="o")
    axes[1].axhline(0.9, color="gray", linestyle="--", alpha=0.4)
    axes[1].set_ylabel("ARI vs baseline")

    axes[2].plot(curve_df["n_features"], curve_df["prototype_sim"], marker="o", color="orange", label="mean")
    axes[2].plot(curve_df["n_features"], curve_df["min_prototype_sim"], marker="o", color="orange", alpha=0.4, label="worst cluster")
    axes[2].axhline(0.97, color="gray", linestyle="--", alpha=0.4)
    axes[2].set_ylabel("Prototype cosine sim")
    axes[2].legend(fontsize=8)

    axes[3].plot(curve_df["n_features"], curve_df["mean_size_drift"], marker="o", color="green")
    axes[3].axhline(0.15, color="gray", linestyle="--", alpha=0.4)
    axes[3].set_ylabel("Mean size drift")
    axes[3].set_xlabel("Number of features")

    for ax in axes:
        ax.axvline(baseline_n, color="black", linestyle=":", alpha=0.6)

    fig.suptitle(f"{position} — stability vs baseline (n={baseline_n}), k={k}")
    plt.tight_layout()
    plt.show()

def assignment_stability_sweep(X_pca_full, n_values, k_values, reference_n=None, random_state=42, n_init=10):
    if reference_n is None:
        reference_n = max(n_values)
    rows = []
    for k in k_values:
        reference_labels = KMeans(n_clusters=k, n_init=n_init, random_state=random_state).fit_predict(X_pca_full[:, :reference_n])
        for n in n_values:
            labels_n = KMeans(n_clusters=k, n_init=n_init, random_state=random_state).fit_predict(X_pca_full[:, :n])
            rows.append({'n': n, 'k': k, 'ari_vs_reference': adjusted_rand_score(labels_n, reference_labels)})
    return pd.DataFrame(rows)

def plot_assignment_stability(stab_df, position_name):
    fig, ax = plt.subplots(figsize=(8, 4))
    colors = plt.cm.tab10.colors
    for i, k in enumerate(sorted(stab_df['k'].unique())):
        sub = stab_df[stab_df['k'] == k].sort_values('n')
        ax.plot(sub['n'], sub['ari_vs_reference'], marker='o', label=f'k={k}', color=colors[i])
    ax.axhline(0.8, color='gray', linestyle='--', linewidth=1, alpha=0.6, label='rough "strong agreement" guide')
    ax.set_xlabel('Number of PCA components (n)')
    ax.set_ylabel(f'ARI vs reference (n={stab_df["n"].max()})')
    ax.set_title(f'{position_name} — assignment stability vs n')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

def cluster_size_balance_sweep(X_pca_full, n_values, k, random_state=42, n_init=10):
    rows = []
    for n in n_values:
        labels = KMeans(n_clusters=k, n_init=n_init, random_state=random_state).fit_predict(X_pca_full[:, :n])
        sizes = pd.Series(labels).value_counts(normalize=True).sort_index()
        rows.append({'n': n, 'k': k, 'min_cluster_share': sizes.min()})
    return pd.DataFrame(rows)

def run_position_stability_check(X_pca_full, n_values, k_values, position_name, reference_n=None, random_state=42, n_init=10):
    stab_df = assignment_stability_sweep(X_pca_full, n_values, k_values, reference_n=reference_n,
                                          random_state=random_state, n_init=n_init)
    plot_assignment_stability(stab_df, position_name)

    balance_df = pd.concat([
        cluster_size_balance_sweep(X_pca_full, n_values, k, random_state=random_state, n_init=n_init)
        for k in k_values
    ], ignore_index=True)

    flagged = balance_df[balance_df['min_cluster_share'] < 0.10]
    if not flagged.empty:
        print(f"\n{position_name}: possible outlier-driven splits (min cluster share < 10%):")
        display(flagged)

    return stab_df, balance_df

# ---- 1. core metric computation, one fit at a time ----
def compute_separation_metrics(X, labels, centers):
    mean_sil = silhouette_score(X, labels)
    sample_sil = silhouette_samples(X, labels)
    worst_cluster_sil = pd.Series(sample_sil, index=labels).groupby(level=0).mean().min()
    db = davies_bouldin_score(X, labels)
    min_centroid_dist = spatial.distance.pdist(centers).min()
    return {
        'mean_silhouette': mean_sil,
        'worst_cluster_silhouette': worst_cluster_sil,
        'davies_bouldin': db,
        'min_centroid_dist': min_centroid_dist,
    }

# ---- 2. fit PCA once at the largest n you'll test ----
def fit_full_pca(X_std, max_n_components, random_state=42):
    """Fit PCA once at the largest n you'll test — PCA is nested, so slicing
    X_pca_full[:, :n] for smaller n is identical to refitting at that n."""
    pca_full = PCA(n_components=max_n_components, random_state=random_state).fit(X_std)
    X_pca_full = pca_full.transform(X_std)
    return pca_full, X_pca_full

# ---- 3. sweep across n and k, slicing the same PCA fit each time ----
def separation_sweep_pca(X_pca_full, n_values, k_values, random_state=42, n_init=10):
    rows = []
    for n in n_values:
        X_n = X_pca_full[:, :n]
        avg_pairwise_dist = spatial.distance.pdist(X_n).mean()
        for k in k_values:
            km = KMeans(n_clusters=k, n_init=n_init, random_state=random_state)
            labels = km.fit_predict(X_n)
            metrics = compute_separation_metrics(X_n, labels, km.cluster_centers_)
            metrics['min_centroid_dist_normalized'] = metrics['min_centroid_dist'] / avg_pairwise_dist
            rows.append({'n': n, 'k': k, **metrics})
    return pd.DataFrame(rows)

# ---- 4. tables, one per k ----
def print_separation_tables(sep_df, position_name=None):
    for k in sorted(sep_df['k'].unique()):
        table = sep_df[sep_df['k'] == k].drop(columns='k').set_index('n').round(4)
        print(f"\n===== {position_name or ''} k={k} =====")
        display(table)

# ---- 5. per-position 4-panel: all metrics, one line per k ----
def plot_separation_metrics(sep_df, position_name):
    metrics = ['mean_silhouette', 'worst_cluster_silhouette', 'davies_bouldin', 'min_centroid_dist_normalized']
    titles = ['Mean silhouette', 'Worst-cluster silhouette', 'Davies-Bouldin (lower better)', 'Min centroid dist (normalized)']

    fig, axes = plt.subplots(len(metrics), 1, figsize=(9, 11), sharex=True)
    colors = plt.cm.tab10.colors
    for ax, metric, title in zip(axes, metrics, titles):
        for i, k in enumerate(sorted(sep_df['k'].unique())):
            sub = sep_df[sep_df['k'] == k].sort_values('n')
            ax.plot(sub['n'], sub[metric], marker='o', label=f'k={k}', color=colors[i])
        ax.set_ylabel(title, fontsize=9)
        ax.grid(alpha=0.3)
    axes[0].legend(loc='best', fontsize=8)
    axes[-1].set_xlabel('Number of PCA components (n)')
    fig.suptitle(f'{position_name} — separation vs n_components', y=1.0)
    plt.tight_layout()
    plt.show()

# ---- 6. n x k heatmap for a single position — fast scan of every combination ----
def plot_position_heatmap(sep_df, position_name, metric='mean_silhouette'):
    pivot = sep_df.pivot(index='n', columns='k', values=metric).sort_index(ascending=False)
    cmap = 'RdYlGn_r' if metric == 'davies_bouldin' else 'RdYlGn'

    fig, ax = plt.subplots(figsize=(1.5 + 1.2 * len(pivot.columns), 0.4 * len(pivot) + 1.5))
    im = ax.imshow(pivot.values, cmap=cmap, aspect='auto')

    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([f'k={k}' for k in pivot.columns])
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_ylabel('n components')

    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            val = pivot.values[i, j]
            if not np.isnan(val):
                ax.text(j, i, f'{val:.3f}', ha='center', va='center', fontsize=8)

    ax.set_title(f'{position_name} — {metric.replace("_", " ")} across n × k')
    fig.colorbar(im, ax=ax, shrink=0.8)
    plt.tight_layout()
    plt.show()

def run_position_separation_analysis(X_std, max_n_components, position_name,
                                      n_values=None, k_values=[2, 3, 4],
                                      reference_n=None,
                                      random_state=42, n_init=30,
                                      heatmap_metric='mean_silhouette'):
    """
    One call per position: fits PCA, sweeps separation metrics, sweeps
    assignment stability against a reference n, and screens for
    outlier-driven splits -- all in one pass.
    """
    if n_values is None:
        n_values = range(2, max_n_components + 1)
    if reference_n is None:
        reference_n = max(n_values)

    pca_full, X_pca_full = fit_full_pca(X_std, max_n_components, random_state=random_state)

    sep_df = separation_sweep_pca(X_pca_full, n_values, k_values, random_state=random_state, n_init=n_init)
    print_separation_tables(sep_df, position_name=position_name)
    plot_separation_metrics(sep_df, position_name)
    plot_position_heatmap(sep_df, position_name, metric=heatmap_metric)

    stab_df = assignment_stability_sweep(X_pca_full, n_values, k_values, reference_n=reference_n,
                                          random_state=random_state, n_init=n_init)
    plot_assignment_stability(stab_df, position_name)

    balance_df = pd.concat([
        cluster_size_balance_sweep(X_pca_full, n_values, k, random_state=random_state, n_init=n_init)
        for k in k_values
    ], ignore_index=True)
    flagged = balance_df[balance_df['min_cluster_share'] < 0.10]
    if not flagged.empty:
        print(f"\n{position_name}: possible outlier-driven splits (min cluster share < 10%):")
        display(flagged)

    print(f"\n{position_name} — quick verdict per k (ARI vs reference n={reference_n}):")
    for k in k_values:
        sub = stab_df[(stab_df['k'] == k) & (stab_df['n'] < reference_n)]
        median_ari = sub['ari_vs_reference'].median()
        verdict = "likely dimension-dilution artifact (assignments stable)" if median_ari >= 0.7 \
            else "possible genuine divergence (assignments shift with n)"
        print(f"  k={k}: median ARI = {median_ari:.3f} -> {verdict}")

    return {'pca': pca_full, 'X_pca_full': X_pca_full, 'sep_df': sep_df,
            'stab_df': stab_df, 'balance_df': balance_df}

def compute_soft_cluster_spectrum(X_pca, kmeans_model, stats_df, sigma_quantile=0.5):
    """
    (same docstring as before, with these changes:)
    - id_cols parameter removed: identity is now carried by stats_df's own
      MultiIndex (player_id, team_id, position_group), so there's nothing
      left to extract into columns before joining.
    - X_pca must be row-aligned with stats_df's INDEX specifically -- see
      the alignment warning below the function.
    """
    X_pca = np.asarray(X_pca)
    centroids = kmeans_model.cluster_centers_
    n_clusters = centroids.shape[0]

    assert len(X_pca) == len(stats_df), "X_pca and stats_df row counts differ"
    assert stats_df.index.is_unique, "stats_df index has duplicate player-team rows"

    dists = np.linalg.norm(X_pca[:, None, :] - centroids[None, :, :], axis=2)
    hard_cluster = np.argmin(dists, axis=1)

    own_dist = dists[np.arange(len(X_pca)), hard_cluster]
    sigma = max(np.quantile(own_dist, sigma_quantile), 1e-8)

    sim_raw = np.exp(-(dists ** 2) / (2 * sigma ** 2))
    sim = sim_raw / sim_raw.sum(axis=1, keepdims=True)

    # built directly on stats_df's own index -- no id_cols extraction needed
    out = pd.DataFrame(index=stats_df.index)
    for cluster_idx in range(n_clusters):
        out[f'dist_to_cluster_{cluster_idx}_k{n_clusters}'] = dists[:, cluster_idx]
    for cluster_idx in range(n_clusters):
        out[f'sim_cluster_{cluster_idx}_k{n_clusters}'] = sim[:, cluster_idx]
    out[f'hard_cluster_k{n_clusters}'] = hard_cluster
    sim_sorted = np.sort(sim, axis=1)[:, ::-1]
    out[f'margin_k{n_clusters}'] = sim_sorted[:, 0] - sim_sorted[:, 1]
    out[f'sigma_used_k{n_clusters}'] = sigma

    return stats_df.join(out)  # joins on shared index labels, not row position

def build_subcluster_adj(df, cluster_col, feature_cols, covariate_col, clusters_to_refit):
    df = df.copy()
    for cluster_id in df[cluster_col].unique():
        sub_idx = df[df[cluster_col] == cluster_id].index
        if cluster_id in clusters_to_refit:
            refit = residualize(
                df.loc[sub_idx], feature_cols=feature_cols, covariate_col=covariate_col,
                group_cols=[cluster_col], robust=True,
            )
            for feat in feature_cols:
                df.loc[sub_idx, feat + "_subcluster_adj"] = refit[feat + "_adj"]
        else:
            for feat in feature_cols:
                df.loc[sub_idx, feat + "_subcluster_adj"] = (
                    df.loc[sub_idx].groupby("league")[feat + "_adj"].transform(safe_standardize)
                )
    return df