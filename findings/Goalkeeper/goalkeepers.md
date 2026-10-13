# **Goalkeepers**

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
    - <a href="goalkeepers_Zecira_Musovic_Chelsea_FCW.md" style="color:black">Zecira Musovic - Chelsea</a>
    - <a href="goalkeepers_Hannah_Hampton_Chelsea_FCW.md" style="color:black">Hannah Hampton - Chelsea</a>
    - <a href="goalkeepers_Rebecca_Leigh_Spencer_Tottenham_Hotspur_Women.md" style="color:black">Rebecca Leigh Spencer - Tottenham Hotspur</a>
    - <a href="goalkeepers_Mária_Korenčiová_Como_W.md" style="color:black">Maria Korenciova - Como</a>
    - <a href="goalkeepers_Mary_Alexandra_Earps_Manchester_United_W.md" style="color:black">Mary Earps - Manchester United</a>
- <a href="#appendix" style="color:black">Appendix</a>
  - <a href="#radar-plots-for-2-clusters-goalkeepers-averages" style="color:black">Radar plots for 2 clusters goalkeepers' averages</a>
    - <a href="#radar-plots-for-2-clusters-goalkeepers-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-2-clusters-goalkeepers-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-2-clusters-goalkeepers-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-2-clusters-goalkeepers-averages-serie-a-women" style="color:black">Serie A Women</a>
  - <a href="#radar-plots-for-3-clusters-goalkeepers-averages" style="color:black">Radar plots for 3 clusters goalkeepers' averages</a>
    - <a href="#radar-plots-for-3-clusters-goalkeepers-averages-fa-womens-super-league" style="color:black">FA Women's Super League</a>
    - <a href="#radar-plots-for-3-clusters-goalkeepers-averages-frauen-bundesliga" style="color:black">Frauen Bundesliga</a>
    - <a href="#radar-plots-for-3-clusters-goalkeepers-averages-liga-f" style="color:black">Liga F</a>
    - <a href="#radar-plots-for-3-clusters-goalkeepers-averages-serie-a-women" style="color:black">Serie A Women</a>

<div style="page-break-before: always; break-before: page;"></div>

<a id="player-counts"></a>

## **Player counts**

In this project, there are a total of 60 goalkeepers considered, with

- 15 goalkeepers in 12 teams in the English FA Women's Super League
- 14 goalkeepers in 12 teams in the German Frauen Bundesliga
- 19 goalkeepers in 16 teams in the Spanish Liga F
- 12 goalkeepers in 10 teams in the Italian Serie A Women

<a id="results"></a>

## **Results**

<a id="results-for-2-clusters"></a>

### **Results for 2 clusters**

<a id="results-for-2-clusters-breakdown-of-results-by-league"></a>

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
      <td>10</td>
      <td>9</td>
      <td>15</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>

The split for two clusters is around 2 for 1 for all leagues, although Liga F is much more lopsided.

<a id="results-for-2-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

- Cluster 0 players on average had more share of their passes on the ground and from keepers' arms. Eventually this can align to a more modern style of ball playing goalkeepers

- On the other hand, cluster 1 players on average attempted longer passes including under pressure and had more share of passes from drop kicks. This can align to more traditional goalkeepers.

Eventually goalkeeper qualities such as saving or sweeping do not contribute to clustering results as much as passing qualities.

<a id="results-for-3-clusters"></a>

### **Results for 3 clusters**

<a id="results-for-3-clusters-breakdown-of-results-by-league"></a>

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
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>10</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>4</td>
      <td>6</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>

The split is more concentrated towards cluster 1 for all leagues.

<a id="comparing-results-for-2-clusters-against-3-clusters"></a>

#### **Comparing results for 2 clusters against 3 clusters**

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
      <td>12</td>
      <td>24</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>5</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>

Most of k = 2 cluster 1 is retained in k = 3 cluster 2, while k = 3 is where both clusters break into, with more coming from k = 2 cluster 0.

<a id="results-for-3-clusters-breakdown-of-results-by-features"></a>

#### **Breakdown of results by features**

- Cluster 0 goalkeepers stand out for high share of passes on the ground, passes from keepers' arms, and lower sweeping positions. These keepers can be read as ball playing keepers.
- While cluster 1 goalkeepers, in contrast, sweep at higher positions, while passing share stays in the middle of the other two clusters. These keepers can be interpreted as sweeper keepers.
- Cluster 2 goalkeepers are characterized by higher average pass lengths including under pressure. Similar to k = 2 cluster 1, these keepers are more traditional than the other two types.

