\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  6 A + 5 B - 6 C1 - 4 C2
Subject To
 Drug_1_Creation: A - X1A - X2A = 0
 Drug_2_Creation: B - X1B - X2B = 0
 Chemical_1_usage: - C1 + X1A + X1B <= 0
 Chemical_2_usage: - C2 + X2A + X2B <= 0
 Drug_A_70_percent_chemical_A: - 0.7 A + X1A >= 0
 Drug_A_70_percent_chemical_B: - 0.6 B + X2B >= 0
 Drug_A_Req: A <= 40
 Drug_B_Req: B <= 30
 Chemical_A_Purchased: C1 <= 45
 Chemical_B_Purchased: C2 <= 40
Bounds
End
