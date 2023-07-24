\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  3 X + 2 Y
Subject To
 first_constraint: 2 X + Y <= 100
 second_constraint: X + Y <= 80
 third_constraint: X <= 40
 fourth_constraint: X >= 0
 fifth_constraint: X >= 0
Bounds
End
