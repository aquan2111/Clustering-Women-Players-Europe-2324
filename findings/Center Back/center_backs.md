# **Center Backs**

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
    - <a href="center_backs_Molly_Bartrip_Tottenham_Hotspur_Women.pdf" style="color:black">Molly Bartrip - Tottenham Hotspur</a>
    - <a href="center_backs_Elba_Verges_Prats_SD_Eibar.pdf" style="color:black">Elba Verges Prats - SD Eibar</a>
    - <a href="center_backs_Kathrin_Julia_Hendrich_VfL_Wolfsburg_WFC.pdf" style="color:black">Kathy Hendrich - VfL Wolfsburg</a>
    - <a href="center_backs_Sophie_Howard_Leicester_City_WFC.pdf" style="color:black">Sophie Howard - Leicester City</a>
    - <a href="center_backs_Risa_Shimizu_West_Ham_United_LFC.pdf" style="color:black">Risa Shimizu - West Ham United</a>
    - <a href="center_backs_Alex_Greenwood_Manchester_City_WFC.pdf" style="color:black">Alex Greenwood - Manchester City</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-center-backs-averages" style="color:black">Radar plots for 2 clusters center backs' averages</a>
    - <a href="#radar-plots-for-2-clusters-center-backs-averages-all-leagues" style="color:black">All leagues</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-all-leagues-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-all-leagues-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-all-leagues-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-2-clusters-center-backs-averages-liga-f" style="color:black">Liga F</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-liga-f-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-liga-f-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-liga-f-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-2-clusters-center-backs-averages-serie-a-women" style="color:black">Serie A Women</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-serie-a-women-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-serie-a-women-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-2-clusters-center-backs-averages-serie-a-women-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
  - <a href="#radar-plots-for-3-clusters-center-backs-averages" style="color:black">Radar plots for 3 clusters center backs' averages</a>
    - <a href="#radar-plots-for-3-clusters-center-backs-averages-all-leagues" style="color:black">All leagues</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-all-leagues-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-all-leagues-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-all-leagues-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-3-clusters-center-backs-averages-liga-f" style="color:black">Liga F</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-liga-f-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-liga-f-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-liga-f-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#radar-plots-for-3-clusters-center-backs-averages-serie-a-women" style="color:black">Serie A Women</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-serie-a-women-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-serie-a-women-carrying-receipt" style="color:black">Carrying & Receipt</a>
      - <a href="#radar-plots-for-3-clusters-center-backs-averages-serie-a-women-defending-vulnerability" style="color:black">Defending & Vulnerability</a>

<div style="page-break-before: always; break-before: page;"></div>

<a id="player-counts"></a>

## **Player counts**

In this project, there are a total of 154 center backs considered, with

* 39 center backs in 12 teams in the English FA Women's Super League
* 36 center backs in 12 teams in the German Frauen Bundesliga
* 53 center backs in 16 teams in the Spanish Liga F
* 26 center backs in 10 teams in the Italian Serie A Women

<a id="results"></a>

## **Results**

<a id="results-for-2-clusters"></a>

### **Results for 2 clusters**

<a id="results-for-2-clusters-breakdown-of-results-by-league"></a>

#### **Breakdown of results by league**

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
      <td>23</td>
      <td>24</td>
      <td>36</td>
      <td>18</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16</td>
      <td>12</td>
      <td>17</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>

Eventually the split between 2 clusters stay close to 2:1 for all four leagues.

<a id="results-for-2-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

- Cluster 0 center backs' defensive actions happen lower, while they passed more on the ground and their passing lengths under pressure were less affected.
- On the other hand, cluster 1 center backs engage more highly, both in terms of receiving and defending, while attempting more forward and progressive passes into the final third.

Therefore, based on these results,

- Cluster 0 center backs can be seen as traditional defenders who tend to hold the defensive line.
- Cluster 1 center backs can be seen as stoppers who are more aggressive in stepping up for defensive actions.

<a id="results-for-3-clusters"></a>

### **Results for 3 clusters**

<a id="results-for-3-clusters-breakdown-of-results-by-league"></a>

#### **Breakdown of results by league**

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
      <td>11</td>
      <td>8</td>
      <td>13</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>15</td>
      <td>19</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14</td>
      <td>13</td>
      <td>21</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>

There seem to be more variances in terms of how players are splitted between clusters within each league.

