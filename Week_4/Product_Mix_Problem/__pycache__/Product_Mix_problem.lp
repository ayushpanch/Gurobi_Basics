\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  3 A + 3 B + 3 C + 3 D1 + 3 E1 + 2 D2 + 2 E2 - 4 M1 - 4 M2 - 4 M3
Subject To
 D1_<=20: D1 <= 20
 E1_<=20: E1 <= 20
 M1_<=128: M1 <= 128
 M2_<=128: M2 <= 128
 M3_<=128: M3 <= 128
 M1_Constraint: 12 A + 7 B + 8 C + 10 D1 + 7 E1 + 10 D2 + 7 E2 - 60 M1 = 0
 M2_Constraint: 8 A + 9 B + 4 C + 11 E1 + 11 E2 - 60 M2 = 0
 M3_Constraint: 5 A + 10 B + 7 C + 3 D1 + 2 E1 + 3 D2 + 2 E2 - 60 M3 = 0
Bounds
End
