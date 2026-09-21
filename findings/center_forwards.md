# **Center Forwards**

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
    - <a href="#breakdown-of-results-by-players-mayra-ramirez-levante" style="color:black">Mayra Ramirez - Levante</a>
    - <a href="#breakdown-of-results-by-players-mayra-ramirez-chelsea" style="color:black">Mayra Ramirez - Chelsea</a>
    - <a href="#breakdown-of-results-by-players-gabi-nunes-levante" style="color:black">Gabi Nunes - Levante</a>
    - <a href="#breakdown-of-results-by-players-rachel-daly-aston-villa" style="color:black">Rachel Daly - Aston Villa</a>
    - <a href="#breakdown-of-results-by-players-khadija-shaw-manchester-city" style="color:black">Khadija Shaw - Manchester City</a>
    - <a href="#breakdown-of-results-by-players-alba-redondo-levante" style="color:black">Alba Redondo - Levante</a>
    - <a href="#breakdown-of-results-by-players-andrea-staskova-ac-milan" style="color:black">Andrea Staskova - AC Milan</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-center-forwards-averages" style="color:black">Radar plots for 2 clusters center forwards' averages</a>
    - <a href="#radar-plots-for-2-clusters-center-forwards-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-2-clusters-center-forwards-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-2-clusters-center-forwards-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-2-clusters-center-forwards-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-3-clusters-center-forwards-averages" style="color:black">Radar plots for 3 clusters center forwards' averages</a>
    - <a href="#radar-plots-for-3-clusters-center-forwards-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-3-clusters-center-forwards-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-3-clusters-center-forwards-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-3-clusters-center-forwards-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-players" style="color:black">Radar plots for players</a>
    - <a href="#radar-plots-for-players-mayra-ramirez-levante" style="color:black">Mayra Ramirez - Levante</a>
      - <a href="#mayra-ramirez-levante-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#mayra-ramirez-levante-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-mayra-ramirez-chelsea" style="color:black">Mayra Ramirez - Chelsea</a>
      - <a href="#mayra-ramirez-chelsea-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#mayra-ramirez-chelsea-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-gabi-nunes-levante" style="color:black">Gabi Nunes - Levante</a>
      - <a href="#gabi-nunes-levante-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#gabi-nunes-levante-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-rachel-daly-aston-villa" style="color:black">Rachel Daly - Aston Villa</a>
      - <a href="#rachel-daly-aston-villa-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#rachel-daly-aston-villa-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-khadija-shaw-manchester-city" style="color:black">Khadija Shaw - Manchester City</a>
      - <a href="#khadija-shaw-manchester-city-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#khadija-shaw-manchester-city-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-alba-redondo-levante" style="color:black">Alba Redondo - Levante</a>
      - <a href="#alba-redondo-levante-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#alba-redondo-levante-3-cluster-plots" style="color:black">3 cluster plots</a>
    - <a href="#radar-plots-for-players-andrea-staskova-ac-milan" style="color:black">Andrea Staskova - AC Milan</a>
      - <a href="#andrea-staskova-ac-milan-2-cluster-plots" style="color:black">2 cluster plots</a>
      - <a href="#andrea-staskova-ac-milan-3-cluster-plots" style="color:black">3 cluster plots</a>


<a id="player-counts"></a>

## **Player counts**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

In this project, there are a total of 76 center forwards considered, with

* 14 center forwards in 12 teams in the English FA Women's Super League
* 17 center forwards in 12 teams in the German Frauen Bundesliga
* 29 center forwards in 16 teams in the Spanish Liga F
* 16 center forwards in 10 teams in the Italian Serie A Women

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
      <td>8</td>
      <td>11</td>
      <td>17</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>6</td>
      <td>12</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>

The split is more lopsided towards cluster 0, except for England's Women's Super League where the split was almost equal.

<a id="results-for-2-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 shows more positiveness towards forward passes, header passes and shots, backward carries, variance in location of involvement down the pitch, and quality of chances. Passing was the main method of progression.
* On the other hand, positiveness in cluster 1 can be seen in average carrying distance, forward carries, average location of involvement down the pitch (receiving, dribbling, turnovers), longer shot distances, and counterpress actions in opposing half. Carrying was the main method of progression.

Therefore, based on these results,

* Cluster 0 forwards can be seen as deep lying forwards.
* Cluster 1 forwards can be seen as advanced pressing forwards.

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
      <td>6</td>
      <td>5</td>
      <td>9</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>12</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
      <td>8</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>

