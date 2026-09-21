# **Wingers**

<a id="table-of-contents"></a>

## **Table of Contents**

- <a href="#player-counts" style="color:black">Player counts</a>
- <a href="#results" style="color:black">Results</a>
  - <a href="#results-for-2-clusters" style="color:black">Results for 2 clusters</a>
    - <a href="#results-for-2-clusters-breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
    - <a href="#results-for-2-clusters-breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
  - <a href="#results-for-3-clusters" style="color:black">Results for 3 clusters</a>
    - <a href="#results-for-3-clusters-breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
    - <a href="#comparing-results-for-2-clusters-against-3-clusters" style="color:black">Comparing results for 2 clusters against 3 clusters</a>
    - <a href="#results-for-3-clusters-breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
  - <a href="#breakdown-of-results-by-players" style="color:black">Breakdown of results by players</a>
    - <a href="#breakdown-of-results-by-players-caroline-graham-hansen-barcelona" style="color:black">Caroline Graham Hansen - Barcelona</a>
    - <a href="#breakdown-of-results-by-players-carlotta-wamser-koln" style="color:black">Carlotta Wamser - Koln</a>
    - <a href="#breakdown-of-results-by-players-grace-clinton-tottenham-hotspur" style="color:black">Grace Clinton - Tottenham Hotspur</a>
    - <a href="#breakdown-of-results-by-players-jule-brand-vfl-wolfsburg" style="color:black">Jule Brand - VfL Wolfsburg</a>
    - <a href="#breakdown-of-results-by-players-klara-buhl-bayern-munchen" style="color:black">Klara Buhl - Bayern Munchen</a>
    - <a href="#breakdown-of-results-by-players-nikita-parris-manchester-united" style="color:black">Nikita Parris - Manchester United</a>
    - <a href="#breakdown-of-results-by-players-beth-mead-arsenal" style="color:black">Beth Mead - Arsenal</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-wingers-averages" style="color:black">Radar plots for 2 clusters wingers' averages</a>
    - <a href="#radar-plots-for-2-clusters-wingers-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-2-clusters-wingers-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-2-clusters-wingers-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-2-clusters-wingers-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-3-clusters-wingers-averages" style="color:black">Radar plots for 3 clusters wingers' averages</a>
    - <a href="#radar-plots-for-3-clusters-wingers-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-3-clusters-wingers-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-3-clusters-wingers-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-3-clusters-wingers-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-players" style="color:black">Radar plots for players</a>
    - <a href="#radar-plots-for-players-caroline-graham-hansen-barcelona" style="color:black">Caroline Graham Hansen - Barcelona</a>
      - <a href="#caroline-graham-hansen-barcelona-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#caroline-graham-hansen-barcelona-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-carlotta-wamser-koln" style="color:black">Carlotta Wamser - Koln</a>
      - <a href="#carlotta-wamser-koln-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#carlotta-wamser-koln-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-grace-clinton-tottenham-hotspur" style="color:black">Grace Clinton - Tottenham Hotspur</a>
      - <a href="#grace-clinton-tottenham-hotspur-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#grace-clinton-tottenham-hotspur-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-jule-brand-vfl-wolfsburg" style="color:black">Jule Brand - VfL Wolfsburg</a>
      - <a href="#jule-brand-vfl-wolfsburg-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#jule-brand-vfl-wolfsburg-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-klara-buhl-bayern-munchen" style="color:black">Klara Buhl - Bayern Munchen</a>
      - <a href="#klara-buhl-bayern-munchen-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#klara-buhl-bayern-munchen-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-nikita-parris-manchester-united" style="color:black">Nikita Parris - Manchester United</a>
      - <a href="#nikita-parris-manchester-united-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#nikita-parris-manchester-united-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-beth-mead-arsenal" style="color:black">Beth Mead - Arsenal</a>
      - <a href="#beth-mead-arsenal-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#beth-mead-arsenal-3-cluster-plots" style="color:black">3 cluster plots</a>


<a id="player-counts"></a>

## **Player counts**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

In this project, there are a total of 85 wingers considered, with

* 22 wingers in 12 teams in the English FA Women's Super League
* 22 wingers in 12 teams in the German Frauen Bundesliga
* 26 wingers in 16 teams in the Spanish Liga F
* 15 wingers in 10 teams in the Italian Serie A Women

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
<table>
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
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>8</td>
      <td>11</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>

