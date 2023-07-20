\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  5 X + 4 Y + 3 Z
Subject To
 first_constraint: 0.4 X + 0.3 Y + 0.2 Z >= 500
 second_constraint: 0.4 X + 0.35 Y + 0.2 Z >= 300
 third_constraint: 0.2 X + 0.35 Y + 0.6 Z >= 300
 fifth_constraint: X <= 700
 sixth_constraint: Y <= 700
 seventh_constraint: Z <= 700
 eight_constraint: Z >= 0
 Ninth_constraint: X >= 0
 tenth_constraint: Y >= 0
Bounds
End
