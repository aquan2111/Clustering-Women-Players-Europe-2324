# **Center Midfields**

<a id="table-of-contents"></a>

## **Table of Contents**

- <a href="#player-counts" style="color:black">Player counts</a>
- <a href="#results" style="color:black">Results</a>
  - <a href="#results-for-2-clusters" style="color:black">Results for 2 clusters</a>
    - <a href="#results-for-2-clusters-breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
      - <a href="#breakdown-of-results-by-league-breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
      - <a href="#breakdown-of-results-by-players" style="color:black">Breakdown of results by players</a>
  - <a href="#results-for-3-clusters" style="color:black">Results for 3 clusters</a>
    - <a href="#results-for-3-clusters-breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
    - <a href="#comparing-results-for-2-clusters-against-3-clusters" style="color:black">Comparing results for 2 clusters against 3 clusters</a>
      - <a href="#comparing-results-for-2-clusters-against-3-clusters-breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-center-midfields-averages" style="color:black">Radar plots for 2 clusters center midfields' averages</a>
    - <a href="#radar-plots-for-2-clusters-center-midfields-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-2-clusters-center-midfields-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-2-clusters-center-midfields-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-2-clusters-center-midfields-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-3-clusters-center-midfields-averages" style="color:black">Radar plots for 3 clusters center midfields' averages</a>
    - <a href="#radar-plots-for-3-clusters-center-midfields-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-3-clusters-center-midfields-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-3-clusters-center-midfields-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-3-clusters-center-midfields-averages-serie-a-women" style="color:black">Serie A Women</a>

<a id="player-counts"></a>

## **Player counts**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

In this project, there are a total of 182 center midfields considered, with

* 46 center midfields in 12 teams in the English FA Women's Super League
* 43 center midfields in 12 teams in the German Frauen Bundesliga
* 57 center midfields in 16 teams in the Spanish Liga F
* 36 center midfields in 10 teams in the Italian Serie A Women

<a id="results"></a>

## **Results**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-2-clusters"></a>

### **Results for 2 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-2-clusters-breakdown-of-results-by-league"></a>

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
      <td>23</td>
      <td>25</td>
      <td>32</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>18</td>
      <td>25</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>

The split is rather more biased towards cluster 0, execpt for England Women's Super League where the split is equal.

<a id="breakdown-of-results-by-league-breakdown-of-results-by-features"></a>

##### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 shows more positiveness towards forward pass percentage, pass lengths, average shot distance, fouls won while defending, and pass more than carry when it comes to progression.
* On the other hand, positiveness in cluster 1 can be seen in positional metrics higher up the pitch, as they carry more than pass as a method of progression, while attempting more through balls and passes into the box.

Therefore, based on these results,

* Cluster 0 center midfielders can be seen as deep midfielders
* Cluster 1 center midfielders can be seen as advanced midfielders

<a id="breakdown-of-results-by-players"></a>

##### **Breakdown of results by players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-3-clusters"></a>

### **Results for 3 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-3-clusters-breakdown-of-results-by-league"></a>

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
      <th>kmeans_3_cluster</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14</td>
      <td>7</td>
      <td>15</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11</td>
      <td>17</td>
      <td>16</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21</td>
      <td>19</td>
      <td>26</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>

<a id="comparing-results-for-2-clusters-against-3-clusters"></a>

#### **Comparing results for 2 clusters against 3 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">
<table border="1">
  <thead>
    <tr>
      <th>kmeans_3_cluster</th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
    <tr>
      <th>kmeans_2_cluster</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>18</td>
      <td>83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>43</td>
      <td>38</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

It seems like k = 3 cluster 1 is a shared zone between the two k = 2 clusters. Interestingly, no players from k = 2 cluster 0 landed in k = 3 cluster 0, while no players from k = 2 cluster 1 landed in k = 3 cluster 2.

<a id="comparing-results-for-2-clusters-against-3-clusters-breakdown-of-results-by-features"></a>

##### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 midfielders passed more backward and shorter, while attempted more through balls in passes into opposition box. They carried forward more, and were active at higher areas up the pitch, including receiving and applying pressures and winning the ball.
* While for cluster 1, these midfielders attempted more passes forward and low and progressive into the final third, while receiving locations vary more. Passing is their main progression method.
* Cluster 2 midfielders, on the other hand, made longer passes and further shots, and were active at lower zones, especially shown in blocks in own box.

Hence, the following conclusions can be made:

* Similar to k = 2 cluster 0, k = 3 cluster 2 center midfields can be seen as deep pivot midfielders
* Similar to k = 2 cluster 1, k = 3 cluster 0 center midfields can be seen as advanced carrying midfielders
* Cluster 1 can be seen as progressive passing midfielders.

