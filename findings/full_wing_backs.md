# **Full/Wing Backs**

<a id="table-of-contents"></a>

## **Table of Contents**

- <a href="#player-counts" style="color:black">Player counts</a>
- <a href="#results" style="color:black">Results</a>
  - <a href="#results-for-2-clusters" style="color:black">Results for 2 clusters</a>
    - <a href="#results-for-2-clusters-breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
      - <a href="#breakdown-of-results-by-league-breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
  - <a href="#results-for-3-clusters" style="color:black">Results for 3 clusters</a>
    - <a href="#results-for-3-clusters-breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
    - <a href="#comparing-results-for-2-clusters-against-3-clusters" style="color:black">Comparing results for 2 clusters against 3 clusters</a>
    - <a href="#results-for-3-clusters-breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
  - <a href="#breakdown-of-results-by-players" style="color:black">Breakdown of results by players</a>
    - <a href="#breakdown-of-results-by-players-ona-batlle-barcelona" style="color:black">Ona Batlle - Barcelona</a>
    - <a href="#breakdown-of-results-by-players-eve-perisset-chelsea" style="color:black">Eve Perisset - Chelsea</a>
    - <a href="#breakdown-of-results-by-players-frederike-kempe-rb-leipzig" style="color:black">Frederike Kempe - RB Leipzig</a>
    - <a href="#breakdown-of-results-by-players-jayde-riviere-manchester-united" style="color:black">Jayde Riviere - Manchester United</a>
    - <a href="#breakdown-of-results-by-players-sofie-svava-real-madrid" style="color:black">Sofie Svava - Real Madrid</a>
    - <a href="#breakdown-of-results-by-players-lucy-bronze-barcelona" style="color:black">Lucy Bronze - Barcelona</a>
    - <a href="#breakdown-of-results-by-players-katie-mccabe-arsenal" style="color:black">Katie McCabe - Arsenal</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-full-wing-backs-averages" style="color:black">Radar plots for 2 clusters full/wing backs' averages</a>
    - <a href="#radar-plots-for-2-clusters-full-wing-backs-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-2-clusters-full-wing-backs-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-2-clusters-full-wing-backs-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-2-clusters-full-wing-backs-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-3-clusters-full-wing-backs-averages" style="color:black">Radar plots for 3 clusters full/wing backs' averages</a>
    - <a href="#radar-plots-for-3-clusters-full-wing-backs-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-3-clusters-full-wing-backs-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-3-clusters-full-wing-backs-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-3-clusters-full-wing-backs-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-players" style="color:black">Radar plots for players</a>
    - <a href="#radar-plots-for-players-ona-batlle-barcelona" style="color:black">Ona Batlle - Barcelona</a>
      - <a href="#ona-batlle-barcelona-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#ona-batlle-barcelona-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-eve-perisset-chelsea" style="color:black">Eve Perisset - Chelsea</a>
      - <a href="#eve-perisset-chelsea-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#eve-perisset-chelsea-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-frederike-kempe-rb-leipzig" style="color:black">Frederike Kempe - RB Leipzig</a>
      - <a href="#frederike-kempe-rb-leipzig-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#frederike-kempe-rb-leipzig-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-jayde-riviere-manchester-united" style="color:black">Jayde Riviere - Manchester United</a>
      - <a href="#jayde-riviere-manchester-united-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#jayde-riviere-manchester-united-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-sofie-svava-real-madrid" style="color:black">Sofie Svava - Real Madrid</a>
      - <a href="#sofie-svava-real-madrid-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#sofie-svava-real-madrid-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-lucy-bronze-barcelona" style="color:black">Lucy Bronze - Barcelona</a>
      - <a href="#lucy-bronze-barcelona-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#lucy-bronze-barcelona-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-katie-mccabe-arsenal" style="color:black">Katie McCabe - Arsenal</a>
      - <a href="#katie-mccabe-arsenal-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#katie-mccabe-arsenal-3-cluster-plots" style="color:black">3 cluster plots</a>


<a id="player-counts"></a>

## **Player counts**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

In this project, there are a total of 129 full/wing backs considered, with

* 14 full/wing backs in 12 teams in the English FA Women's Super League
* 17 full/wing backs in 12 teams in the German Frauen Bundesliga
* 29 full/wing backs in 16 teams in the Spanish Liga F
* 16 full/wing backs in 10 teams in the Italian Serie A Women

<a id="results"></a>

## **Results**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-2-clusters"></a>

### **Results for 2 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-2-clusters-breakdown-of-results-by-league"></a>

