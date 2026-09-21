# **Center Midfields Attacking**

<a id="table-of-contents"></a>

## **Table of Contents**

- <a href="#player-counts" style="color:black">Player counts</a>
- <a href="#results" style="color:black">Results</a>
  - <a href="#results-for-2-clusters" style="color:black">Results for 2 clusters</a>
    - <a href="#breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
    - <a href="#breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
  - <a href="#breakdown-of-results-by-players" style="color:black">Breakdown of results by players</a>
    - <a href="#breakdown-of-results-by-players-aitana-bonmati-barcelona" style="color:black">Aitana Bonmati - Barcelona</a>
    - <a href="#breakdown-of-results-by-players-julia-grosso-juventus" style="color:black">Julia Grosso - Juventus</a>
    - <a href="#breakdown-of-results-by-players-jill-roord-manchester-city" style="color:black">Jill Roord - Manchester City</a>
    - <a href="#breakdown-of-results-by-players-svenja-huth-vfl-wolfsburg" style="color:black">Svenja Huth - VfL Wolfsburg</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-center-midfields-averages" style="color:black">Radar plots for 2 clusters center midfields' averages</a>
    - <a href="#fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#liga-f" style="color:black">Liga F</a>
    - <a href="#serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-players" style="color:black">Radar plots for players</a>
    - <a href="#radar-plots-for-players-aitana-bonmati-barcelona" style="color:black">Aitana Bonmati - Barcelona</a>
      - <a href="#aitana-bonmati-barcelona-center-midfield-3-cluster-plots" style="color:black">Center Midfield — 3 cluster plots</a>
      - <a href="#aitana-bonmati-barcelona-attacking-sub-position-2-cluster-plots" style="color:black">Attacking sub-position — 2 cluster plots</a>
    - <a href="#radar-plots-for-players-julia-grosso-juventus" style="color:black">Julia Grosso - Juventus</a>
      - <a href="#julia-grosso-juventus-center-midfield-3-cluster-plots" style="color:black">Center Midfield — 3 cluster plots</a>
      - <a href="#julia-grosso-juventus-attacking-sub-position-2-cluster-plots" style="color:black">Attacking sub-position — 2 cluster plots</a>
    - <a href="#radar-plots-for-players-jill-roord-manchester-city" style="color:black">Jill Roord - Manchester City</a>
      - <a href="#jill-roord-manchester-city-center-midfield-3-cluster-plots" style="color:black">Center Midfield — 3 cluster plots</a>
      - <a href="#jill-roord-manchester-city-attacking-sub-position-2-cluster-plots" style="color:black">Attacking sub-position — 2 cluster plots</a>
    - <a href="#radar-plots-for-players-svenja-huth-vfl-wolfsburg" style="color:black">Svenja Huth - VfL Wolfsburg</a>
      - <a href="#svenja-huth-vfl-wolfsburg-center-midfield-3-cluster-plots" style="color:black">Center Midfield — 3 cluster plots</a>
      - <a href="#svenja-huth-vfl-wolfsburg-attacking-sub-position-2-cluster-plots" style="color:black">Attacking sub-position — 2 cluster plots</a>


<a id="player-counts"></a>

## **Player counts**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

In this project, there are a total of 43 attacking center midfields considered, with

* 21 attacking center midfields in 12 teams in the English FA Women's Super League
* 19 attacking center midfields in 12 teams in the German Frauen Bundesliga
* 26 attacking center midfields in 16 teams in the Spanish Liga F
* 17 attacking center midfields in 10 teams in the Italian Serie A Women

<a id="results"></a>

## **Results**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-2-clusters"></a>

### **Results for 2 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="breakdown-of-results-by-league"></a>

#### **Breakdown of results by league**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">
<table border="1">
  <thead>
    <tr>
      <th>league</th>
      <th>FA Women's Super League</th>
      <th>Frauen Bundesliga</th>
      <th>Liga F</th>
      <th>Serie A Women</th>
    </tr>
    <tr>
      <th>kmeans_2_cluster</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>3</td>
      <td>7</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>4</td>
      <td>8</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>

The split is quite equal for all leagues.

<a id="breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 midfielders involved in higher up the pitch positions, including receiving, pressing, commiting fouls, and other vulnerability features. They also made counterpress actions at higher rates. Passing was their main progression method.
* On the other hand, cluster 1 midfielders made more ground passes and carried longer. They progressed more by carrying. Average press time for these players was longer.