<a id="comparing-results-for-2-clusters-against-3-clusters"></a>

#### **Comparing results for 2 clusters against 3 clusters**

<div>
<table  border="1">
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
      <td>2</td>
      <td>42</td>
      <td>57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>35</td>
      <td>18</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>

It seems like k = 3 cluster 1 is a shared middle zone between the two k = 2 clusters.

<a id="results-for-3-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

- Cluster 0 shows more positiveness towards average positioning for receiving and defensive actions, and progressive forward passing.
- Cluster 2, on the other hand, shows more positiveness towards average pass length change under pressure, while engage in defensive actions at much lower positions.
- While for cluster 1, most of their features stayed in between the other two clusters, not much really stood out.

Hence, the following conclusions can be made:

- Similar to k = 2 cluster 0, k = 3 cluster 2 center backs can be seen as traditional defenders holding the line.
- Similar to k = 2 cluster 1, k = 3 cluster 0 center backs can be seen as stoppers.
- Cluster 1, while they engage in defending as highly as cluster 0, their passing look close to cluster 2, which can be seen as high engagement low progressing center backs.

However, these results are not stable as number of components are added, so results are not highly confident.

<a id="breakdown-of-results-by-players"></a>

### **Breakdown of results by players**

Findings and radar plots for each center back are in their own files:

- <a href="center_backs_Molly_Bartrip_Tottenham_Hotspur_Women.pdf" style="color:black">Molly Bartrip - Tottenham Hotspur</a>
- <a href="center_backs_Elba_Verges_Prats_SD_Eibar.pdf" style="color:black">Elba Verges Prats - SD Eibar</a>
- <a href="center_backs_Kathrin_Julia_Hendrich_VfL_Wolfsburg_WFC.pdf" style="color:black">Kathy Hendrich - VfL Wolfsburg</a>
- <a href="center_backs_Sophie_Howard_Leicester_City_WFC.pdf" style="color:black">Sophie Howard - Leicester City</a>
- <a href="center_backs_Risa_Shimizu_West_Ham_United_LFC.pdf" style="color:black">Risa Shimizu - West Ham United</a>
- <a href="center_backs_Alex_Greenwood_Manchester_City_WFC.pdf" style="color:black">Alex Greenwood - Manchester City</a>

<div style="page-break-before: always; break-before: page;"></div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="appendix"></a>

## **Appendix**

<a id="radar-plots-for-2-clusters-center-backs-averages"></a>

### **Radar plots for 2 clusters center backs' averages**

<a id="radar-plots-for-2-clusters-center-backs-averages-all-leagues"></a>

#### **All leagues**

<a id="radar-plots-for-2-clusters-center-backs-averages-all-leagues-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_raw.png" alt="Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 1: Center Backs Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_adj.png" alt="Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 2: Center Backs Passing — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-all-leagues-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_raw.png" alt="Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 3: Center Backs Carrying Receipt — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_adj.png" alt="Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 4: Center Backs Carrying Receipt — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-all-leagues-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_raw.png" alt="Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 5: Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_adj.png" alt="Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 6: Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<a id="radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_raw_FA_Womens_Super_League.png" alt="England Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 7: England Center Backs Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_adj_FA_Womens_Super_League.png" alt="England Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 8: England Center Backs Passing — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_raw_FA_Womens_Super_League.png" alt="England Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 9: England Center Backs Carrying Receipt — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_adj_FA_Womens_Super_League.png" alt="England Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 10: England Center Backs Carrying Receipt — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-fa-womens-super-league-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 11: England Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 12: England Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<a id="radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 13: Germany Center Backs Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_adj_Frauen_Bundesliga.png" alt="Germany Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 14: Germany Center Backs Passing — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_raw_Frauen_Bundesliga.png" alt="Germany Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 15: Germany Center Backs Carrying Receipt — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_adj_Frauen_Bundesliga.png" alt="Germany Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 16: Germany Center Backs Carrying Receipt — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-frauen-bundesliga-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 17: Germany Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 18: Germany Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-liga-f"></a>

#### **Liga F**

<a id="radar-plots-for-2-clusters-center-backs-averages-liga-f-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_raw_Liga_F.png" alt="Spain Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 19: Spain Center Backs Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_adj_Liga_F.png" alt="Spain Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 20: Spain Center Backs Passing — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-liga-f-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_raw_Liga_F.png" alt="Spain Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 21: Spain Center Backs Carrying Receipt — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_adj_Liga_F.png" alt="Spain Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 22: Spain Center Backs Carrying Receipt — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-liga-f-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 23: Spain Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 24: Spain Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-serie-a-women"></a>