The split was quite equal between all three clusters.

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
      <td>25</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>25</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

While most of k = 2 cluster 1 is converted into k = 3 cluster 0, k = 2 cluster 0 is divided further into k = 3 cluster 1 and 2. Interestingly, no players belong to k = 2 cluster 0 and k = 3 cluster 0.

<a id="results-for-3-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

* Cluster 0 forwards carried longer and more forward, involved at more advanced locations both in terms of receiving, dribbling, defending, and turning the ball over. Main method of progression is carrying.
* While for cluster 1 forwards, they passed more backward on the ground, had the highest quality of shots, involved at more varied locations.
* Cluster 2 forwards, on the other hand, passed more forward and progressive, while also stood out for switch passes, header passes and shots, passing lengths, backward carries. Main method of progression is passing.

Hence, the following conclusions can be made:

* Similar to k = 2 cluster 1, k = 3 cluster 0 forwards can be seen as advanced pressing forwards.
* Cluster 1 forwards can be interpreted as poachers whose goal was focused only on finishing chances.
* While cluster 2 forwards can be seen as target forwards.

<a id="breakdown-of-results-by-players"></a>

### **Breakdown of results by players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="breakdown-of-results-by-players-mayra-ramirez-levante"></a>

#### **Mayra Ramirez - Levante**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

During her first half stint at Levante, Ramirez was safely clustered with advanced pressing forwards. Her passes were rarely forward or progressive, while her positioning during receipts, dribbles, presses, and turnovers were high up the pitch. She was also active with counterpress actions in the opposing half. Her average carry distance was high.

<a id="breakdown-of-results-by-players-mayra-ramirez-chelsea"></a>

#### **Mayra Ramirez - Chelsea**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

After the first half of the season, Chelsea broke the then record for a British transfer by signing Ramirez. Similar to her Levante stint, she was clustered with advanced pressing forwards, although the margins were thinner. Similar to her time at Levante, her average carry distance was also high and her turnover positions were also high. On the other hand, her press, receipt, and dribble positions were not as high, and her forward passing was more positive.

<a id="breakdown-of-results-by-players-gabi-nunes-levante"></a>

#### **Gabi Nunes - Levante**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Nunes was clustered into deep lying forwards at k = 2, and then into poachers at k = 3. Her passes were shorter and not progressive but rather more backward. Her involvement locations were not too high, which include receiving, dribbling, pressing, and turning the ball over. Her chances quality were also high.

<a id="breakdown-of-results-by-players-rachel-daly-aston-villa"></a>

#### **Rachel Daly - Aston Villa**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Daly was clustered into deep lying forwards at k = 2, and then into target forwards at k = 3. Her passes were mostly forward and progressive, while her pass lengths were also longer, even under pressure. She also had a fair share of header passes and shots. Her pressing and turnover locations were low down the pitch.

<a id="breakdown-of-results-by-players-khadija-shaw-manchester-city"></a>

#### **Khadija Shaw - Manchester City**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Shaw was clustered with advanced forwards for both k = 2 and k = 3, but the margins were very close. Her pressure and miscontrol locations were high, but the same tendency was not seen in receiving, dribbling, and dispossession locations. Her average carry distance was not too long, but most carries were not backward. She did not counterpress as much in the opposing half as most other advanced forwards.

<a id="breakdown-of-results-by-players-alba-redondo-levante"></a>

#### **Alba Redondo - Levante**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Redondo was clustered with deep lying forwards at k = 2, and then into poachers at k = 3, although the margins were not too clear. Her passes were still short and mostly backward, but many of them are header passes. The quality of her shots was high. She was more involved in pressing and counterpress actions in the opposing half than most poachers do.

<a id="breakdown-of-results-by-players-andrea-staskova-ac-milan"></a>

#### **Andrea Staskova - AC Milan**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

Staskova was clustered just into deep lying forwards at k = 2, and then just into target forwards at k = 3. Her forward pass share was high, but so was her backward pass share. Her pass lengths were elevated under pressure. Her header passes and shots were also elevated, while her shot quality was high on average. Her turnover locations were also higher than most other target forwards.

<a id="appendix"></a>

## **Appendix**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-forwards-averages"></a>

### **Radar plots for 2 clusters center forwards' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_raw.png" alt="Center Forwards Passing Raw Comparison">

