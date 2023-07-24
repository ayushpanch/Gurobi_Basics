\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  50 X + 100 Y
Subject To
 first_constraint: 7 X + 2 Y >= 28
 second_constraint: 2 X + 12 Y >= 24
 fourth_constraint: X >= 0
 fifth_constraint: X >= 0
Bounds
End
