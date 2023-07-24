\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  X + Y + Z - Constant
Subject To
 first_constraint: X - Y <= 4
 second_constraint: Y + Z <= 9
 third_constraint: - X + Z >= 2
Bounds
 Constant = 1
End
