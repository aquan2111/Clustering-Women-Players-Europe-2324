# **Center Midfields Attacking**

<a id="table-of-contents"></a>

## **Table of Contents**

- <a href="#player-counts" style="color:black">Player counts</a>
- <a href="#results" style="color:black">Results</a>
  - <a href="#results-for-2-clusters" style="color:black">Results for 2 clusters</a>
    - <a href="#breakdown-of-results-by-league" style="color:black">Breakdown of results by league</a>
    - <a href="#breakdown-of-results-by-features" style="color:black">Breakdown of results by features</a>
  - <a href="#breakdown-of-results-by-players" style="color:black">Breakdown of results by players</a>
    - <a href="center_midfields_attacking_Aitana_Bonmati_Conca_Barcelona_WFC.pdf" style="color:black">Aitana Bonmati - Barcelona</a>
    - <a href="center_midfields_attacking_Julia_Angela_Grosso_Juventus_W.pdf" style="color:black">Julia Grosso - Juventus</a>
    - <a href="center_midfields_attacking_Jill_Roord_Manchester_City_WFC.pdf" style="color:black">Jill Roord - Manchester City</a>
    - <a href="center_midfields_attacking_Svenja_Huth_VfL_Wolfsburg_WFC.pdf" style="color:black">Svenja Huth - VfL Wolfsburg</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-center-midfields-averages" style="color:black">Radar plots for 2 clusters center midfields' averages</a>
    - <a href="#radar-plots-for-2-clusters-center-midfields-averages-all-leagues" style="color:black">All leagues</a>
      - <a href="#radar-plots-for-2-clusters-center-midfields-averages-all-leagues-passing" style="color:black">Passing</a>
      - <a href="#radar-plots-for-2-clusters-center-midfields-averages-all-leagues-carrying-receipt-dribbling-shooting" style="color:black">Carrying, Receipt, Dribbling & Shooting</a>
      - <a href="#radar-plots-for-2-clusters-center-midfields-averages-all-leagues-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#fa-womens-super-league" style="color:black">FA Women's Super League</a>
      - <a href="#fa-womens-super-league-passing" style="color:black">Passing</a>
      - <a href="#fa-womens-super-league-carrying-receipt-dribbling-shooting" style="color:black">Carrying, Receipt, Dribbling & Shooting</a>
      - <a href="#fa-womens-super-league-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
      - <a href="#frauen-bundesliga-passing" style="color:black">Passing</a>
      - <a href="#frauen-bundesliga-carrying-receipt-dribbling-shooting" style="color:black">Carrying, Receipt, Dribbling & Shooting</a>
      - <a href="#frauen-bundesliga-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#liga-f" style="color:black">Liga F</a>
      - <a href="#liga-f-passing" style="color:black">Passing</a>
      - <a href="#liga-f-carrying-receipt-dribbling-shooting" style="color:black">Carrying, Receipt, Dribbling & Shooting</a>
      - <a href="#liga-f-defending-vulnerability" style="color:black">Defending & Vulnerability</a>
    - <a href="#serie-a-women" style="color:black">Serie A Women</a>
      - <a href="#serie-a-women-passing" style="color:black">Passing</a>
      - <a href="#serie-a-women-carrying-receipt-dribbling-shooting" style="color:black">Carrying, Receipt, Dribbling & Shooting</a>
      - <a href="#serie-a-women-defending-vulnerability" style="color:black">Defending & Vulnerability</a>

<div style="page-break-before: always; break-before: page;"></div>

<a id="player-counts"></a>

## **Player counts**

In this project, there are a total of 43 attacking center midfields considered, with

* 21 attacking center midfields in 12 teams in the English FA Women's Super League
* 19 attacking center midfields in 12 teams in the German Frauen Bundesliga
* 26 attacking center midfields in 16 teams in the Spanish Liga F
* 17 attacking center midfields in 10 teams in the Italian Serie A Women

<a id="results"></a>

## **Results**

<a id="results-for-2-clusters"></a>

### **Results for 2 clusters**

<a id="breakdown-of-results-by-league"></a>

#### **Breakdown of results by league**

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

* Cluster 0 midfielders involved in higher up the pitch positions, including receiving, pressing, commiting fouls, and other vulnerability features. They also made counterpress actions at higher rates. Passing was their main progression method.
* On the other hand, cluster 1 midfielders made more ground passes and carried longer. They progressed more by carrying. Average press time for these players was longer.

Therefore, based on these results,

* Cluster 0 attacking midfielders can be seen as advanced high pressing operators, acting as shadow strikers.
* Cluster 1 attacking midfielders can be seen as deeper distributors and carriers, although can still be seen as advanced playmakers.