Figure 1: Center Forwards Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_adj.png" alt="Center Forwards Passing Adjusted Comparison">

Figure 2: Center Forwards Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_raw.png" alt="Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 3: Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_adj.png" alt="Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 4: Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_raw.png" alt="Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 5: Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_adj.png" alt="Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 6: Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-forwards-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_raw_FA_Womens_Super_League.png" alt="England Center Forwards Passing Raw Comparison">

Figure 7: England Center Forwards Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_adj_FA_Womens_Super_League.png" alt="England Center Forwards Passing Adjusted Comparison">

Figure 8: England Center Forwards Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_raw_FA_Womens_Super_League.png" alt="England Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 9: England Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_adj_FA_Womens_Super_League.png" alt="England Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 10: England Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 11: England Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 12: England Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-forwards-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Forwards Passing Raw Comparison">

Figure 13: Germany Center Forwards Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_adj_Frauen_Bundesliga.png" alt="Germany Center Forwards Passing Adjusted Comparison">

Figure 14: Germany Center Forwards Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_raw_Frauen_Bundesliga.png" alt="Germany Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 15: Germany Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_adj_Frauen_Bundesliga.png" alt="Germany Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 16: Germany Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 17: Germany Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 18: Germany Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-forwards-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_raw_Liga_F.png" alt="Spain Center Forwards Passing Raw Comparison">

Figure 19: Spain Center Forwards Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_adj_Liga_F.png" alt="Spain Center Forwards Passing Adjusted Comparison">

Figure 20: Spain Center Forwards Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_raw_Liga_F.png" alt="Spain Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 21: Spain Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_adj_Liga_F.png" alt="Spain Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 22: Spain Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 23: Spain Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 24: Spain Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-2-clusters-center-forwards-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_raw_Serie_A_Women.png" alt="Italy Center Forwards Passing Raw Comparison">

Figure 25: Italy Center Forwards Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/passing_adj_Serie_A_Women.png" alt="Italy Center Forwards Passing Adjusted Comparison">

Figure 26: Italy Center Forwards Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_raw_Serie_A_Women.png" alt="Italy Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 27: Italy Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/carrying_dribbling_shooting_receipt_adj_Serie_A_Women.png" alt="Italy Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 28: Italy Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 29: Italy Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 30: Italy Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-forwards-averages"></a>

### **Radar plots for 3 clusters center forwards' averages**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_raw.png" alt="Center Forwards Passing Raw Comparison">

Figure 31: Center Forwards Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_adj.png" alt="Center Forwards Passing Adjusted Comparison">

Figure 32: Center Forwards Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_raw.png" alt="Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 33: Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_adj.png" alt="Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 34: Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_raw.png" alt="Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 35: Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_adj.png" alt="Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 36: Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-forwards-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_raw_FA_Womens_Super_League.png" alt="England Center Forwards Passing Raw Comparison">

Figure 37: England Center Forwards Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_adj_FA_Womens_Super_League.png" alt="England Center Forwards Passing Adjusted Comparison">

Figure 38: England Center Forwards Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_raw_FA_Womens_Super_League.png" alt="England Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 39: England Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_adj_FA_Womens_Super_League.png" alt="England Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 40: England Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 41: England Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 42: England Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-forwards-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Forwards Passing Raw Comparison">

Figure 43: Germany Center Forwards Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_adj_Frauen_Bundesliga.png" alt="Germany Center Forwards Passing Adjusted Comparison">

Figure 44: Germany Center Forwards Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_raw_Frauen_Bundesliga.png" alt="Germany Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 45: Germany Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_adj_Frauen_Bundesliga.png" alt="Germany Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 46: Germany Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 47: Germany Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 48: Germany Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-forwards-averages-liga-f"></a>

#### **Liga F**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_raw_Liga_F.png" alt="Spain Center Forwards Passing Raw Comparison">

Figure 49: Spain Center Forwards Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_adj_Liga_F.png" alt="Spain Center Forwards Passing Adjusted Comparison">

Figure 50: Spain Center Forwards Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_raw_Liga_F.png" alt="Spain Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 51: Spain Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_adj_Liga_F.png" alt="Spain Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 52: Spain Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 53: Spain Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 54: Spain Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-3-clusters-center-forwards-averages-serie-a-women"></a>

#### **Serie A Women**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_raw_Serie_A_Women.png" alt="Italy Center Forwards Passing Raw Comparison">

Figure 55: Italy Center Forwards Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/passing_adj_Serie_A_Women.png" alt="Italy Center Forwards Passing Adjusted Comparison">