Therefore, based on these results,

* Cluster 0 attacking midfielders can be seen as advanced high pressing operators, acting as shadow strikers.
* Cluster 1 attacking midfielders can be seen as deeper distributors and carriers, although can still be seen as advanced playmakers.

<a id="breakdown-of-results-by-players"></a>

### **Breakdown of results by players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="breakdown-of-results-by-players-aitana-bonmati-barcelona"></a>

#### **Aitana Bonmati - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

The three time Ballon D'or winner from 2023 to 2025 was clustered confidently with shadow strikers. She was involved at advanced locations up the pitch, including receiving, dribbling, pressing, turnovers. She was also active in counterpressing in opposition half and receiving inside opposition box. On the other hand, her passes were shorter and on the ground.

<a id="breakdown-of-results-by-players-julia-grosso-juventus"></a>

#### **Julia Grosso - Juventus**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Grosso was safely clustered with advanced playmakers. Most of her passes were on the ground. Receiving and pressing locations were lower down the pitch, while the other way around could be observed in dribbling and turnovers. She was not heavily involved in counterpress actions, but held the press longer.

<a id="breakdown-of-results-by-players-jill-roord-manchester-city"></a>

#### **Jill Roord - Manchester City**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Roord was closely clustered with shadow strikers. This can be seen in her receipts, presses, and turnovers happening higher up the pitch and counterpress actions in opposing half. Nevertheless, her passes were longer with high share of switches, and her carries were longer and faster.

<a id="breakdown-of-results-by-players-svenja-huth-vfl-wolfsburg"></a>

#### **Svenja Huth - VfL Wolfsburg**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Huth was marginally clustered with advanced playmakers. Her carries were longer and faster than average, while her low passes made up a significant proportion. On the other hand, she was more active at advanced zones and engaged in more counterpressing actions in opposition half. Most of her progression was done via passing.

<a id="appendix"></a>

## **Appendix**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-midfields-averages"></a>

### **Radar plots for 2 clusters center midfields' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_raw.png" alt="Center Midfields Attacking Passing Raw Comparison">

Figure 1: Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_subcluster_adj.png" alt="Center Midfields Attacking Passing Subcluster Adjusted Comparison">

Figure 2: Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw.png" alt="Center Midfields Attacking Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 3: Center Midfields Attacking Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj.png" alt="Center Midfields Attacking Carrying Receipt Dribbling Shooting Subcluster Adjusted Comparison">

Figure 4: Center Midfields Attacking Carrying Receipt Dribbling Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw.png" alt="Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 5: Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj.png" alt="Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison">

Figure 6: Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_raw_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Passing Raw Comparison">

Figure 7: England Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Passing Subcluster Adjusted Comparison">

Figure 8: England Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 9: England Center Midfields Attacking Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Carrying Receipt Dribbling Shooting Subcluster Adjusted Comparison">

Figure 10: England Center Midfields Attacking Carrying Receipt Dribbling Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 11: England Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison">

Figure 12: England Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Passing Raw Comparison">

Figure 13: Germany Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Passing Subcluster Adjusted Comparison">

Figure 14: Germany Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 15: Germany Center Midfields Attacking Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Carrying Receipt Dribbling Shooting Subcluster Adjusted Comparison">

Figure 16: Germany Center Midfields Attacking Carrying Receipt Dribbling Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 17: Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison">

Figure 18: Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_raw_Liga_F.png" alt="Spain Center Midfields Attacking Passing Raw Comparison">

Figure 19: Spain Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_Liga_F.png" alt="Spain Center Midfields Attacking Passing Subcluster Adjusted Comparison">

Figure 20: Spain Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_Liga_F.png" alt="Spain Center Midfields Attacking Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 21: Spain Center Midfields Attacking Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_Liga_F.png" alt="Spain Center Midfields Attacking Carrying Receipt Dribbling Shooting Subcluster Adjusted Comparison">

Figure 22: Spain Center Midfields Attacking Carrying Receipt Dribbling Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 23: Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_Liga_F.png" alt="Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison">

Figure 24: Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_raw_Serie_A_Women.png" alt="Italy Center Midfields Attacking Passing Raw Comparison">