#### **Breakdown of results by league**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div>
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
      <td>15</td>
      <td>12</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15</td>
      <td>16</td>
      <td>24</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>

Eventually the split between two clusters seems pretty equal, though a bit more biased towards cluster 1 for Frauen Bundesliga and Liga F.

<a id="breakdown-of-results-by-league-breakdown-of-results-by-features"></a>

##### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 players tend to receive and take defensive actions in higher areas, especially when it comes to defending where there are more variations on where those actions happened, while also counterpress more in opposition half . They progress more by carrying than passing, and attempt more crosses and passes into the opposition box.
* On the other hand, cluster 1 players tend to pass more forward and longer while receiving and defending from lower areas, especially when it comes to blocking inside own box.

Therefore, based on these results,

* Cluster 0 players can be seen as advanced carrying wingbacks
* Cluster 1 players can be seen as traditional while forward passing fullbacks

<a id="results-for-3-clusters"></a>

### **Results for 3 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-3-clusters-breakdown-of-results-by-league"></a>

#### **Breakdown of results by league**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div>
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
      <td>10</td>
      <td>8</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11</td>
      <td>10</td>
      <td>15</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>13</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>

<a id="comparing-results-for-2-clusters-against-3-clusters"></a>

#### **Comparing results for 2 clusters against 3 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div>
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
      <td>41</td>
      <td>0</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>46</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>

It seems like k = 3 cluster 2 is a shared middle zone between the two k = 2 clusters.

<a id="results-for-3-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 shows more positiveness towards backward and ground pass percentage, progressive carrying into the final third being the main method of progression, and average carrying speed. Progression is done more via carrying than passing. Defensive actions are also taken at higher positions with greater variance, even in opposing half as shown in counterpress actions.
* While for cluster 1, these players perform defensive actions at much lower positions with much less variations in the locations, especially in blocking inside their own box.
* Cluster 2, on the other hand, shows more positiveness towards forward progressive passing metrics, including crosses and passes into box while receiving and dribbling from wider zones, and also forward carrying. Unlnike cluster 0, progression is done more via passing than carrying.

Hence, the following conclusions can be made:

* Cluster 0 can be seen as advanced carrying wingbacks
* Cluster 1 can be seen as traditional defending fullbacks
* Cluster 2 can be seen as progressive passing and chance creating wingbacks

<a id="breakdown-of-results-by-players"></a>

### **Breakdown of results by players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="breakdown-of-results-by-players-ona-batlle-barcelona"></a>

#### **Ona Batlle - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Batlle was safely clustered with advanced carrying wingbacks for both k = 2 and k = 3. She stood out for extremely high defensive actions and receipts up the pitch, especially for pressures and counterpress actions in opposing half. Her passing was mostly ground and backward recycling passes.

<a id="breakdown-of-results-by-players-eve-perisset-chelsea"></a>

#### **Eve Perisset - Chelsea**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Perisset was safely clustered with traditional fullbacks for both k = 2 and k = 3. Her receipts and most defensive actions were done at lower places down the pitch at less variance, while her passing was highly forward and progressive.

<a id="breakdown-of-results-by-players-frederike-kempe-rb-leipzig"></a>

#### **Frederike Kempe - RB Leipzig**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Kempe was safely clustered with fullbacks for k = 2 and then with progressive passing wingbacks for k = 3. Her passes were longer and more progressive into the final third, and she passed more than carried to progress. In contrast, her receipts and most defensive actions, which include pressures, blocks, and tackles, positions were lower, and she was less involved in counterpress actions.

<a id="breakdown-of-results-by-players-jayde-riviere-manchester-united"></a>

#### **Jayde Riviere - Manchester United**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Riviere was clustered into advanced carrying wingbacks for both k = 2 and k = 3, but only just in both cases, pretty much two-way and three-way ties in both scenarios. Her passing lengths were long, while her progressive and into the final third passing share were average and her forward carrying share was low. Her receipt positions were low, while her defensive actions locations varied by individual actions, although most of them were higher up the pitch.

<a id="breakdown-of-results-by-players-sofie-svava-real-madrid"></a>

#### **Sofie Svava - Real Madrid**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Svava was clustered into traditional fullbacks for both k = 2 and k = 3, but the margins stayed very close in both situations. She rarely made progressive into the final third passes, most passes were more on the ground, although she did attempted a significant number of crosses, switch passes, and passes into the box. Her receipt positions saw much higher than average variance.

<a id="breakdown-of-results-by-players-lucy-bronze-barcelona"></a>