Further clustering of each type of midfielders (Defensive/Center/Attacking) will be done based on the results of k = 3 clusters.

<a id="appendix"></a>

## **Appendix**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-midfields-averages"></a>

### **Radar plots for 2 clusters center midfields' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_raw.png" alt="Center Midfields Passing Raw Comparison">

Figure 1: Center Midfields Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_adj.png" alt="Center Midfields Passing Adjusted Comparison">

Figure 2: Center Midfields Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_raw.png" alt="Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 3: Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_adj.png" alt="Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 4: Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_raw.png" alt="Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 5: Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_adj.png" alt="Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 6: Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-midfields-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_raw_FA_Womens_Super_League.png" alt="England Center Midfields Passing Raw Comparison">

Figure 7: England Center Midfields Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_adj_FA_Womens_Super_League.png" alt="England Center Midfields Passing Adjusted Comparison">

Figure 8: England Center Midfields Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_raw_FA_Womens_Super_League.png" alt="England Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 9: England Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_adj_FA_Womens_Super_League.png" alt="England Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 10: England Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 11: England Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 12: England Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-midfields-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Passing Raw Comparison">

Figure 13: Germany Center Midfields Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Passing Adjusted Comparison">

Figure 14: Germany Center Midfields Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 15: Germany Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 16: Germany Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 17: Germany Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 18: Germany Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-midfields-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_raw_Liga_F.png" alt="Spain Center Midfields Passing Raw Comparison">

Figure 19: Spain Center Midfields Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_adj_Liga_F.png" alt="Spain Center Midfields Passing Adjusted Comparison">

Figure 20: Spain Center Midfields Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_raw_Liga_F.png" alt="Spain Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 21: Spain Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_adj_Liga_F.png" alt="Spain Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 22: Spain Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 23: Spain Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 24: Spain Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-midfields-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_raw_Serie_A_Women.png" alt="Italy Center Midfields Passing Raw Comparison">

Figure 25: Italy Center Midfields Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/passing_adj_Serie_A_Women.png" alt="Italy Center Midfields Passing Adjusted Comparison">

Figure 26: Italy Center Midfields Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_raw_Serie_A_Women.png" alt="Italy Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 27: Italy Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/carrying_receipt_dribbling_shooting_adj_Serie_A_Women.png" alt="Italy Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 28: Italy Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 29: Italy Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k2/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 30: Italy Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-midfields-averages"></a>

### **Radar plots for 3 clusters center midfields' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_raw.png" alt="Center Midfields Passing Raw Comparison">

Figure 31: Center Midfields Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_adj.png" alt="Center Midfields Passing Adjusted Comparison">

Figure 32: Center Midfields Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_raw.png" alt="Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 33: Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_adj.png" alt="Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 34: Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_raw.png" alt="Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 35: Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_adj.png" alt="Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 36: Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-midfields-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_raw_FA_Womens_Super_League.png" alt="England Center Midfields Passing Raw Comparison">

Figure 37: England Center Midfields Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_adj_FA_Womens_Super_League.png" alt="England Center Midfields Passing Adjusted Comparison">

Figure 38: England Center Midfields Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_raw_FA_Womens_Super_League.png" alt="England Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 39: England Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_adj_FA_Womens_Super_League.png" alt="England Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 40: England Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 41: England Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 42: England Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-midfields-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Passing Raw Comparison">

Figure 43: Germany Center Midfields Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Passing Adjusted Comparison">

Figure 44: Germany Center Midfields Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 45: Germany Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 46: Germany Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 47: Germany Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 48: Germany Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-midfields-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_raw_Liga_F.png" alt="Spain Center Midfields Passing Raw Comparison">

Figure 49: Spain Center Midfields Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_adj_Liga_F.png" alt="Spain Center Midfields Passing Adjusted Comparison">

Figure 50: Spain Center Midfields Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_raw_Liga_F.png" alt="Spain Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 51: Spain Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_adj_Liga_F.png" alt="Spain Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 52: Spain Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 53: Spain Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 54: Spain Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-midfields-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_raw_Serie_A_Women.png" alt="Italy Center Midfields Passing Raw Comparison">

Figure 55: Italy Center Midfields Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/passing_adj_Serie_A_Women.png" alt="Italy Center Midfields Passing Adjusted Comparison">

Figure 56: Italy Center Midfields Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_raw_Serie_A_Women.png" alt="Italy Center Midfields Carrying Receipt Dribbling Shooting Raw Comparison">

Figure 57: Italy Center Midfields Carrying Receipt Dribbling Shooting — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/carrying_receipt_dribbling_shooting_adj_Serie_A_Women.png" alt="Italy Center Midfields Carrying Receipt Dribbling Shooting Adjusted Comparison">

Figure 58: Italy Center Midfields Carrying Receipt Dribbling Shooting — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Midfields Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 59: Italy Center Midfields Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Midfield/k3/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Center Midfields Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 60: Italy Center Midfields Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>