Once again, goalkeeper positioning and saving by body parts do not contribute to clustering, although sweeping positioning does.

However, these results are not robust as number of components are added, so results are not highly confident.

<a id="breakdown-of-results-by-players"></a>

### **Breakdown of results by players**

Findings and radar plots for each goalkeeper are in their own files:

- <a href="goalkeepers_Zecira_Musovic_Chelsea_FCW.md" style="color:black">Zecira Musovic - Chelsea</a>
- <a href="goalkeepers_Hannah_Hampton_Chelsea_FCW.md" style="color:black">Hannah Hampton - Chelsea</a>
- <a href="goalkeepers_Rebecca_Leigh_Spencer_Tottenham_Hotspur_Women.md" style="color:black">Rebecca Leigh Spencer - Tottenham Hotspur</a>
- <a href="goalkeepers_Mária_Korenčiová_Como_W.md" style="color:black">Maria Korenciova - Como</a>
- <a href="goalkeepers_Mary_Alexandra_Earps_Manchester_United_W.md" style="color:black">Mary Earps - Manchester United</a>

<div style="page-break-before: always; break-before: page;"></div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="appendix"></a>

## **Appendix**

<a id="radar-plots-for-2-clusters-goalkeepers-averages"></a>

### **Radar plots for 2 clusters goalkeepers' averages**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_raw.png" alt="Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 1: All Goalkeepers - Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_adj.png" alt="Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 2: All Goalkeepers - Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-goalkeepers-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_raw_FA_Womens_Super_League.png" alt="England Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 3: FA Women's Super League Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_adj_FA_Womens_Super_League.png" alt="England Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 4: FA Women's Super League Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-goalkeepers-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_raw_Frauen_Bundesliga.png" alt="Germany Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 5: Frauen Bundesliga Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_adj_Frauen_Bundesliga.png" alt="Germany Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 6: Frauen Bundesliga Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-goalkeepers-averages-liga-f"></a>

#### **Liga F**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_raw_Liga_F.png" alt="Spain Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 7: Liga F Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_adj_Liga_F.png" alt="Spain Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 8: Liga F Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-2-clusters-goalkeepers-averages-serie-a-women"></a>

#### **Serie A Women**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_raw_Serie_A_Women.png" alt="Italy Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 9: Serie A Women Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k2/all_features_adj_Serie_A_Women.png" alt="Italy Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 10: Serie A Women Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-goalkeepers-averages"></a>

### **Radar plots for 3 clusters goalkeepers' averages**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_raw.png" alt="Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 11: Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_adj.png" alt="Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 12: Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-goalkeepers-averages-fa-womens-super-league"></a>

#### **FA Women's Super League**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_raw_FA_Womens_Super_League.png" alt="England Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 13: FA Women's Super League Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_adj_FA_Womens_Super_League.png" alt="England Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 14: FA Women's Super League Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-goalkeepers-averages-frauen-bundesliga"></a>

#### **Frauen Bundesliga**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_raw_Frauen_Bundesliga.png" alt="Germany Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 15: Frauen Bundesliga Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_adj_Frauen_Bundesliga.png" alt="Germany Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 16: Frauen Bundesliga Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-goalkeepers-averages-liga-f"></a>

#### **Liga F**

<div style="page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_raw_Liga_F.png" alt="Spain Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 17: Liga F Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_adj_Liga_F.png" alt="Spain Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 18: Liga F Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>

<div align="right"><a href="#table-of-contents" style="color:black">↑ Back to table of contents</a></div>

<a id="radar-plots-for-3-clusters-goalkeepers-averages-serie-a-women"></a>

#### **Serie A Women**

<div style="page-break-inside: avoid; break-inside: avoid;">
<table border="0" style="width: 100%; border: none; border-collapse: collapse;">
<tr style="border: none; background: none;">
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_raw_Serie_A_Women.png" alt="Italy Goalkeepers Raw Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 19: Serie A Women Goalkeepers — Raw Statistics Comparison
</td>
<td align="center" valign="top" width="50%" style="border: none; padding: 0 4px 0; background: none;">
<img src="../../radar_plots/Goalkeeper/k3/all_features_adj_Serie_A_Women.png" alt="Italy Goalkeepers Adjusted Comparison" style="max-width: 100%; max-height: 10.5cm;"><br>
Figure 20: Serie A Women Goalkeepers — Adjusted Statistics Comparison
</td>
</tr>
</table>
</div>