Figure 56: Italy Center Forwards Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_raw_Serie_A_Women.png" alt="Italy Center Forwards Carrying Dribbling Shooting Receipt Raw Comparison">

Figure 57: Italy Center Forwards Carrying Dribbling Shooting Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/carrying_dribbling_shooting_receipt_adj_Serie_A_Women.png" alt="Italy Center Forwards Carrying Dribbling Shooting Receipt Adjusted Comparison">

Figure 58: Italy Center Forwards Carrying Dribbling Shooting Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Forwards Defending Vulnerability Fifty Fifty Raw Comparison">

Figure 59: Italy Center Forwards Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Center Forwards Defending Vulnerability Fifty Fifty Adjusted Comparison">

Figure 60: Italy Center Forwards Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players"></a>

### **Radar plots for players**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-players-mayra-ramirez-levante"></a>

#### **Mayra Ramirez - Levante**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="mayra-ramirez-levante-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_raw.png" alt="Mayra Ramirez (Levante) Passing — Raw Statistics Comparison">

Figure 61: Mayra Ramirez (Levante) — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_raw_league_relative.png" alt="Mayra Ramirez (Levante) Passing — League-Aware Raw Statistics Comparison">

Figure 62: Mayra Ramirez (Levante) — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_adj.png" alt="Mayra Ramirez (Levante) Passing — Adjusted Statistics Comparison">

Figure 63: Mayra Ramirez (Levante) — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_adj_league_relative.png" alt="Mayra Ramirez (Levante) Passing — League-Aware Adjusted Statistics Comparison">

Figure 64: Mayra Ramirez (Levante) — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 65: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 66: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 67: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 68: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — Raw Statistics Comparison">

Figure 69: Mayra Ramirez (Levante) — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 70: Mayra Ramirez (Levante) — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 71: Mayra Ramirez (Levante) — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 72: Mayra Ramirez (Levante) — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="mayra-ramirez-levante-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_raw.png" alt="Mayra Ramirez (Levante) Passing — Raw Statistics Comparison">

Figure 73: Mayra Ramirez (Levante) — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_raw_league_relative.png" alt="Mayra Ramirez (Levante) Passing — League-Aware Raw Statistics Comparison">

Figure 74: Mayra Ramirez (Levante) — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_adj.png" alt="Mayra Ramirez (Levante) Passing — Adjusted Statistics Comparison">

Figure 75: Mayra Ramirez (Levante) — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/passing_adj_league_relative.png" alt="Mayra Ramirez (Levante) Passing — League-Aware Adjusted Statistics Comparison">

Figure 76: Mayra Ramirez (Levante) — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 77: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 78: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 79: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Mayra Ramirez (Levante) Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 80: Mayra Ramirez (Levante) — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — Raw Statistics Comparison">

Figure 81: Mayra Ramirez (Levante) — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 82: Mayra Ramirez (Levante) — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 83: Mayra Ramirez (Levante) — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Mayra Ramirez (Levante) Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 84: Mayra Ramirez (Levante) — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-mayra-ramirez-chelsea"></a>

#### **Mayra Ramirez - Chelsea**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="mayra-ramirez-chelsea-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_raw.png" alt="Mayra Ramirez (Chelsea) Passing — Raw Statistics Comparison">

Figure 85: Mayra Ramirez (Chelsea) — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_raw_league_relative.png" alt="Mayra Ramirez (Chelsea) Passing — League-Aware Raw Statistics Comparison">

Figure 86: Mayra Ramirez (Chelsea) — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_adj.png" alt="Mayra Ramirez (Chelsea) Passing — Adjusted Statistics Comparison">

Figure 87: Mayra Ramirez (Chelsea) — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_adj_league_relative.png" alt="Mayra Ramirez (Chelsea) Passing — League-Aware Adjusted Statistics Comparison">

Figure 88: Mayra Ramirez (Chelsea) — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_raw.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 89: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 90: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_adj.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 91: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 92: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — Raw Statistics Comparison">

Figure 93: Mayra Ramirez (Chelsea) — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 94: Mayra Ramirez (Chelsea) — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 95: Mayra Ramirez (Chelsea) — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 96: Mayra Ramirez (Chelsea) — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="mayra-ramirez-chelsea-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_raw.png" alt="Mayra Ramirez (Chelsea) Passing — Raw Statistics Comparison">