<a id="breakdown-of-results-by-players"></a>

### **Breakdown of results by players**

Findings and radar plots for each attacking center midfielder are in their own files:

- <a href="center_midfields_attacking_Aitana_Bonmati_Conca_Barcelona_WFC.pdf" style="color:black">Aitana Bonmati - Barcelona</a>
- <a href="center_midfields_attacking_Julia_Angela_Grosso_Juventus_W.pdf" style="color:black">Julia Grosso - Juventus</a>
- <a href="center_midfields_attacking_Jill_Roord_Manchester_City_WFC.pdf" style="color:black">Jill Roord - Manchester City</a>
- <a href="center_midfields_attacking_Svenja_Huth_VfL_Wolfsburg_WFC.pdf" style="color:black">Svenja Huth - VfL Wolfsburg</a>

<div style="page-break-before: always; break-before: page;"></div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="appendix"></a>

## **Appendix**

<a id="radar-plots-for-2-clusters-center-midfields-averages"></a>

### **Radar plots for 2 clusters center midfields' averages**

<a id="radar-plots-for-2-clusters-center-midfields-averages-all-leagues"></a>

#### **All leagues**

<a id="radar-plots-for-2-clusters-center-midfields-averages-all-leagues-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_raw.png" alt="Center Midfields Attacking Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 1: Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_subcluster_adj.png" alt="Center Midfields Attacking Passing Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 2: Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-midfields-averages-all-leagues-carrying-receipt-dribbling-shooting"></a>

##### **Carrying, Receipt, Dribbling & Shooting**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw.png" alt="Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 3: Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj.png" alt="Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 4: Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-center-midfields-averages-all-leagues-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw.png" alt="Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 5: Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj.png" alt="Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 6: Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="fa-womens-super-league"></a>

#### **FA Women's Super League**

<a id="fa-womens-super-league-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_raw_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 7: England Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Passing Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 8: England Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="fa-womens-super-league-carrying-receipt-dribbling-shooting"></a>

##### **Carrying, Receipt, Dribbling & Shooting**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 9: England Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 10: England Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="fa-womens-super-league-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 11: England Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_FA_Womens_Super_League.png" alt="England Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 12: England Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<a id="frauen-bundesliga-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 13: Germany Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Passing Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 14: Germany Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="frauen-bundesliga-carrying-receipt-dribbling-shooting"></a>

##### **Carrying, Receipt, Dribbling & Shooting**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 15: Germany Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 16: Germany Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="frauen-bundesliga-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 17: Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_Frauen_Bundesliga.png" alt="Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 18: Germany Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="liga-f"></a>

#### **Liga F**

<a id="liga-f-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_raw_Liga_F.png" alt="Spain Center Midfields Attacking Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 19: Spain Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_Liga_F.png" alt="Spain Center Midfields Attacking Passing Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 20: Spain Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="liga-f-carrying-receipt-dribbling-shooting"></a>

##### **Carrying, Receipt, Dribbling & Shooting**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_Liga_F.png" alt="Spain Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 21: Spain Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_Liga_F.png" alt="Spain Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 22: Spain Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="liga-f-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_Liga_F.png" alt="Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 23: Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_Liga_F.png" alt="Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 24: Spain Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="serie-a-women"></a>

#### **Serie A Women**

<a id="serie-a-women-passing"></a>

##### **Passing**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_raw_Serie_A_Women.png" alt="Italy Center Midfields Attacking Passing Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 25: Italy Center Midfields Attacking Passing — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/passing_subcluster_adj_Serie_A_Women.png" alt="Italy Center Midfields Attacking Passing Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 26: Italy Center Midfields Attacking Passing — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="serie-a-women-carrying-receipt-dribbling-shooting"></a>

##### **Carrying, Receipt, Dribbling & Shooting**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_raw_Serie_A_Women.png" alt="Italy Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 27: Italy Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/carrying_receipt_dribbling_shooting_subcluster_adj_Serie_A_Women.png" alt="Italy Center Midfields Attacking Carrying, Receipt, Dribbling &amp; Shooting Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 28: Italy Center Midfields Attacking Carrying, Receipt, Dribbling & Shooting — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="serie-a-women-defending-vulnerability"></a>

##### **Defending & Vulnerability**

<div style="page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_raw_Serie_A_Women.png" alt="Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 29: Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty — Raw Statistics Comparison, 2 Clusters
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Center%20Midfield%20Attacking/k2/defending_vulnerability_fifty_fifty_subcluster_adj_Serie_A_Women.png" alt="Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty Subcluster Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 30: Italy Center Midfields Attacking Defending Vulnerability Fifty Fifty — Subcluster Adjusted Statistics Comparison, 2 Clusters
</td>
</tr>
</table>
</div>