#### **Lucy Bronze - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Bronze was clustered into fullbacks at k = 2, and then progressive passing wingbacks at k = 3. Her passing was slightly more average than other players of k = 3 cluster when it comes to progressive passes into the final third, while her pass lengths were shorter than average. Her dribble locations were wider than average of this cluster, while her receipt positions were slightly higher up the pitch. She was not as active in counterpress actions.

<a id="breakdown-of-results-by-players-katie-mccabe-arsenal"></a>

#### **Katie McCabe - Arsenal**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

McCabe was marginally clustered into k = 2 advanced carrying wingbacks, but then safely clustered into k = 3 progressive passing wingbacks. Her passes were dominantly longer and more progressive into the final third, and she also attempted more crosses, switch passes and passes into opposition box. Her receipt positions were quite high, while most of her defensive actions except blocks also happened higher, especially when it comes to counterpress actions.

<a id="appendix"></a>

## **Appendix**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-full-wing-backs-averages"></a>

### **Radar plots for 2 clusters full/wing backs' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_raw.png" alt="Full/Wing Backs Passing Raw Comparison">

Figure 1: Full/Wing Backs Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_adj.png" alt="Full/Wing Backs Passing Adjusted Comparison">

Figure 2: Full/Wing Backs Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_raw.png" alt="Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 3: Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_adj.png" alt="Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 4: Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_raw.png" alt="Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 5: Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_adj.png" alt="Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 6: Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-full-wing-backs-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_raw_FA_Womens_Super_League.png" alt="England Full/Wing Backs Passing Raw Comparison">

Figure 7: England Full/Wing Backs Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_adj_FA_Womens_Super_League.png" alt="England Full/Wing Backs Passing Adjusted Comparison">

Figure 8: England Full/Wing Backs Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_raw_FA_Womens_Super_League.png" alt="England Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 9: England Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_adj_FA_Womens_Super_League.png" alt="England Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 10: England Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 11: England Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 12: England Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-full-wing-backs-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_raw_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Passing Raw Comparison">

Figure 13: Germany Full/Wing Backs Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_adj_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Passing Adjusted Comparison">

Figure 14: Germany Full/Wing Backs Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_raw_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 15: Germany Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_adj_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 16: Germany Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 17: Germany Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 18: Germany Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-full-wing-backs-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_raw_Liga_F.png" alt="Spain Full/Wing Backs Passing Raw Comparison">

Figure 19: Spain Full/Wing Backs Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_adj_Liga_F.png" alt="Spain Full/Wing Backs Passing Adjusted Comparison">

Figure 20: Spain Full/Wing Backs Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_raw_Liga_F.png" alt="Spain Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 21: Spain Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_adj_Liga_F.png" alt="Spain Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 22: Spain Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 23: Spain Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 24: Spain Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-full-wing-backs-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_raw_Serie_A_Women.png" alt="Italy Full/Wing Backs Passing Raw Comparison">

Figure 25: Italy Full/Wing Backs Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/passing_adj_Serie_A_Women.png" alt="Italy Full/Wing Backs Passing Adjusted Comparison">

Figure 26: Italy Full/Wing Backs Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_raw_Serie_A_Women.png" alt="Italy Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 27: Italy Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/carrying_receipt_adj_Serie_A_Women.png" alt="Italy Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 28: Italy Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 29: Italy Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 30: Italy Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-3-clusters-full-wing-backs-averages"></a>

### **Radar plots for 3 clusters full/wing backs' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_raw.png" alt="Full/Wing Backs Passing Raw Comparison">

Figure 31: Full/Wing Backs Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_adj.png" alt="Full/Wing Backs Passing Adjusted Comparison">

Figure 32: Full/Wing Backs Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_raw.png" alt="Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 33: Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_adj.png" alt="Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 34: Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_raw.png" alt="Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 35: Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_adj.png" alt="Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 36: Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-full-wing-backs-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_raw_FA_Womens_Super_League.png" alt="England Full/Wing Backs Passing Raw Comparison">

Figure 37: England Full/Wing Backs Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_adj_FA_Womens_Super_League.png" alt="England Full/Wing Backs Passing Adjusted Comparison">

Figure 38: England Full/Wing Backs Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_raw_FA_Womens_Super_League.png" alt="England Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 39: England Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_adj_FA_Womens_Super_League.png" alt="England Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 40: England Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 41: England Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 42: England Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-full-wing-backs-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_raw_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Passing Raw Comparison">

Figure 43: Germany Full/Wing Backs Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_adj_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Passing Adjusted Comparison">

Figure 44: Germany Full/Wing Backs Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_raw_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 45: Germany Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_adj_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 46: Germany Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 47: Germany Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 48: Germany Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-full-wing-backs-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_raw_Liga_F.png" alt="Spain Full/Wing Backs Passing Raw Comparison">