Figure 97: Mayra Ramirez (Chelsea) — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_raw_league_relative.png" alt="Mayra Ramirez (Chelsea) Passing — League-Aware Raw Statistics Comparison">

Figure 98: Mayra Ramirez (Chelsea) — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_adj.png" alt="Mayra Ramirez (Chelsea) Passing — Adjusted Statistics Comparison">

Figure 99: Mayra Ramirez (Chelsea) — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/passing_adj_league_relative.png" alt="Mayra Ramirez (Chelsea) Passing — League-Aware Adjusted Statistics Comparison">

Figure 100: Mayra Ramirez (Chelsea) — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_raw.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 101: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 102: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_adj.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 103: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Mayra Ramirez (Chelsea) Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 104: Mayra Ramirez (Chelsea) — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — Raw Statistics Comparison">

Figure 105: Mayra Ramirez (Chelsea) — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 106: Mayra Ramirez (Chelsea) — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 107: Mayra Ramirez (Chelsea) — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Mayra_Tatiana_Ramírez_Ramírez_Chelsea_FCW/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Mayra Ramirez (Chelsea) Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 108: Mayra Ramirez (Chelsea) — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-gabi-nunes-levante"></a>

#### **Gabi Nunes - Levante**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="gabi-nunes-levante-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_raw.png" alt="Gabi Nunes Passing — Raw Statistics Comparison">

Figure 109: Gabi Nunes — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_raw_league_relative.png" alt="Gabi Nunes Passing — League-Aware Raw Statistics Comparison">

Figure 110: Gabi Nunes — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_adj.png" alt="Gabi Nunes Passing — Adjusted Statistics Comparison">

Figure 111: Gabi Nunes — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_adj_league_relative.png" alt="Gabi Nunes Passing — League-Aware Adjusted Statistics Comparison">

Figure 112: Gabi Nunes — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 113: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 114: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 115: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 116: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw.png" alt="Gabi Nunes Defending & Vulnerability — Raw Statistics Comparison">

Figure 117: Gabi Nunes — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Gabi Nunes Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 118: Gabi Nunes — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj.png" alt="Gabi Nunes Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 119: Gabi Nunes — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Gabi Nunes Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 120: Gabi Nunes — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="gabi-nunes-levante-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_raw.png" alt="Gabi Nunes Passing — Raw Statistics Comparison">

Figure 121: Gabi Nunes — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_raw_league_relative.png" alt="Gabi Nunes Passing — League-Aware Raw Statistics Comparison">

Figure 122: Gabi Nunes — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_adj.png" alt="Gabi Nunes Passing — Adjusted Statistics Comparison">

Figure 123: Gabi Nunes — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/passing_adj_league_relative.png" alt="Gabi Nunes Passing — League-Aware Adjusted Statistics Comparison">

Figure 124: Gabi Nunes — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 125: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 126: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 127: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Gabi Nunes Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 128: Gabi Nunes — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw.png" alt="Gabi Nunes Defending & Vulnerability — Raw Statistics Comparison">

Figure 129: Gabi Nunes — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Gabi Nunes Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 130: Gabi Nunes — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj.png" alt="Gabi Nunes Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 131: Gabi Nunes — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Gabriela_Nunes_da_Silva_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Gabi Nunes Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 132: Gabi Nunes — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-rachel-daly-aston-villa"></a>

#### **Rachel Daly - Aston Villa**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="rachel-daly-aston-villa-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/passing_raw.png" alt="Rachel Daly Passing — Raw Statistics Comparison">

Figure 133: Rachel Daly — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/passing_raw_league_relative.png" alt="Rachel Daly Passing — League-Aware Raw Statistics Comparison">

Figure 134: Rachel Daly — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/passing_adj.png" alt="Rachel Daly Passing — Adjusted Statistics Comparison">

Figure 135: Rachel Daly — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/passing_adj_league_relative.png" alt="Rachel Daly Passing — League-Aware Adjusted Statistics Comparison">

Figure 136: Rachel Daly — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_raw.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 137: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 138: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_adj.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 139: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 140: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_raw.png" alt="Rachel Daly Defending & Vulnerability — Raw Statistics Comparison">

Figure 141: Rachel Daly — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Rachel Daly Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 142: Rachel Daly — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_adj.png" alt="Rachel Daly Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 143: Rachel Daly — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Rachel Daly Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 144: Rachel Daly — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="rachel-daly-aston-villa-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/passing_raw.png" alt="Rachel Daly Passing — Raw Statistics Comparison">