For all leagues, the split was roughly the same of 60:40 ratio between cluster 0 and cluster 1.

<a id="results-for-2-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 wingers show positive signature towards low passes progressive passes, switch passes, crosses, cutbacks, inside and into opposition box passes, forward carrying, and involving at higher and wider positions (including receiving, dribbling, pressuring, and turnovers), and counterpress actions in opposing half.
* On the other hand, cluster 1 wingers show positive signature in ground passes, change in passing length under pressure, backward carrying.

Therefore, based on these results,

* Cluster 0 wingers are more advanced wingers who involve much higher and are more creative.
* Cluster 1 wingers can be seen as wide midfielders.

<a id="results-for-3-clusters"></a>

### **Results for 3 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="results-for-3-clusters-breakdown-of-results-by-league"></a>

#### **Breakdown of results by league**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div>
<table>
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
      <td>11</td>
      <td>14</td>
      <td>13</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>4</td>
      <td>7</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>

Rougly 50% of players ended up in cluster 0 for all leagues, while the rest were quite evenly splitted between cluster 1 and cluster 2.

<a id="comparing-results-for-2-clusters-against-3-clusters"></a>

#### **Comparing results for 2 clusters against 3 clusters**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div>
<table>
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
      <td>45</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>18</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>

It seems like cluster 0 of k = 2 aligns to cluster 0 of k = 3, while cluster 1 of k = 2 equally splits out into k = 3 cluster 1 and 2.

<a id="results-for-3-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 wingers made more progressive passes, low passes, switch passes, crosses, cutbacks, passes into and inside opposition box, forward carries, and involve at higher and wider locations (receiving, dribbling, pressing, turnovers), especially with counterpress actions in opposing half.
* In contrast, cluster 1 wingers had higher backward passing percentage, ground passing percentage, average carry distance and progressive carries into final third. Carrying was their main method of progression.
* While for cluster 2 wingers, they stood out for forward passing percentage, especially into the final third, average pass length and change in passing length under pressure, deeper and more central receiving and dribbling locations. Passing was their main method of progression. Their average carry speed was the slowest among the three clusters.

Following all the information, the following conclusions can be made:

* Similar to cluster 0 of k = 2, cluster 0 of k = 3 can be seen as advanced wingers.
* Cluster 1 can be seen as wide conservative midfielders.
* Cluster 2 can be seen as wide playmakers.

<a id="breakdown-of-results-by-players"></a>

### **Breakdown of results by players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="breakdown-of-results-by-players-caroline-graham-hansen-barcelona"></a>

#### **Caroline Graham Hansen - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Graham Hansen was safely clustered into advanced wingers for both k = 2 and k = 3. This can be shown in her high share of progressive passes and crosses, low share of ground passes, and higher positional involvement both defensively and offensively up the pitch.

<a id="breakdown-of-results-by-players-carlotta-wamser-koln"></a>

#### **Carlotta Wamser - Koln**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Wamser was safely clustered into wide midfielders for both k = 2 and k = 3. Most of her passes were on the ground without being progressive, and she barely made any crosses. Most of her receipts were also lower down the pitch, and the same trend can be seen for her pressures applied and dispossessions.

<a id="breakdown-of-results-by-players-grace-clinton-tottenham-hotspur"></a>

#### **Grace Clinton - Tottenham Hotspur**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Clinton was clustered into wide midfielders for k = 2 and wide playmakers for k = 3. Her defensive and receiving positionings were very low, while she did not attempt many crosses. Her receipt locations were very central, but her passes were longer than average. Interestingly enough, she averaged higher carry distance.

<a id="breakdown-of-results-by-players-jule-brand-vfl-wolfsburg"></a>

#### **Jule Brand - VfL Wolfsburg**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Brand was clustered into advanced wingers for both k = 2 and k = 3, but only just. Her average carry distance and carry speed were very high, and such carries were mostly progressive. In contrast, her receiving and pressing positions were lower, and she did not cross much.

<a id="breakdown-of-results-by-players-klara-buhl-bayern-munchen"></a>