Figure 49: Spain Full/Wing Backs Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_adj_Liga_F.png" alt="Spain Full/Wing Backs Passing Adjusted Comparison">

Figure 50: Spain Full/Wing Backs Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_raw_Liga_F.png" alt="Spain Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 51: Spain Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_adj_Liga_F.png" alt="Spain Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 52: Spain Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 53: Spain Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 54: Spain Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-full-wing-backs-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_raw_Serie_A_Women.png" alt="Italy Full/Wing Backs Passing Raw Comparison">

Figure 55: Italy Full/Wing Backs Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/passing_adj_Serie_A_Women.png" alt="Italy Full/Wing Backs Passing Adjusted Comparison">

Figure 56: Italy Full/Wing Backs Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_raw_Serie_A_Women.png" alt="Italy Full/Wing Backs Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 57: Italy Full/Wing Backs Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/carrying_receipt_adj_Serie_A_Women.png" alt="Italy Full/Wing Backs Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 58: Italy Full/Wing Backs Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Full/Wing Backs Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 59: Italy Full/Wing Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Full/Wing Backs Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 60: Italy Full/Wing Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players"></a>

### **Radar plots for players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-players-ona-batlle-barcelona"></a>

#### **Ona Batlle - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="ona-batlle-barcelona-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/passing_raw.png" alt="Ona Batlle Passing — Raw Statistics Comparison">

Figure 61: Ona Batlle — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/passing_raw_league_relative.png" alt="Ona Batlle Passing — League-Aware Raw Statistics Comparison">

Figure 62: Ona Batlle — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/passing_adj.png" alt="Ona Batlle Passing — Adjusted Statistics Comparison">

Figure 63: Ona Batlle — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/passing_adj_league_relative.png" alt="Ona Batlle Passing — League-Aware Adjusted Statistics Comparison">

Figure 64: Ona Batlle — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_raw.png" alt="Ona Batlle Carrying & Receipt — Raw Statistics Comparison">

Figure 65: Ona Batlle — Carrying & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_raw_league_relative.png" alt="Ona Batlle Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 66: Ona Batlle — Carrying & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_adj.png" alt="Ona Batlle Carrying & Receipt — Adjusted Statistics Comparison">

Figure 67: Ona Batlle — Carrying & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_adj_league_relative.png" alt="Ona Batlle Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 68: Ona Batlle — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Ona Batlle Defending & Vulnerability — Raw Statistics Comparison">

Figure 69: Ona Batlle — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Ona Batlle Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 70: Ona Batlle — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Ona Batlle Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 71: Ona Batlle — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Ona Batlle Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 72: Ona Batlle — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="ona-batlle-barcelona-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/passing_raw.png" alt="Ona Batlle Passing — Raw Statistics Comparison">

Figure 73: Ona Batlle — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/passing_raw_league_relative.png" alt="Ona Batlle Passing — League-Aware Raw Statistics Comparison">

Figure 74: Ona Batlle — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/passing_adj.png" alt="Ona Batlle Passing — Adjusted Statistics Comparison">

Figure 75: Ona Batlle — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/passing_adj_league_relative.png" alt="Ona Batlle Passing — League-Aware Adjusted Statistics Comparison">

Figure 76: Ona Batlle — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_raw.png" alt="Ona Batlle Carrying & Receipt — Raw Statistics Comparison">

Figure 77: Ona Batlle — Carrying & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_raw_league_relative.png" alt="Ona Batlle Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 78: Ona Batlle — Carrying & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_adj.png" alt="Ona Batlle Carrying & Receipt — Adjusted Statistics Comparison">

Figure 79: Ona Batlle — Carrying & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/carrying_receipt_adj_league_relative.png" alt="Ona Batlle Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 80: Ona Batlle — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Ona Batlle Defending & Vulnerability — Raw Statistics Comparison">

Figure 81: Ona Batlle — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Ona Batlle Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 82: Ona Batlle — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Ona Batlle Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 83: Ona Batlle — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Ona_Batlle_Pascual_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Ona Batlle Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 84: Ona Batlle — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-eve-perisset-chelsea"></a>

#### **Eve Perisset - Chelsea**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="eve-perisset-chelsea-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/passing_raw.png" alt="Eve Perisset Passing — Raw Statistics Comparison">

Figure 85: Eve Perisset — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/passing_raw_league_relative.png" alt="Eve Perisset Passing — League-Aware Raw Statistics Comparison">