Figure 145: Rachel Daly — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/passing_raw_league_relative.png" alt="Rachel Daly Passing — League-Aware Raw Statistics Comparison">

Figure 146: Rachel Daly — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/passing_adj.png" alt="Rachel Daly Passing — Adjusted Statistics Comparison">

Figure 147: Rachel Daly — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/passing_adj_league_relative.png" alt="Rachel Daly Passing — League-Aware Adjusted Statistics Comparison">

Figure 148: Rachel Daly — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_raw.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 149: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 150: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_adj.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 151: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Rachel Daly Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 152: Rachel Daly — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_raw.png" alt="Rachel Daly Defending & Vulnerability — Raw Statistics Comparison">

Figure 153: Rachel Daly — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Rachel Daly Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 154: Rachel Daly — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_adj.png" alt="Rachel Daly Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 155: Rachel Daly — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Rachel_Daly_Aston_Villa_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Rachel Daly Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 156: Rachel Daly — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-khadija-shaw-manchester-city"></a>

#### **Khadija Shaw - Manchester City**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="khadija-shaw-manchester-city-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_raw.png" alt="Khadija Shaw Passing — Raw Statistics Comparison">

Figure 157: Khadija Shaw — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_raw_league_relative.png" alt="Khadija Shaw Passing — League-Aware Raw Statistics Comparison">

Figure 158: Khadija Shaw — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_adj.png" alt="Khadija Shaw Passing — Adjusted Statistics Comparison">

Figure 159: Khadija Shaw — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_adj_league_relative.png" alt="Khadija Shaw Passing — League-Aware Adjusted Statistics Comparison">

Figure 160: Khadija Shaw — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 161: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 162: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 163: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 164: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Khadija Shaw Defending & Vulnerability — Raw Statistics Comparison">

Figure 165: Khadija Shaw — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Khadija Shaw Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 166: Khadija Shaw — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Khadija Shaw Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 167: Khadija Shaw — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Khadija Shaw Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 168: Khadija Shaw — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="khadija-shaw-manchester-city-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_raw.png" alt="Khadija Shaw Passing — Raw Statistics Comparison">

Figure 169: Khadija Shaw — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_raw_league_relative.png" alt="Khadija Shaw Passing — League-Aware Raw Statistics Comparison">

Figure 170: Khadija Shaw — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_adj.png" alt="Khadija Shaw Passing — Adjusted Statistics Comparison">

Figure 171: Khadija Shaw — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/passing_adj_league_relative.png" alt="Khadija Shaw Passing — League-Aware Adjusted Statistics Comparison">

Figure 172: Khadija Shaw — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_raw.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 173: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 174: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_adj.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 175: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Khadija Shaw Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 176: Khadija Shaw — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw.png" alt="Khadija Shaw Defending & Vulnerability — Raw Statistics Comparison">

Figure 177: Khadija Shaw — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Khadija Shaw Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 178: Khadija Shaw — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_adj.png" alt="Khadija Shaw Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 179: Khadija Shaw — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Khadija_Monifa_Shaw_Manchester_City_WFC/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Khadija Shaw Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 180: Khadija Shaw — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-alba-redondo-levante"></a>

#### **Alba Redondo - Levante**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="alba-redondo-levante-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_raw.png" alt="Alba Redondo Passing — Raw Statistics Comparison">

Figure 181: Alba Redondo — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_raw_league_relative.png" alt="Alba Redondo Passing — League-Aware Raw Statistics Comparison">

Figure 182: Alba Redondo — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_adj.png" alt="Alba Redondo Passing — Adjusted Statistics Comparison">

Figure 183: Alba Redondo — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_adj_league_relative.png" alt="Alba Redondo Passing — League-Aware Adjusted Statistics Comparison">

Figure 184: Alba Redondo — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 185: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 186: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 187: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 188: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw.png" alt="Alba Redondo Defending & Vulnerability — Raw Statistics Comparison">

Figure 189: Alba Redondo — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Alba Redondo Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 190: Alba Redondo — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj.png" alt="Alba Redondo Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 191: Alba Redondo — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Alba Redondo Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 192: Alba Redondo — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="alba-redondo-levante-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_raw.png" alt="Alba Redondo Passing — Raw Statistics Comparison">

Figure 193: Alba Redondo — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_raw_league_relative.png" alt="Alba Redondo Passing — League-Aware Raw Statistics Comparison">