#### **Klara Buhl - Bayern Munchen**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Buhl was clustered into wide midfielders for both k= 2 and k = 3, but the similarities to other clusters were also very high. Her receipt, pressing, and turnover locations were rather low down the pitch, while her dribbling location was slightly higher. Her carries were more forward and faster, while her passes were longer but not too progressive. In contrast, many of the passes ended up in opposition box.

<a id="breakdown-of-results-by-players-nikita-parris-manchester-united"></a>

#### **Nikita Parris - Manchester United**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Parris was clustered into wide midfielders for k = 2, and then wide playmakers for k = 3, although the margins were very thin. In terms of her passing, she did not attempt many crosses or progressive passes or passes into opposition box, while her passes were mostly short. She received the ball higher but more central, while also dribbled high but wider. Her pressures were also at higher locations, while counterpress actions occured more frequently in opposing half.

<a id="breakdown-of-results-by-players-beth-mead-arsenal"></a>

#### **Beth Mead - Arsenal**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Mead was closely clustered with wingers for k = 2, but then more confidently clustered with wide playmakers for k = 3. This can be shown in her longer and more progressive passes into the box, while she did not attempt too many crosses. While she carried forward much, her carry speed and distance were not high. She received and dribbled at higher locations, while her pressure locations were not too high although she had quite high number of counterpress actions in opposing half.

<a id="appendix"></a>

## **Appendix**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-wingers-averages"></a>

### **Radar plots for 2 clusters wingers' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_raw.png" alt="Wingers Passing Raw Comparison">

Figure 1: Wingers Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_adj.png" alt="Wingers Passing Adjusted Comparison">

Figure 2: Wingers Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_raw.png" alt="Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 3: Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_adj.png" alt="Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 4: Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_raw.png" alt="Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 5: Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_adj.png" alt="Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 6: Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-wingers-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_raw_FA_Womens_Super_League.png" alt="England Wingers Passing Raw Comparison">

Figure 7: England Wingers Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_adj_FA_Womens_Super_League.png" alt="England Wingers Passing Adjusted Comparison">

Figure 8: England Wingers Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_raw_FA_Womens_Super_League.png" alt="England Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 9: England Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_adj_FA_Womens_Super_League.png" alt="England Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 10: England Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 11: England Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 12: England Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-wingers-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_raw_Frauen_Bundesliga.png" alt="Germany Wingers Passing Raw Comparison">

Figure 13: Germany Wingers Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_adj_Frauen_Bundesliga.png" alt="Germany Wingers Passing Adjusted Comparison">

Figure 14: Germany Wingers Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_raw_Frauen_Bundesliga.png" alt="Germany Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 15: Germany Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_adj_Frauen_Bundesliga.png" alt="Germany Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 16: Germany Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 17: Germany Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 18: Germany Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-wingers-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_raw_Liga_F.png" alt="Spain Wingers Passing Raw Comparison">

Figure 19: Spain Wingers Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_adj_Liga_F.png" alt="Spain Wingers Passing Adjusted Comparison">

Figure 20: Spain Wingers Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_raw_Liga_F.png" alt="Spain Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 21: Spain Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_adj_Liga_F.png" alt="Spain Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 22: Spain Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 23: Spain Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 24: Spain Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-wingers-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_raw_Serie_A_Women.png" alt="Italy Wingers Passing Raw Comparison">

Figure 25: Italy Wingers Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/passing_adj_Serie_A_Women.png" alt="Italy Wingers Passing Adjusted Comparison">

Figure 26: Italy Wingers Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_raw_Serie_A_Women.png" alt="Italy Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 27: Italy Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/carrying_dribbling_shooting_receipt_adj_Serie_A_Women.png" alt="Italy Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 28: Italy Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 29: Italy Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 30: Italy Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-3-clusters-wingers-averages"></a>

### **Radar plots for 3 clusters wingers' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_raw.png" alt="Wingers Passing Raw Comparison">

Figure 31: Wingers Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_adj.png" alt="Wingers Passing Adjusted Comparison">

Figure 32: Wingers Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_raw.png" alt="Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 33: Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_adj.png" alt="Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 34: Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_raw.png" alt="Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 35: Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_adj.png" alt="Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 36: Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-wingers-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_raw_FA_Womens_Super_League.png" alt="England Wingers Passing Raw Comparison">

Figure 37: England Wingers Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_adj_FA_Womens_Super_League.png" alt="England Wingers Passing Adjusted Comparison">

