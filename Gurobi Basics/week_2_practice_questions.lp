\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  + 140 Constant
Subject To
 first_constraint: 0.2 X + 0.32 Y <= 0.25
 second_constraint: X + Y = 1
Bounds
 Constant = 1
End