Figure 194: Alba Redondo — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_adj.png" alt="Alba Redondo Passing — Adjusted Statistics Comparison">

Figure 195: Alba Redondo — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/passing_adj_league_relative.png" alt="Alba Redondo Passing — League-Aware Adjusted Statistics Comparison">

Figure 196: Alba Redondo — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 197: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 198: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 199: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Alba Redondo Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 200: Alba Redondo — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw.png" alt="Alba Redondo Defending & Vulnerability — Raw Statistics Comparison">

Figure 201: Alba Redondo — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Alba Redondo Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 202: Alba Redondo — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj.png" alt="Alba Redondo Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 203: Alba Redondo — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Alba_María_Redondo_Ferrer_Levante_UD_Femenino/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Alba Redondo Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 204: Alba Redondo — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<a id="radar-plots-for-players-andrea-staskova-ac-milan"></a>

#### **Andrea Staskova - AC Milan**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="andrea-staskova-ac-milan-2-cluster-plots"></a>

##### **2 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/passing_raw.png" alt="Andrea Staskova Passing — Raw Statistics Comparison">

Figure 205: Andrea Staskova — Passing — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/passing_raw_league_relative.png" alt="Andrea Staskova Passing — League-Aware Raw Statistics Comparison">

Figure 206: Andrea Staskova — Passing — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/passing_adj.png" alt="Andrea Staskova Passing — Adjusted Statistics Comparison">

Figure 207: Andrea Staskova — Passing — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/passing_adj_league_relative.png" alt="Andrea Staskova Passing — League-Aware Adjusted Statistics Comparison">

Figure 208: Andrea Staskova — Passing — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_raw.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 209: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 210: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_adj.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 211: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 212: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_raw.png" alt="Andrea Staskova Defending & Vulnerability — Raw Statistics Comparison">

Figure 213: Andrea Staskova — Defending & Vulnerability — Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Andrea Staskova Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 214: Andrea Staskova — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_adj.png" alt="Andrea Staskova Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 215: Andrea Staskova — Defending & Vulnerability — Adjusted Statistics Comparison, 2 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k2/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Andrea Staskova Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 216: Andrea Staskova — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 2 Clusters

</div>

<a id="andrea-staskova-ac-milan-3-cluster-plots"></a>

##### **3 cluster plots**

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/passing_raw.png" alt="Andrea Staskova Passing — Raw Statistics Comparison">

Figure 217: Andrea Staskova — Passing — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/passing_raw_league_relative.png" alt="Andrea Staskova Passing — League-Aware Raw Statistics Comparison">

Figure 218: Andrea Staskova — Passing — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/passing_adj.png" alt="Andrea Staskova Passing — Adjusted Statistics Comparison">

Figure 219: Andrea Staskova — Passing — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/passing_adj_league_relative.png" alt="Andrea Staskova Passing — League-Aware Adjusted Statistics Comparison">

Figure 220: Andrea Staskova — Passing — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_raw.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison">

Figure 221: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_raw_league_relative.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison">

Figure 222: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_adj.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison">

Figure 223: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/carrying_dribbling_shooting_receipt_adj_league_relative.png" alt="Andrea Staskova Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison">

Figure 224: Andrea Staskova — Carrying, Dribbling, Shooting & Receipt — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_raw.png" alt="Andrea Staskova Defending & Vulnerability — Raw Statistics Comparison">

Figure 225: Andrea Staskova — Defending & Vulnerability — Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_raw_league_relative.png" alt="Andrea Staskova Defending & Vulnerability — League-Aware Raw Statistics Comparison">

Figure 226: Andrea Staskova — Defending & Vulnerability — League-Aware Raw Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_adj.png" alt="Andrea Staskova Defending & Vulnerability — Adjusted Statistics Comparison">

Figure 227: Andrea Staskova — Defending & Vulnerability — Adjusted Statistics Comparison, 3 Clusters

</div>

<div align="center">

<img src="../radar_charts/Center%20Forward/k3/Andrea_Stašková_AC_Milan_W/defending_vulnerability_fifty_fifty_adj_league_relative.png" alt="Andrea Staskova Defending & Vulnerability — League-Aware Adjusted Statistics Comparison">

Figure 228: Andrea Staskova — Defending & Vulnerability — League-Aware Adjusted Statistics Comparison, 3 Clusters

</div>