\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  6 X1 + 4 X2 + 6 Y1 + 8 Y2
Subject To
 first_constraint: 3 X1 + 2 X2 + 2 Y1 + 4 Y2 <= 480
 second_constraint: X1 + X2 + 2 Y1 + 3 Y2 <= 400
 third_constraint: 2 X1 + X2 + 2 Y1 + Y2 <= 400
 fifth_constraint: X1 >= 50
 sixth_constraint: X2 + Y1 >= 100
 seventh_constraint: Y2 <= 25
 eight_constraint: Y2 >= 0
 Ninth_constraint: X1 >= 0
 tenth_constraint: X2 >= 0
 Ninth_constraint: Y1 >= 0
 tenth_constraint: Y2 >= 0
Bounds
End
