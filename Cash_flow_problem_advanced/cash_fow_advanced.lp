\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  B + 1.9 D + 1.5 E + 1.08 S2
Subject To
 initial_investment: A + C + D + S0 = 100000
 criteria_DV0: A <= 75000
 criteria_DV1: B <= 75000
 criteria_DV2: C <= 75000
 criteria_DV3: D <= 75000
 criteria_DV4: E <= 75000
 at_year_1_: 0.5 A - B + 1.2 C + 1.08 S0 - S1 = 0
 at_year_2: A + 0.5 B - E + 1.08 S1 - S2 = 0
 R8: A >= 0
 R9: B >= 0
 R10: C >= 0
 R11: D >= 0
 R12: E >= 0
 R13: S0 >= 0
 R14: S1 >= 0
 R15: S2 >= 0
Bounds
End
