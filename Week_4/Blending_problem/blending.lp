\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.25 Feed_1 + 0.3 Feed_2 + 0.32 Feed_3 + 0.15 Feed_4
Subject To
 total_demand: Feed_1 + Feed_2 + Feed_3 + Feed_4 = 8000
 grains_Constraint: 0.1 Feed_1 + 0.3 Feed_2 + 0.15 Feed_3 + 0.1 Feed_4
   >= 1200
 corn_Constraint: 0.3 Feed_1 + 0.05 Feed_2 + 0.2 Feed_3 + 0.1 Feed_4
   >= 1600
 mineral_Constraint: 0.2 Feed_1 + 0.2 Feed_2 + 0.2 Feed_3 + 0.3 Feed_4
   >= 1200
Bounds
End