Figure 86: Eve Perisset — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/passing_adj.png" alt="Eve Perisset Passing — Adjusted Statistics Comparison">

Figure 87: Eve Perisset — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/passing_adj_league_relative.png" alt="Eve Perisset Passing — League-Aware Adjusted Statistics Comparison">

Figure 88: Eve Perisset — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/carrying_receipt_raw.png" alt="Eve Perisset Carrying & Receipt — Raw Statistics Comparison">

Figure 89: Eve Perisset — Carrying & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/carrying_receipt_raw_league_relative.png" alt="Eve Perisset Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 90: Eve Perisset — Carrying & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/carrying_receipt_adj.png" alt="Eve Perisset Carrying & Receipt — Adjusted Statistics Comparison">

Figure 91: Eve Perisset — Carrying & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/carrying_receipt_adj_league_relative.png" alt="Eve Perisset Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 92: Eve Perisset — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw.png" alt="Eve Perisset Defending & Vulnerability — Raw Statistics Comparison">

Figure 93: Eve Perisset — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Eve Perisset Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 94: Eve Perisset — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj.png" alt="Eve Perisset Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 95: Eve Perisset — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Eve Perisset Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 96: Eve Perisset — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="eve-perisset-chelsea-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/passing_raw.png" alt="Eve Perisset Passing — Raw Statistics Comparison">

Figure 97: Eve Perisset — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/passing_raw_league_relative.png" alt="Eve Perisset Passing — League-Aware Raw Statistics Comparison">

Figure 98: Eve Perisset — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/passing_adj.png" alt="Eve Perisset Passing — Adjusted Statistics Comparison">

Figure 99: Eve Perisset — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/passing_adj_league_relative.png" alt="Eve Perisset Passing — League-Aware Adjusted Statistics Comparison">

Figure 100: Eve Perisset — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/carrying_receipt_raw.png" alt="Eve Perisset Carrying & Receipt — Raw Statistics Comparison">

Figure 101: Eve Perisset — Carrying & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/carrying_receipt_raw_league_relative.png" alt="Eve Perisset Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 102: Eve Perisset — Carrying & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/carrying_receipt_adj.png" alt="Eve Perisset Carrying & Receipt — Adjusted Statistics Comparison">

Figure 103: Eve Perisset — Carrying & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/carrying_receipt_adj_league_relative.png" alt="Eve Perisset Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 104: Eve Perisset — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw.png" alt="Eve Perisset Defending & Vulnerability — Raw Statistics Comparison">

Figure 105: Eve Perisset — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Eve Perisset Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 106: Eve Perisset — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj.png" alt="Eve Perisset Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 107: Eve Perisset — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Eve_Perisset_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Eve Perisset Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 108: Eve Perisset — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-frederike-kempe-rb-leipzig"></a>

#### **Frederike Kempe - RB Leipzig**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="frederike-kempe-rb-leipzig-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/passing_raw.png" alt="Frederike Kempe Passing — Raw Statistics Comparison">

Figure 109: Frederike Kempe — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/passing_raw_league_relative.png" alt="Frederike Kempe Passing — League-Aware Raw Statistics Comparison">

Figure 110: Frederike Kempe — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/passing_adj.png" alt="Frederike Kempe Passing — Adjusted Statistics Comparison">

Figure 111: Frederike Kempe — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/passing_adj_league_relative.png" alt="Frederike Kempe Passing — League-Aware Adjusted Statistics Comparison">

Figure 112: Frederike Kempe — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_raw.png" alt="Frederike Kempe Carrying & Receipt — Raw Statistics Comparison">

Figure 113: Frederike Kempe — Carrying & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_raw_league_relative.png" alt="Frederike Kempe Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 114: Frederike Kempe — Carrying & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_adj.png" alt="Frederike Kempe Carrying & Receipt — Adjusted Statistics Comparison">

Figure 115: Frederike Kempe — Carrying & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_adj_league_relative.png" alt="Frederike Kempe Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 116: Frederike Kempe — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_raw.png" alt="Frederike Kempe Defending & Vulnerability — Raw Statistics Comparison">

Figure 117: Frederike Kempe — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Frederike Kempe Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 118: Frederike Kempe — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_adj.png" alt="Frederike Kempe Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 119: Frederike Kempe — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Frederike Kempe Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 120: Frederike Kempe — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="frederike-kempe-rb-leipzig-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/passing_raw.png" alt="Frederike Kempe Passing — Raw Statistics Comparison">

Figure 121: Frederike Kempe — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/passing_raw_league_relative.png" alt="Frederike Kempe Passing — League-Aware Raw Statistics Comparison">

