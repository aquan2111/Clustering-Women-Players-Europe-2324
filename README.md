<p align="right"><img alt="Hudl StatsBomb logo" src="https://raw.githubusercontent.com/statsbomb/logos/main/HudlStatsbomb_Python.svg" height="28"></p>

# Clustering-Women-Players-Europe-2324

The goal of the project is to group players in 4 European leagues (English FA Women's Super League, German Frauen Bundesliga, Spanish Liga F, and Italian Serie A Women) by how they play.

Data: [StatsBomb Open Data](https://github.com/statsbomb/open-data).

## What this project answers

- What types of goalkeepers, center backs, full/wing backs, center midfielders, wingers, and center forwards exist across all four leagues?
- For a player, which type does she belong to, and how firmly does she fit it?

## The data

- StatsBomb event data for 2023/2024 season: every pass, carry, reception, duel, interception, clearance, save, etc.
- Each player is profiled per position, using only her minutes there. The minimum number of minutes required per player is 35% of total minutes of the season. For example, for a player used at both center back and full back, she gets two separate profiles.
- A player who moves mid season appears once per club.

## Player counts

| Position | Players |
| --- | --- |
| Goalkeepers | 60 |
| Center Backs | 154 |
| Full/Wing Backs | 129 |
| Center Midfielders | 182 |
| Wingers | 85 |
| Center Forwards | 76 |

## How players were grouped

1. **Style, not output.** A profile describes habits, such as which way she passes and how far, where she receives the ball, or how high she defends. How good she is (pass completion rate, duels won), and how much she does everything is kept out of the grouping.
2. **Compared with her own league.** Every number is measured against players in the same position in the same league.
3. **Adjusted for team strength.** Initial results put players at top clubs (such as Chelsea, Barcelona, Bayern, AS Roma) together in almost every position, so the system was spotting players playing for a dominant side rather than a style. Therefore, each team is rated on possession, expected goals difference, and pressing intensity via PPDA (passes per defensive action). Each player is then compared with what a player in her team's situation would normally do. Serie A Women had a different split format that season, so each opponent counts equally.
4. **Grouped by style, position by position.** The main view splits each position into two main styles, with a finer three-way split where it held up. Only groupings that came back similar every time the analysis was re-run in different ways were kept. For center midfielders, the grouping was first done into three groups: deeper, central, and advanced roles, before further grouping was done within each group.
5. **Described in football terms.** Each style is described by what sets it apart, with roles from football video games like Football Manager and EA Sports FC also used as reference.

## How to read the charts

The example below is Alessia Russo (Arsenal), center forward, in the three-style view.

Her own line is the same in both rows, only the grey shape changes. Read across a row to see what the strength adjustment changes, and down a column to see the effect of comparing only with her league.

<table>
  <tr>
    <th></th>
    <th>Strength-adjusted (<code>adj</code>)</th>
    <th>As observed (<code>raw</code>)</th>
  </tr>
  <tr>
    <th>vs her group,<br>all four leagues</th>
    <td width="45%"><img src="radar_plots/Center%20Forward/k3/Alessia_Russo_Arsenal_WFC/carrying_dribbling_shooting_receipt_adj.png" width="100%"></td>
    <td width="45%"><img src="radar_plots/Center%20Forward/k3/Alessia_Russo_Arsenal_WFC/carrying_dribbling_shooting_receipt_raw.png" width="100%"></td>
  </tr>
  <tr>
    <th>vs her group,<br>her league only</th>
    <td width="45%"><img src="radar_plots/Center%20Forward/k3/Alessia_Russo_Arsenal_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" width="100%"></td>
    <td width="45%"><img src="radar_plots/Center%20Forward/k3/Alessia_Russo_Arsenal_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" width="100%"></td>
  </tr>
</table>

- Each spoke shows her percentile against players in the same position in the same league. The outer edge is the top of the league.
- The grey shape is her group's average, while the coloured line is the player's stats.
- **adj** charts are strength adjusted, use these to compare styles.
- **raw** charts show her numbers as they happened, which is what you would see watching her.
- The bar at the top shows how strongly she fits each style. A split bar means she sits between styles.
- **vs FA Women's Super League peers** charts compare her only with group members from her own league

### Example chart labels

| Label | Meaning |
| --- | --- |
| shot open play head pct | Percentage of her open play shots with the head |
| carry distance avg | Average of the distance of all her carries |
| receipt x avg | How far up the pitch she receives the ball |

## Limitations

### Data

- **One season.** All the profiles describe only the season 2023/2024 rather than a fixed identity. The styles shown in this season may not be the same as other seasons.
- **On the ball only.** All the stats only describe actions on the ball, while movements off the ball, positioning when nothing happens, and decisions not to act do not show up in events data.
- **Small samples.** Players with few minutes at a position, and rare actions such as sweeps and fouls, are less reliable. A rate built from only a handful of events was replaced with the league norm.
- **Serie A Women's split season.** After 18 rounds, the league was split into a championship round and a relegation round. Team strength accounts for this, but players' own numbers still reflect who they faced.

### Team strength adjustment

- **It removes more than circumstance.** It removes whatever tends to go with playing for a dominant side. This includes having more of the ball, but it can also include habits that top clubs coach into their players. A player's adjusted chart can therefore underestimate a trait she would keep at any club.
- **It assumes team strength works steadily.** It treats every step up the table, from bottom side to mid table to title contender, as shifting a player's numbers by the same amount in the same direction.
- **It assumes team strength works the same way in every league.** One correction per position is used for all four leagues, so being near the top of your league is assumed to change a player's numbers by the same amount. If team strength plays more strongly in one league than in another, that league's players will be slightly under- or over-corrected. The leagues were combined because each one alone has too few players at a position for a reliable correction.
- **Barcelona players are the hardest case.** Barcelona dominated Liga F by far more than any other club dominated its league, so their adjustment rests on the least evidence. Their adjusted charts should be read alongside their raw ones.

### Reading the results

- **Style is not quality.** Two players landing in the same group play the same way, but nothing can be said whether who is better.
- **Leagues are not ranked against each other.** Percentiles and team strength are both measured within league. A top 10% center back in Serie A Women and a top 10% center back in Frauen Bundesliga are near the top of their own league, but they are not guaranteed to be equal.
- **Styles are tendencies, not boxes.** Many players sit between groups, which can be seen at the bar at the top of each chart showing how firmly she fits.
- **Names are interpretation.** Group names and Football Manager/EA Sports FC roles are the closest football description of what the data shows, not the labels the data produced.

## Folder guide

- `findings/`: Write-ups by position (markdown and PDF)
- `radar_plots/<Position>/k2`, `k3`: Two and three style views, with one folder per player inside.
- `code/`: notebooks and functions
