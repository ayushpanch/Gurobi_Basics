\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  X + Y
Subject To
 first_constraint: X + Y >= 400
 second_constraint: - X + 2 Y <= 400
 fourth_constraint: X >= 0
 fifth_constraint: Y >= 0
Bounds
End