#### **Serie A Women**

<a id="radar-plots-for-2-clusters-center-backs-averages-serie-a-women-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_raw_Serie_A_Women.png" alt="Italy Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 25: Italy Center Backs Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/passing_adj_Serie_A_Women.png" alt="Italy Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 26: Italy Center Backs Passing — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-serie-a-women-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_raw_Serie_A_Women.png" alt="Italy Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 27: Italy Center Backs Carrying Receipt — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/carrying_receipt_adj_Serie_A_Women.png" alt="Italy Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 28: Italy Center Backs Carrying Receipt — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-backs-averages-serie-a-women-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 29: Italy Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k2/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 30: Italy Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages"></a>

### **Radar plots for 3 clusters center backs' averages**

<a id="radar-plots-for-3-clusters-center-backs-averages-all-leagues"></a>

#### **All leagues**

<a id="radar-plots-for-3-clusters-center-backs-averages-all-leagues-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_raw.png" alt="Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 31: Center Backs Passing — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_adj.png" alt="Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 32: Center Backs Passing — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-all-leagues-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_raw.png" alt="Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 33: Center Backs Carrying Receipt — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_adj.png" alt="Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 34: Center Backs Carrying Receipt — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-all-leagues-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_raw.png" alt="Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 35: Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_adj.png" alt="Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 36: Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<a id="radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_raw_FA_Womens_Super_League.png" alt="England Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 37: England Center Backs Passing — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_adj_FA_Womens_Super_League.png" alt="England Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 38: England Center Backs Passing — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_raw_FA_Womens_Super_League.png" alt="England Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 39: England Center Backs Carrying Receipt — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_adj_FA_Womens_Super_League.png" alt="England Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 40: England Center Backs Carrying Receipt — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-fa-womens-super-league-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 41: England Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_adj_FA_Womens_Super_League.png" alt="England Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 42: England Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<a id="radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 43: Germany Center Backs Passing — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_adj_Frauen_Bundesliga.png" alt="Germany Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 44: Germany Center Backs Passing — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_raw_Frauen_Bundesliga.png" alt="Germany Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 45: Germany Center Backs Carrying Receipt — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_adj_Frauen_Bundesliga.png" alt="Germany Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 46: Germany Center Backs Carrying Receipt — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-frauen-bundesliga-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 47: Germany Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_adj_Frauen_Bundesliga.png" alt="Germany Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 48: Germany Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-liga-f"></a>

#### **Liga F**

<a id="radar-plots-for-3-clusters-center-backs-averages-liga-f-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_raw_Liga_F.png" alt="Spain Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 49: Spain Center Backs Passing — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_adj_Liga_F.png" alt="Spain Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 50: Spain Center Backs Passing — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-liga-f-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_raw_Liga_F.png" alt="Spain Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 51: Spain Center Backs Carrying Receipt — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_adj_Liga_F.png" alt="Spain Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 52: Spain Center Backs Carrying Receipt — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-liga-f-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 53: Spain Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_adj_Liga_F.png" alt="Spain Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 54: Spain Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-serie-a-women"></a>

#### **Serie A Women**

<a id="radar-plots-for-3-clusters-center-backs-averages-serie-a-women-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_raw_Serie_A_Women.png" alt="Italy Center Backs Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 55: Italy Center Backs Passing — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/passing_adj_Serie_A_Women.png" alt="Italy Center Backs Passing Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 56: Italy Center Backs Passing — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-serie-a-women-carrying-receipt"></a>

##### **Carrying & Receipt**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_raw_Serie_A_Women.png" alt="Italy Center Backs Carrying Receipt Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 57: Italy Center Backs Carrying Receipt — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/carrying_receipt_adj_Serie_A_Women.png" alt="Italy Center Backs Carrying Receipt Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 58: Italy Center Backs Carrying Receipt — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-center-backs-averages-serie-a-women-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Backs Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 59: Italy Center Backs Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 3 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Back/k3/defending_vulnerability_fifty_fifty_adj_Serie_A_Women.png" alt="Italy Center Backs Defending Vulnerability Fifty Fifty Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 60: Italy Center Backs Defending Vulnerability Fifty Fifty — Adjusted Statistics Comparison, 3 Clusters
</td>
</tr>
</table>
</div>
