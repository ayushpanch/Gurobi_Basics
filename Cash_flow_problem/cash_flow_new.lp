\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  Decision_Variables[1] + 1.9 Decision_Variables[3]
   + 1.5 Decision_Variables[4] + 1.08 Decision_Variables[7]
Subject To
 initial_investment: Decision_Variables[0] + Decision_Variables[2]
   + Decision_Variables[3] + Decision_Variables[5] = 100000
 criteria_DV0: Decision_Variables[0] <= 75000
 criteria_DV1: Decision_Variables[1] <= 75000
 criteria_DV2: Decision_Variables[2] <= 75000
 criteria_DV3: Decision_Variables[3] <= 75000
 criteria_DV4: Decision_Variables[4] <= 75000
 at_year_1_: 0.5 Decision_Variables[0] - Decision_Variables[1]
   + 1.2 Decision_Variables[2] + 1.08 Decision_Variables[5]
   - Decision_Variables[6] = 0
 at_year_2: Decision_Variables[0] + 0.5 Decision_Variables[1]
   - Decision_Variables[4] + 1.08 Decision_Variables[6]
   - Decision_Variables[7] = 0
 R8: Decision_Variables[0] >= 0
 R9: Decision_Variables[1] >= 0
 R10: Decision_Variables[2] >= 0
 R11: Decision_Variables[3] >= 0
 R12: Decision_Variables[4] >= 0
 R13: Decision_Variables[5] >= 0
 R14: Decision_Variables[6] >= 0
 R15: Decision_Variables[7] >= 0
Bounds
End