Figure 25: Italy Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_Serie_A_Women.png" alt="Italy Center Midfields Attacking Passing Subcluster Adjusted Comparison">

Figure 26: Italy Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_Serie_A_Women.png" alt="Italy Center Midfields Attacking Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 27: Italy Center Midfields Attacking Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_Serie_A_Women.png" alt="Italy Center Midfields Attacking Carrying Receipt Dribbling Shooting Subcluster Adjusted Comparison">

Figure 28: Italy Center Midfields Attacking Carrying Receipt Dribbling Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 29: Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_Serie_A_Women.png" alt="Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison">

Figure 30: Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-players"></a>

### **Radar plots for players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-players-aitana-bonmati-barcelona"></a>

#### **Aitana Bonmati - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="aitana-bonmati-barcelona-center-midfield-3-cluster-plots"></a>

##### **Center Midfield — 3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/passing_raw.png" alt="Aitana Bonmati Passing — Raw Statistics Comparison (Center Midfield)">

Figure 31: Aitana Bonmati — Passing — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/passing_raw_league_relative.png" alt="Aitana Bonmati Passing — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 32: Aitana Bonmati — Passing — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/passing_adj.png" alt="Aitana Bonmati Passing — Adjusted Statistics Comparison (Center Midfield)">

Figure 33: Aitana Bonmati — Passing — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/passing_adj_league_relative.png" alt="Aitana Bonmati Passing — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 34: Aitana Bonmati — Passing — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_raw.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Center Midfield)">

Figure 35: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 36: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_adj.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison (Center Midfield)">

Figure 37: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_adj_league_relative.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 38: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Aitana Bonmati Defending & Vulnerability — Raw Statistics Comparison (Center Midfield)">

Figure 39: Aitana Bonmati — Defending & Vulnerability — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Aitana Bonmati Defending & Vulnerability — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 40: Aitana Bonmati — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Aitana Bonmati Defending & Vulnerability — Adjusted Statistics Comparison (Center Midfield)">

Figure 41: Aitana Bonmati — Defending & Vulnerability — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Aitana Bonmati Defending & Vulnerability — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 42: Aitana Bonmati — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<a id="aitana-bonmati-barcelona-attacking-sub-position-2-cluster-plots"></a>

##### **Attacking sub-position — 2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/passing_raw.png" alt="Aitana Bonmati Passing — Raw Statistics Comparison (Attacking sub-position)">

Figure 43: Aitana Bonmati — Passing — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/passing_raw_league_relative.png" alt="Aitana Bonmati Passing — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 44: Aitana Bonmati — Passing — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/passing_subcluster_adj.png" alt="Aitana Bonmati Passing — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 45: Aitana Bonmati — Passing — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/passing_subcluster_adj_league_relative.png" alt="Aitana Bonmati Passing — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 46: Aitana Bonmati — Passing — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_raw.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Attacking sub-position)">

Figure 47: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 48: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_subcluster_adj.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 49: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/carrying_receipt_dribbling_shooting_subcluster_adj_league_relative.png" alt="Aitana Bonmati Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 50: Aitana Bonmati — Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Aitana Bonmati Defending & Vulnerability — Raw Statistics Comparison (Attacking sub-position)">

Figure 51: Aitana Bonmati — Defending & Vulnerability — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Aitana Bonmati Defending & Vulnerability — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 52: Aitana Bonmati — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_subcluster_adj.png" alt="Aitana Bonmati Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 53: Aitana Bonmati — Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Aitana_Bonmati_Conca_Barcelona_WFC/defending_vulnerability_fifty_fifty_subcluster_adj_league_relative.png" alt="Aitana Bonmati Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 54: Aitana Bonmati — Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<a id="radar-plots-for-players-julia-grosso-juventus"></a>

#### **Julia Grosso - Juventus**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="julia-grosso-juventus-center-midfield-3-cluster-plots"></a>

##### **Center Midfield — 3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/passing_raw.png" alt="Julia Grosso Passing — Raw Statistics Comparison (Center Midfield)">

Figure 55: Julia Grosso — Passing — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/passing_raw_league_relative.png" alt="Julia Grosso Passing — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 56: Julia Grosso — Passing — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/passing_adj.png" alt="Julia Grosso Passing — Adjusted Statistics Comparison (Center Midfield)">

