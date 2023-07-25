\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.0865 Decsion_Variables + 0.0952 Decsion_Variables
   + 0.1 Decsion_Variables + 0.0875 Decsion_Variables
   + 0.0925 Decsion_Variables + 0.09 Decsion_Variables
Subject To
 total_invest_amount: Decsion_Variables + Decsion_Variables
   + Decsion_Variables + Decsion_Variables + Decsion_Variables
   + Decsion_Variables = 750000
 R1: Decsion_Variables <= 187500
 R2: Decsion_Variables <= 187500
 R3: Decsion_Variables <= 187500
 R4: Decsion_Variables <= 187500
 R5: Decsion_Variables <= 187500
 R6: Decsion_Variables <= 187500
 Long_Investment: Decsion_Variables + Decsion_Variables + Decsion_Variables
   + Decsion_Variables >= 375000
 High_Risk_Investment: Decsion_Variables + Decsion_Variables
   + Decsion_Variables <= 262500
Bounds
 Decsion_Variables >= 1
 Decsion_Variables >= 2
 Decsion_Variables >= 3
 Decsion_Variables >= 4
 Decsion_Variables >= 5
 Decsion_Variables >= 6
End