Figure 38: England Wingers Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_raw_FA_Womens_Super_League.png" alt="England Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 39: England Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_adj_FA_Womens_Super_League.png" alt="England Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 40: England Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 41: England Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 42: England Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-wingers-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_raw_Frauen_Bundesliga.png" alt="Germany Wingers Passing Raw Comparison">

Figure 43: Germany Wingers Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_adj_Frauen_Bundesliga.png" alt="Germany Wingers Passing Adjusted Comparison">

Figure 44: Germany Wingers Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_raw_Frauen_Bundesliga.png" alt="Germany Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 45: Germany Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_adj_Frauen_Bundesliga.png" alt="Germany Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 46: Germany Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 47: Germany Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 48: Germany Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-wingers-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_raw_Liga_F.png" alt="Spain Wingers Passing Raw Comparison">

Figure 49: Spain Wingers Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_adj_Liga_F.png" alt="Spain Wingers Passing Adjusted Comparison">

Figure 50: Spain Wingers Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_raw_Liga_F.png" alt="Spain Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 51: Spain Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_adj_Liga_F.png" alt="Spain Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 52: Spain Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 53: Spain Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 54: Spain Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-wingers-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_raw_Serie_A_Women.png" alt="Italy Wingers Passing Raw Comparison">

Figure 55: Italy Wingers Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/passing_adj_Serie_A_Women.png" alt="Italy Wingers Passing Adjusted Comparison">

Figure 56: Italy Wingers Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_raw_Serie_A_Women.png" alt="Italy Wingers Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 57: Italy Wingers Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/carrying_dribbling_shooting_receipt_adj_Serie_A_Women.png" alt="Italy Wingers Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 58: Italy Wingers Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Wingers Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 59: Italy Wingers Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Wingers Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 60: Italy Wingers Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players"></a>

### **Radar plots for players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-players-caroline-graham-hansen-barcelona"></a>

#### **Caroline Graham Hansen - Barcelona**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="caroline-graham-hansen-barcelona-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/passing_raw.png" alt="Caroline Graham Hansen Passing — Raw Statistics Comparison">

Figure 61: Caroline Graham Hansen — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/passing_raw_league_relative.png" alt="Caroline Graham Hansen Passing — League-Aware Raw Statistics Comparison">

Figure 62: Caroline Graham Hansen — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/passing_adj.png" alt="Caroline Graham Hansen Passing — Adjusted Statistics Comparison">

Figure 63: Caroline Graham Hansen — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/passing_adj_league_relative.png" alt="Caroline Graham Hansen Passing — League-Aware Adjusted Statistics Comparison">

Figure 64: Caroline Graham Hansen — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 65: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 66: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 67: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 68: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Caroline Graham Hansen Defending & Vulnerability — Raw Statistics Comparison">

Figure 69: Caroline Graham Hansen — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Caroline Graham Hansen Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 70: Caroline Graham Hansen — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Caroline Graham Hansen Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 71: Caroline Graham Hansen — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Caroline Graham Hansen Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 72: Caroline Graham Hansen — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="caroline-graham-hansen-barcelona-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/passing_raw.png" alt="Caroline Graham Hansen Passing — Raw Statistics Comparison">

Figure 73: Caroline Graham Hansen — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/passing_raw_league_relative.png" alt="Caroline Graham Hansen Passing — League-Aware Raw Statistics Comparison">

Figure 74: Caroline Graham Hansen — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/passing_adj.png" alt="Caroline Graham Hansen Passing — Adjusted Statistics Comparison">

Figure 75: Caroline Graham Hansen — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/passing_adj_league_relative.png" alt="Caroline Graham Hansen Passing — League-Aware Adjusted Statistics Comparison">

Figure 76: Caroline Graham Hansen — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 77: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 78: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 79: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Caroline Graham Hansen Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 80: Caroline Graham Hansen — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Caroline Graham Hansen Defending & Vulnerability — Raw Statistics Comparison">

Figure 81: Caroline Graham Hansen — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Caroline Graham Hansen Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 82: Caroline Graham Hansen — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Caroline Graham Hansen Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 83: Caroline Graham Hansen — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Caroline_Graham_Hansen_Barcelona_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Caroline Graham Hansen Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 84: Caroline Graham Hansen — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-carlotta-wamser-koln"></a>

#### **Carlotta Wamser - Koln**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="carlotta-wamser-koln-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/passing_raw.png" alt="Carlotta Wamser Passing — Raw Statistics Comparison">