Figure 57: Julia Grosso — Passing — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/passing_adj_league_relative.png" alt="Julia Grosso Passing — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 58: Julia Grosso — Passing — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_raw.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Center Midfield)">

Figure 59: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 60: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_adj.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison (Center Midfield)">

Figure 61: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_adj_league_relative.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 62: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_raw.png" alt="Julia Grosso Defending & Vulnerability — Raw Statistics Comparison (Center Midfield)">

Figure 63: Julia Grosso — Defending & Vulnerability — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Julia Grosso Defending & Vulnerability — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 64: Julia Grosso — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_adj.png" alt="Julia Grosso Defending & Vulnerability — Adjusted Statistics Comparison (Center Midfield)">

Figure 65: Julia Grosso — Defending & Vulnerability — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Julia Grosso Defending & Vulnerability — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 66: Julia Grosso — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<a id="julia-grosso-juventus-attacking-sub-position-2-cluster-plots"></a>

##### **Attacking sub-position — 2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/passing_raw.png" alt="Julia Grosso Passing — Raw Statistics Comparison (Attacking sub-position)">

Figure 67: Julia Grosso — Passing — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/passing_raw_league_relative.png" alt="Julia Grosso Passing — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 68: Julia Grosso — Passing — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/passing_subcluster_adj.png" alt="Julia Grosso Passing — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 69: Julia Grosso — Passing — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/passing_subcluster_adj_league_relative.png" alt="Julia Grosso Passing — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 70: Julia Grosso — Passing — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_raw.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Attacking sub-position)">

Figure 71: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 72: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_subcluster_adj.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 73: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/carrying_receipt_dribbling_shooting_subcluster_adj_league_relative.png" alt="Julia Grosso Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 74: Julia Grosso — Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_raw.png" alt="Julia Grosso Defending & Vulnerability — Raw Statistics Comparison (Attacking sub-position)">

Figure 75: Julia Grosso — Defending & Vulnerability — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Julia Grosso Defending & Vulnerability — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 76: Julia Grosso — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_subcluster_adj.png" alt="Julia Grosso Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 77: Julia Grosso — Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Julia_Angela_Grosso_Juventus_W/defending_vulnerability_fifty_fifty_subcluster_adj_league_relative.png" alt="Julia Grosso Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 78: Julia Grosso — Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<a id="radar-plots-for-players-jill-roord-manchester-city"></a>

#### **Jill Roord - Manchester City**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="jill-roord-manchester-city-center-midfield-3-cluster-plots"></a>

##### **Center Midfield — 3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/passing_raw.png" alt="Jill Roord Passing — Raw Statistics Comparison (Center Midfield)">

Figure 79: Jill Roord — Passing — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/passing_raw_league_relative.png" alt="Jill Roord Passing — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 80: Jill Roord — Passing — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/passing_adj.png" alt="Jill Roord Passing — Adjusted Statistics Comparison (Center Midfield)">

Figure 81: Jill Roord — Passing — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/passing_adj_league_relative.png" alt="Jill Roord Passing — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 82: Jill Roord — Passing — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_raw.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Center Midfield)">

Figure 83: Jill Roord — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 84: Jill Roord — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_adj.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison (Center Midfield)">

Figure 85: Jill Roord — Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_adj_league_relative.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 86: Jill Roord — Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Jill Roord Defending & Vulnerability — Raw Statistics Comparison (Center Midfield)">

Figure 87: Jill Roord — Defending & Vulnerability — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Jill Roord Defending & Vulnerability — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 88: Jill Roord — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Jill Roord Defending & Vulnerability — Adjusted Statistics Comparison (Center Midfield)">

Figure 89: Jill Roord — Defending & Vulnerability — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Jill Roord Defending & Vulnerability — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 90: Jill Roord — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<a id="jill-roord-manchester-city-attacking-sub-position-2-cluster-plots"></a>

##### **Attacking sub-position — 2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/passing_raw.png" alt="Jill Roord Passing — Raw Statistics Comparison (Attacking sub-position)">

Figure 91: Jill Roord — Passing — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/passing_raw_league_relative.png" alt="Jill Roord Passing — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 92: Jill Roord — Passing — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/passing_subcluster_adj.png" alt="Jill Roord Passing — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 93: Jill Roord — Passing — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/passing_subcluster_adj_league_relative.png" alt="Jill Roord Passing — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 94: Jill Roord — Passing — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_raw.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Attacking sub-position)">

