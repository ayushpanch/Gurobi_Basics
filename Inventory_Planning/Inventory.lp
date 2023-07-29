\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  54.25 month_1 + 48.75 month_2 + 48.25 month_3 + 47.75 month_4
   - 4762.5 Constant
Subject To
 Lower_Bound_Constraint: month_1 >= 400
 Upper_Bound_Constraint: month_1 <= 500
 Lower_Bound_Constraint: month_2 >= 400
 Upper_Bound_Constraint: month_2 <= 520
 Lower_Bound_Constraint: month_3 >= 400
 Upper_Bound_Constraint: month_3 <= 450
 Lower_Bound_Constraint: month_4 >= 400
 Upper_Bound_Constraint: month_4 <= 550
 Lower_Bound_Constraint: month_1 >= 350
 Upper_Bound_Constraint: month_1 <= 430
 Lower_Bound_Constraint: month_1 + month_2 >= 930
 Upper_Bound_Constraint: month_1 + month_2 <= 1010
 Lower_Bound_Constraint: month_1 + month_2 + month_3 >= 1240
 Upper_Bound_Constraint: month_1 + month_2 + month_3 <= 1320
 Lower_Bound_Constraint: month_1 + month_2 + month_3 + month_4 >= 1780
 Upper_Bound_Constraint: month_1 + month_2 + month_3 + month_4 <= 1860
Bounds
 Constant = 1
End