Figure 85: Carlotta Wamser — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/passing_raw_league_relative.png" alt="Carlotta Wamser Passing — League-Aware Raw Statistics Comparison">

Figure 86: Carlotta Wamser — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/passing_adj.png" alt="Carlotta Wamser Passing — Adjusted Statistics Comparison">

Figure 87: Carlotta Wamser — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/passing_adj_league_relative.png" alt="Carlotta Wamser Passing — League-Aware Adjusted Statistics Comparison">

Figure 88: Carlotta Wamser — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_raw.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 89: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 90: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_adj.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 91: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 92: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_raw.png" alt="Carlotta Wamser Defending & Vulnerability — Raw Statistics Comparison">

Figure 93: Carlotta Wamser — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Carlotta Wamser Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 94: Carlotta Wamser — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_adj.png" alt="Carlotta Wamser Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 95: Carlotta Wamser — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Carlotta Wamser Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 96: Carlotta Wamser — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="carlotta-wamser-koln-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/passing_raw.png" alt="Carlotta Wamser Passing — Raw Statistics Comparison">

Figure 97: Carlotta Wamser — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/passing_raw_league_relative.png" alt="Carlotta Wamser Passing — League-Aware Raw Statistics Comparison">

Figure 98: Carlotta Wamser — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/passing_adj.png" alt="Carlotta Wamser Passing — Adjusted Statistics Comparison">

Figure 99: Carlotta Wamser — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/passing_adj_league_relative.png" alt="Carlotta Wamser Passing — League-Aware Adjusted Statistics Comparison">

Figure 100: Carlotta Wamser — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_raw.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 101: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 102: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_adj.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 103: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Carlotta Wamser Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 104: Carlotta Wamser — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_raw.png" alt="Carlotta Wamser Defending & Vulnerability — Raw Statistics Comparison">

Figure 105: Carlotta Wamser — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Carlotta Wamser Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 106: Carlotta Wamser — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_adj.png" alt="Carlotta Wamser Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 107: Carlotta Wamser — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Carlotta_Wamser_Köln/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Carlotta Wamser Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 108: Carlotta Wamser — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-grace-clinton-tottenham-hotspur"></a>

#### **Grace Clinton - Tottenham Hotspur**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="grace-clinton-tottenham-hotspur-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/passing_raw.png" alt="Grace Clinton Passing — Raw Statistics Comparison">

Figure 109: Grace Clinton — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/passing_raw_league_relative.png" alt="Grace Clinton Passing — League-Aware Raw Statistics Comparison">

Figure 110: Grace Clinton — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/passing_adj.png" alt="Grace Clinton Passing — Adjusted Statistics Comparison">

Figure 111: Grace Clinton — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/passing_adj_league_relative.png" alt="Grace Clinton Passing — League-Aware Adjusted Statistics Comparison">

Figure 112: Grace Clinton — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_raw.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 113: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 114: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_adj.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 115: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 116: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_raw.png" alt="Grace Clinton Defending & Vulnerability — Raw Statistics Comparison">

Figure 117: Grace Clinton — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Grace Clinton Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 118: Grace Clinton — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_adj.png" alt="Grace Clinton Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 119: Grace Clinton — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Grace Clinton Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 120: Grace Clinton — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="grace-clinton-tottenham-hotspur-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/passing_raw.png" alt="Grace Clinton Passing — Raw Statistics Comparison">

Figure 121: Grace Clinton — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/passing_raw_league_relative.png" alt="Grace Clinton Passing — League-Aware Raw Statistics Comparison">

Figure 122: Grace Clinton — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/passing_adj.png" alt="Grace Clinton Passing — Adjusted Statistics Comparison">

Figure 123: Grace Clinton — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/passing_adj_league_relative.png" alt="Grace Clinton Passing — League-Aware Adjusted Statistics Comparison">

Figure 124: Grace Clinton — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_raw.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 125: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 126: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_adj.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 127: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Grace Clinton Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 128: Grace Clinton — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_raw.png" alt="Grace Clinton Defending & Vulnerability — Raw Statistics Comparison">

Figure 129: Grace Clinton — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Grace Clinton Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 130: Grace Clinton — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_adj.png" alt="Grace Clinton Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 131: Grace Clinton — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Grace_Clinton_Tottenham_Hotspur_Women/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Grace Clinton Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 132: Grace Clinton — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-jule-brand-vfl-wolfsburg"></a>