Figure 95: Jill Roord — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 96: Jill Roord — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_subcluster_adj.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 97: Jill Roord — Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/carrying_receipt_dribbling_shooting_subcluster_adj_league_relative.png" alt="Jill Roord Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 98: Jill Roord — Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Jill Roord Defending & Vulnerability — Raw Statistics Comparison (Attacking sub-position)">

Figure 99: Jill Roord — Defending & Vulnerability — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Jill Roord Defending & Vulnerability — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 100: Jill Roord — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_subcluster_adj.png" alt="Jill Roord Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 101: Jill Roord — Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Jill_Roord_Manchester_City_WFC/defending_vulnerability_fifty_fifty_subcluster_adj_league_relative.png" alt="Jill Roord Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 102: Jill Roord — Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<a id="radar-plots-for-players-svenja-huth-vfl-wolfsburg"></a>

#### **Svenja Huth - VfL Wolfsburg**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="svenja-huth-vfl-wolfsburg-center-midfield-3-cluster-plots"></a>

##### **Center Midfield — 3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/passing_raw.png" alt="Svenja Huth Passing — Raw Statistics Comparison (Center Midfield)">

Figure 103: Svenja Huth — Passing — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/passing_raw_league_relative.png" alt="Svenja Huth Passing — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 104: Svenja Huth — Passing — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/passing_adj.png" alt="Svenja Huth Passing — Adjusted Statistics Comparison (Center Midfield)">

Figure 105: Svenja Huth — Passing — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/passing_adj_league_relative.png" alt="Svenja Huth Passing — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 106: Svenja Huth — Passing — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_raw.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Center Midfield)">

Figure 107: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 108: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_adj.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison (Center Midfield)">

Figure 109: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_adj_league_relative.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 110: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Svenja Huth Defending & Vulnerability — Raw Statistics Comparison (Center Midfield)">

Figure 111: Svenja Huth — Defending & Vulnerability — Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Svenja Huth Defending & Vulnerability — League-Aware Raw Statistics Comparison (Center Midfield)">

Figure 112: Svenja Huth — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Svenja Huth Defending & Vulnerability — Adjusted Statistics Comparison (Center Midfield)">

Figure 113: Svenja Huth — Defending & Vulnerability — Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Svenja Huth Defending & Vulnerability — League-Aware Adjusted Statistics Comparison (Center Midfield)">

Figure 114: Svenja Huth — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, Center Midfield, 3 Clusters

</div>

<a id="svenja-huth-vfl-wolfsburg-attacking-sub-position-2-cluster-plots"></a>

##### **Attacking sub-position — 2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/passing_raw.png" alt="Svenja Huth Passing — Raw Statistics Comparison (Attacking sub-position)">

Figure 115: Svenja Huth — Passing — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/passing_raw_league_relative.png" alt="Svenja Huth Passing — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 116: Svenja Huth — Passing — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/passing_subcluster_adj.png" alt="Svenja Huth Passing — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 117: Svenja Huth — Passing — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/passing_subcluster_adj_league_relative.png" alt="Svenja Huth Passing — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 118: Svenja Huth — Passing — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_raw.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison (Attacking sub-position)">

Figure 119: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_raw_league_relative.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 120: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_subcluster_adj.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 121: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/carrying_receipt_dribbling_shooting_subcluster_adj_league_relative.png" alt="Svenja Huth Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 122: Svenja Huth — Carrying, Receipt, Dribbling & Shooting — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Svenja Huth Defending & Vulnerability — Raw Statistics Comparison (Attacking sub-position)">

Figure 123: Svenja Huth — Defending & Vulnerability — Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Svenja Huth Defending & Vulnerability — League-Aware Raw Statistics Comparison (Attacking sub-position)">

Figure 124: Svenja Huth — Defending & Vulnerability — League-Aware Raw Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_subcluster_adj.png" alt="Svenja Huth Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 125: Svenja Huth — Defending & Vulnerability — Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield%20Attacking/k2/Svenja_Huth_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_subcluster_adj_league_relative.png" alt="Svenja Huth Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison (Attacking sub-position)">

Figure 126: Svenja Huth — Defending & Vulnerability — League-Aware Subcluster-Adjusted Statistics Comparison, Attacking sub-position, 2 Clusters

</div>