Figure 122: Frederike Kempe — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/passing_adj.png" alt="Frederike Kempe Passing — Adjusted Statistics Comparison">

Figure 123: Frederike Kempe — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/passing_adj_league_relative.png" alt="Frederike Kempe Passing — League-Aware Adjusted Statistics Comparison">

Figure 124: Frederike Kempe — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_raw.png" alt="Frederike Kempe Carrying & Receipt — Raw Statistics Comparison">

Figure 125: Frederike Kempe — Carrying & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_raw_league_relative.png" alt="Frederike Kempe Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 126: Frederike Kempe — Carrying & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_adj.png" alt="Frederike Kempe Carrying & Receipt — Adjusted Statistics Comparison">

Figure 127: Frederike Kempe — Carrying & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/carrying_receipt_adj_league_relative.png" alt="Frederike Kempe Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 128: Frederike Kempe — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_raw.png" alt="Frederike Kempe Defending & Vulnerability — Raw Statistics Comparison">

Figure 129: Frederike Kempe — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Frederike Kempe Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 130: Frederike Kempe — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_adj.png" alt="Frederike Kempe Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 131: Frederike Kempe — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Frederike_Kempe_RB_Leipzig_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Frederike Kempe Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 132: Frederike Kempe — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-jayde-riviere-manchester-united"></a>

#### **Jayde Riviere - Manchester United**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="jayde-riviere-manchester-united-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_raw.png" alt="Jayde Riviere Passing — Raw Statistics Comparison">

Figure 133: Jayde Riviere — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_raw_league_relative.png" alt="Jayde Riviere Passing — League-Aware Raw Statistics Comparison">

Figure 134: Jayde Riviere — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_adj.png" alt="Jayde Riviere Passing — Adjusted Statistics Comparison">

Figure 135: Jayde Riviere — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_adj_league_relative.png" alt="Jayde Riviere Passing — League-Aware Adjusted Statistics Comparison">

Figure 136: Jayde Riviere — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_raw.png" alt="Jayde Riviere Carrying & Receipt — Raw Statistics Comparison">

Figure 137: Jayde Riviere — Carrying & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_raw_league_relative.png" alt="Jayde Riviere Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 138: Jayde Riviere — Carrying & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_adj.png" alt="Jayde Riviere Carrying & Receipt — Adjusted Statistics Comparison">

Figure 139: Jayde Riviere — Carrying & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_adj_league_relative.png" alt="Jayde Riviere Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 140: Jayde Riviere — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_raw.png" alt="Jayde Riviere Defending & Vulnerability — Raw Statistics Comparison">

Figure 141: Jayde Riviere — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Jayde Riviere Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 142: Jayde Riviere — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_adj.png" alt="Jayde Riviere Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 143: Jayde Riviere — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Jayde Riviere Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 144: Jayde Riviere — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="jayde-riviere-manchester-united-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_raw.png" alt="Jayde Riviere Passing — Raw Statistics Comparison">

Figure 145: Jayde Riviere — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_raw_league_relative.png" alt="Jayde Riviere Passing — League-Aware Raw Statistics Comparison">

Figure 146: Jayde Riviere — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_adj.png" alt="Jayde Riviere Passing — Adjusted Statistics Comparison">

Figure 147: Jayde Riviere — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/passing_adj_league_relative.png" alt="Jayde Riviere Passing — League-Aware Adjusted Statistics Comparison">

Figure 148: Jayde Riviere — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_raw.png" alt="Jayde Riviere Carrying & Receipt — Raw Statistics Comparison">

Figure 149: Jayde Riviere — Carrying & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_raw_league_relative.png" alt="Jayde Riviere Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 150: Jayde Riviere — Carrying & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_adj.png" alt="Jayde Riviere Carrying & Receipt — Adjusted Statistics Comparison">

Figure 151: Jayde Riviere — Carrying & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/carrying_receipt_adj_league_relative.png" alt="Jayde Riviere Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 152: Jayde Riviere — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_raw.png" alt="Jayde Riviere Defending & Vulnerability — Raw Statistics Comparison">

Figure 153: Jayde Riviere — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Jayde Riviere Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 154: Jayde Riviere — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_adj.png" alt="Jayde Riviere Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 155: Jayde Riviere — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Jayde_Yuk_Fun_Riviere_Manchester_United_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Jayde Riviere Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 156: Jayde Riviere — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-sofie-svava-real-madrid"></a>

#### **Sofie Svava - Real Madrid**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="sofie-svava-real-madrid-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/passing_raw.png" alt="Sofie Svava Passing — Raw Statistics Comparison">