#### **Jule Brand - VfL Wolfsburg**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="jule-brand-vfl-wolfsburg-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/passing_raw.png" alt="Jule Brand Passing — Raw Statistics Comparison">

Figure 133: Jule Brand — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/passing_raw_league_relative.png" alt="Jule Brand Passing — League-Aware Raw Statistics Comparison">

Figure 134: Jule Brand — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/passing_adj.png" alt="Jule Brand Passing — Adjusted Statistics Comparison">

Figure 135: Jule Brand — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/passing_adj_league_relative.png" alt="Jule Brand Passing — League-Aware Adjusted Statistics Comparison">

Figure 136: Jule Brand — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 137: Jule Brand — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 138: Jule Brand — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 139: Jule Brand — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 140: Jule Brand — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Jule Brand Defending & Vulnerability — Raw Statistics Comparison">

Figure 141: Jule Brand — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Jule Brand Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 142: Jule Brand — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Jule Brand Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 143: Jule Brand — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Jule Brand Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 144: Jule Brand — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="jule-brand-vfl-wolfsburg-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/passing_raw.png" alt="Jule Brand Passing — Raw Statistics Comparison">

Figure 145: Jule Brand — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/passing_raw_league_relative.png" alt="Jule Brand Passing — League-Aware Raw Statistics Comparison">

Figure 146: Jule Brand — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/passing_adj.png" alt="Jule Brand Passing — Adjusted Statistics Comparison">

Figure 147: Jule Brand — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/passing_adj_league_relative.png" alt="Jule Brand Passing — League-Aware Adjusted Statistics Comparison">

Figure 148: Jule Brand — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 149: Jule Brand — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 150: Jule Brand — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 151: Jule Brand — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Jule Brand Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 152: Jule Brand — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Jule Brand Defending & Vulnerability — Raw Statistics Comparison">

Figure 153: Jule Brand — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Jule Brand Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 154: Jule Brand — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Jule Brand Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 155: Jule Brand — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Jule_Brand_VfL_Wolfsburg_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Jule Brand Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 156: Jule Brand — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-klara-buhl-bayern-munchen"></a>

#### **Klara Buhl - Bayern Munchen**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="klara-buhl-bayern-munchen-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/passing_raw.png" alt="Klara Buhl Passing — Raw Statistics Comparison">

Figure 157: Klara Buhl — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/passing_raw_league_relative.png" alt="Klara Buhl Passing — League-Aware Raw Statistics Comparison">

Figure 158: Klara Buhl — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/passing_adj.png" alt="Klara Buhl Passing — Adjusted Statistics Comparison">

Figure 159: Klara Buhl — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/passing_adj_league_relative.png" alt="Klara Buhl Passing — League-Aware Adjusted Statistics Comparison">

Figure 160: Klara Buhl — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_raw.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 161: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 162: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_adj.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 163: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 164: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_raw.png" alt="Klara Buhl Defending & Vulnerability — Raw Statistics Comparison">

Figure 165: Klara Buhl — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Klara Buhl Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 166: Klara Buhl — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_adj.png" alt="Klara Buhl Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 167: Klara Buhl — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Klara Buhl Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 168: Klara Buhl — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="klara-buhl-bayern-munchen-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/passing_raw.png" alt="Klara Buhl Passing — Raw Statistics Comparison">

Figure 169: Klara Buhl — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/passing_raw_league_relative.png" alt="Klara Buhl Passing — League-Aware Raw Statistics Comparison">

Figure 170: Klara Buhl — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/passing_adj.png" alt="Klara Buhl Passing — Adjusted Statistics Comparison">

Figure 171: Klara Buhl — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/passing_adj_league_relative.png" alt="Klara Buhl Passing — League-Aware Adjusted Statistics Comparison">

Figure 172: Klara Buhl — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_raw.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 173: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 174: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_adj.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 175: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Klara Buhl Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 176: Klara Buhl — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_raw.png" alt="Klara Buhl Defending & Vulnerability — Raw Statistics Comparison">

Figure 177: Klara Buhl — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Klara Buhl Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 178: Klara Buhl — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_adj.png" alt="Klara Buhl Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 179: Klara Buhl — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Klara_Bühl_Bayern_München_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Klara Buhl Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 180: Klara Buhl — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-nikita-parris-manchester-united"></a>

