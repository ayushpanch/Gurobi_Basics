\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  29 X0 + 25 X1 + 21 X2 + 17 X3 + 12 X4 + 9 X5 - 21 Y0 - 17 Y1 - 13 Y2
   - 9 Y3 - 5 Y4 - Y5 - 6520 Constant
Subject To
 month_1_constraint: X0 - Y0 >= -20
 month_2_constraint: X0 + X1 - Y0 - Y1 >= 90
 month_3_constraint: X0 + X1 + X2 - Y0 - Y1 - Y2 >= 205
 month_4_constraint: X0 + X1 + X2 + X3 - Y0 - Y1 - Y2 - Y3 >= 345
 month_5_constraint: X0 + X1 + X2 + X3 + X4 - Y0 - Y1 - Y2 - Y3 - Y4
   >= 455
 month_6_constraint: X0 + X1 + X2 + X3 + X4 + X5 - Y0 - Y1 - Y2 - Y3 - Y4
   - Y5 >= 655
 R6: X0 >= 0
 R7: X1 >= 0
 R8: X2 >= 0
 R9: X3 >= 0
 R10: X4 >= 0
 R11: X5 >= 0
 R12: Y0 >= 0
 R13: Y1 >= 0
 R14: Y2 >= 0
 R15: Y3 >= 0
 R16: Y4 >= 0
 R17: Y5 >= 0
Bounds
 Constant = 1
End