Figure 157: Sofie Svava — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/passing_raw_league_relative.png" alt="Sofie Svava Passing — League-Aware Raw Statistics Comparison">

Figure 158: Sofie Svava — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/passing_adj.png" alt="Sofie Svava Passing — Adjusted Statistics Comparison">

Figure 159: Sofie Svava — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/passing_adj_league_relative.png" alt="Sofie Svava Passing — League-Aware Adjusted Statistics Comparison">

Figure 160: Sofie Svava — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_raw.png" alt="Sofie Svava Carrying & Receipt — Raw Statistics Comparison">

Figure 161: Sofie Svava — Carrying & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_raw_league_relative.png" alt="Sofie Svava Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 162: Sofie Svava — Carrying & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_adj.png" alt="Sofie Svava Carrying & Receipt — Adjusted Statistics Comparison">

Figure 163: Sofie Svava — Carrying & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_adj_league_relative.png" alt="Sofie Svava Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 164: Sofie Svava — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_raw.png" alt="Sofie Svava Defending & Vulnerability — Raw Statistics Comparison">

Figure 165: Sofie Svava — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Sofie Svava Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 166: Sofie Svava — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_adj.png" alt="Sofie Svava Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 167: Sofie Svava — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Sofie Svava Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 168: Sofie Svava — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="sofie-svava-real-madrid-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/passing_raw.png" alt="Sofie Svava Passing — Raw Statistics Comparison">

Figure 169: Sofie Svava — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/passing_raw_league_relative.png" alt="Sofie Svava Passing — League-Aware Raw Statistics Comparison">

Figure 170: Sofie Svava — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/passing_adj.png" alt="Sofie Svava Passing — Adjusted Statistics Comparison">

Figure 171: Sofie Svava — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/passing_adj_league_relative.png" alt="Sofie Svava Passing — League-Aware Adjusted Statistics Comparison">

Figure 172: Sofie Svava — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_raw.png" alt="Sofie Svava Carrying & Receipt — Raw Statistics Comparison">

Figure 173: Sofie Svava — Carrying & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_raw_league_relative.png" alt="Sofie Svava Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 174: Sofie Svava — Carrying & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_adj.png" alt="Sofie Svava Carrying & Receipt — Adjusted Statistics Comparison">

Figure 175: Sofie Svava — Carrying & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/carrying_receipt_adj_league_relative.png" alt="Sofie Svava Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 176: Sofie Svava — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_raw.png" alt="Sofie Svava Defending & Vulnerability — Raw Statistics Comparison">

Figure 177: Sofie Svava — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Sofie Svava Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 178: Sofie Svava — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_adj.png" alt="Sofie Svava Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 179: Sofie Svava — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Sofie_Svava_Real_Madrid_CF_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Sofie Svava Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 180: Sofie Svava — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-lucy-bronze-barcelona"></a>

#### **Lucy Bronze - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="lucy-bronze-barcelona-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/passing_raw.png" alt="Lucy Bronze Passing — Raw Statistics Comparison">

Figure 181: Lucy Bronze — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/passing_raw_league_relative.png" alt="Lucy Bronze Passing — League-Aware Raw Statistics Comparison">

Figure 182: Lucy Bronze — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/passing_adj.png" alt="Lucy Bronze Passing — Adjusted Statistics Comparison">

Figure 183: Lucy Bronze — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/passing_adj_league_relative.png" alt="Lucy Bronze Passing — League-Aware Adjusted Statistics Comparison">

Figure 184: Lucy Bronze — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/carrying_receipt_raw.png" alt="Lucy Bronze Carrying & Receipt — Raw Statistics Comparison">

Figure 185: Lucy Bronze — Carrying & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/carrying_receipt_raw_league_relative.png" alt="Lucy Bronze Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 186: Lucy Bronze — Carrying & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/carrying_receipt_adj.png" alt="Lucy Bronze Carrying & Receipt — Adjusted Statistics Comparison">

Figure 187: Lucy Bronze — Carrying & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/carrying_receipt_adj_league_relative.png" alt="Lucy Bronze Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 188: Lucy Bronze — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Lucy Bronze Defending & Vulnerability — Raw Statistics Comparison">

Figure 189: Lucy Bronze — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Lucy Bronze Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 190: Lucy Bronze — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Lucy Bronze Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 191: Lucy Bronze — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Lucy Bronze Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 192: Lucy Bronze — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="lucy-bronze-barcelona-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/passing_raw.png" alt="Lucy Bronze Passing — Raw Statistics Comparison">

