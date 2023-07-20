\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  50 X1 + 61 X2 + 83 Y1 + 97 Y2 + 130 Z1 + 145 Z2
Subject To
 first_constraint: 2 X1 + 1.5 Y1 + 3 Z1 <= 10000
 second_constraint: X1 + 2 Y1 + Z1 <= 5000
 third_constraint: X1 + X2 = 3000
 fourth_constraint: Y1 + Y2 = 2000
 fifth_constraint: Z1 + Z2 = 1000
 fifth_constraint: X1 >= 0
 sixth_constraint: X2 >= 0
 seventh_constraint: Y1 >= 0
 eight_constraint: Y2 >= 0
 Ninth_constraint: Z1 >= 0
 tenth_constraint: Z2 >= 0
Bounds
End