#### **Nikita Parris - Manchester United**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="nikita-parris-manchester-united-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/passing_raw.png" alt="Nikita Parris Passing — Raw Statistics Comparison">

Figure 181: Nikita Parris — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/passing_raw_league_relative.png" alt="Nikita Parris Passing — League-Aware Raw Statistics Comparison">

Figure 182: Nikita Parris — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/passing_adj.png" alt="Nikita Parris Passing — Adjusted Statistics Comparison">

Figure 183: Nikita Parris — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/passing_adj_league_relative.png" alt="Nikita Parris Passing — League-Aware Adjusted Statistics Comparison">

Figure 184: Nikita Parris — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_raw.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 185: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 186: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_adj.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 187: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 188: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_raw.png" alt="Nikita Parris Defending & Vulnerability — Raw Statistics Comparison">

Figure 189: Nikita Parris — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Nikita Parris Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 190: Nikita Parris — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_adj.png" alt="Nikita Parris Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 191: Nikita Parris — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Nikita Parris Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 192: Nikita Parris — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="nikita-parris-manchester-united-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/passing_raw.png" alt="Nikita Parris Passing — Raw Statistics Comparison">

Figure 193: Nikita Parris — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/passing_raw_league_relative.png" alt="Nikita Parris Passing — League-Aware Raw Statistics Comparison">

Figure 194: Nikita Parris — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/passing_adj.png" alt="Nikita Parris Passing — Adjusted Statistics Comparison">

Figure 195: Nikita Parris — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/passing_adj_league_relative.png" alt="Nikita Parris Passing — League-Aware Adjusted Statistics Comparison">

Figure 196: Nikita Parris — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_raw.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 197: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 198: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_adj.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 199: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Nikita Parris Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 200: Nikita Parris — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_raw.png" alt="Nikita Parris Defending & Vulnerability — Raw Statistics Comparison">

Figure 201: Nikita Parris — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Nikita Parris Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 202: Nikita Parris — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_adj.png" alt="Nikita Parris Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 203: Nikita Parris — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Nikita_Parris_Manchester_United_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Nikita Parris Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 204: Nikita Parris — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-beth-mead-arsenal"></a>

#### **Beth Mead - Arsenal**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="beth-mead-arsenal-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/passing_raw.png" alt="Beth Mead Passing — Raw Statistics Comparison">

Figure 205: Beth Mead — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/passing_raw_league_relative.png" alt="Beth Mead Passing — League-Aware Raw Statistics Comparison">

Figure 206: Beth Mead — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/passing_adj.png" alt="Beth Mead Passing — Adjusted Statistics Comparison">

Figure 207: Beth Mead — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/passing_adj_league_relative.png" alt="Beth Mead Passing — League-Aware Adjusted Statistics Comparison">

Figure 208: Beth Mead — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 209: Beth Mead — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 210: Beth Mead — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 211: Beth Mead — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 212: Beth Mead — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Beth Mead Defending & Vulnerability — Raw Statistics Comparison">

Figure 213: Beth Mead — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Beth Mead Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 214: Beth Mead — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Beth Mead Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 215: Beth Mead — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k2/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Beth Mead Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 216: Beth Mead — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="beth-mead-arsenal-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/passing_raw.png" alt="Beth Mead Passing — Raw Statistics Comparison">

Figure 217: Beth Mead — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/passing_raw_league_relative.png" alt="Beth Mead Passing — League-Aware Raw Statistics Comparison">

Figure 218: Beth Mead — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/passing_adj.png" alt="Beth Mead Passing — Adjusted Statistics Comparison">

Figure 219: Beth Mead — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/passing_adj_league_relative.png" alt="Beth Mead Passing — League-Aware Adjusted Statistics Comparison">

Figure 220: Beth Mead — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 221: Beth Mead — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 222: Beth Mead — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 223: Beth Mead — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Beth Mead Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 224: Beth Mead — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Beth Mead Defending & Vulnerability — Raw Statistics Comparison">

Figure 225: Beth Mead — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Beth Mead Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 226: Beth Mead — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Beth Mead Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 227: Beth Mead — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Winger/k3/Bethany_Mead_Arsenal_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Beth Mead Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 228: Beth Mead — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>