Figure 193: Lucy Bronze — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/passing_raw_league_relative.png" alt="Lucy Bronze Passing — League-Aware Raw Statistics Comparison">

Figure 194: Lucy Bronze — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/passing_adj.png" alt="Lucy Bronze Passing — Adjusted Statistics Comparison">

Figure 195: Lucy Bronze — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/passing_adj_league_relative.png" alt="Lucy Bronze Passing — League-Aware Adjusted Statistics Comparison">

Figure 196: Lucy Bronze — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/carrying_receipt_raw.png" alt="Lucy Bronze Carrying & Receipt — Raw Statistics Comparison">

Figure 197: Lucy Bronze — Carrying & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/carrying_receipt_raw_league_relative.png" alt="Lucy Bronze Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 198: Lucy Bronze — Carrying & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/carrying_receipt_adj.png" alt="Lucy Bronze Carrying & Receipt — Adjusted Statistics Comparison">

Figure 199: Lucy Bronze — Carrying & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/carrying_receipt_adj_league_relative.png" alt="Lucy Bronze Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 200: Lucy Bronze — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Lucy Bronze Defending & Vulnerability — Raw Statistics Comparison">

Figure 201: Lucy Bronze — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Lucy Bronze Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 202: Lucy Bronze — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Lucy Bronze Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 203: Lucy Bronze — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Lucy_Bronze_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Lucy Bronze Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 204: Lucy Bronze — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-katie-mccabe-arsenal"></a>

#### **Katie McCabe - Arsenal**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="katie-mccabe-arsenal-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/passing_raw.png" alt="Katie McCabe Passing — Raw Statistics Comparison">

Figure 205: Katie McCabe — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/passing_raw_league_relative.png" alt="Katie McCabe Passing — League-Aware Raw Statistics Comparison">

Figure 206: Katie McCabe — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/passing_adj.png" alt="Katie McCabe Passing — Adjusted Statistics Comparison">

Figure 207: Katie McCabe — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/passing_adj_league_relative.png" alt="Katie McCabe Passing — League-Aware Adjusted Statistics Comparison">

Figure 208: Katie McCabe — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/carrying_receipt_raw.png" alt="Katie McCabe Carrying & Receipt — Raw Statistics Comparison">

Figure 209: Katie McCabe — Carrying & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/carrying_receipt_raw_league_relative.png" alt="Katie McCabe Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 210: Katie McCabe — Carrying & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/carrying_receipt_adj.png" alt="Katie McCabe Carrying & Receipt — Adjusted Statistics Comparison">

Figure 211: Katie McCabe — Carrying & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/carrying_receipt_adj_league_relative.png" alt="Katie McCabe Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 212: Katie McCabe — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Katie McCabe Defending & Vulnerability — Raw Statistics Comparison">

Figure 213: Katie McCabe — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Katie McCabe Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 214: Katie McCabe — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Katie McCabe Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 215: Katie McCabe — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k2/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Katie McCabe Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 216: Katie McCabe — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="katie-mccabe-arsenal-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/passing_raw.png" alt="Katie McCabe Passing — Raw Statistics Comparison">

Figure 217: Katie McCabe — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/passing_raw_league_relative.png" alt="Katie McCabe Passing — League-Aware Raw Statistics Comparison">

Figure 218: Katie McCabe — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/passing_adj.png" alt="Katie McCabe Passing — Adjusted Statistics Comparison">

Figure 219: Katie McCabe — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/passing_adj_league_relative.png" alt="Katie McCabe Passing — League-Aware Adjusted Statistics Comparison">

Figure 220: Katie McCabe — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/carrying_receipt_raw.png" alt="Katie McCabe Carrying & Receipt — Raw Statistics Comparison">

Figure 221: Katie McCabe — Carrying & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/carrying_receipt_raw_league_relative.png" alt="Katie McCabe Carrying & Receipt — League-Aware Raw Statistics Comparison">

Figure 222: Katie McCabe — Carrying & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/carrying_receipt_adj.png" alt="Katie McCabe Carrying & Receipt — Adjusted Statistics Comparison">

Figure 223: Katie McCabe — Carrying & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/carrying_receipt_adj_league_relative.png" alt="Katie McCabe Carrying & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 224: Katie McCabe — Carrying & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Katie McCabe Defending & Vulnerability — Raw Statistics Comparison">

Figure 225: Katie McCabe — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Katie McCabe Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 226: Katie McCabe — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Katie McCabe Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 227: Katie McCabe — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Full%20Wing%20Back/k3/Katie_McCabe_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Katie McCabe Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 228: Katie McCabe — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>