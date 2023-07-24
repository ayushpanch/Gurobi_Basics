\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.0865 X1 + 0.0952 X2 + 0.1 X3 + 0.0875 X4 + 0.0925 X5 + 0.09 X6
Subject To
 total_invest_amount: X1 + X2 + X3 + X4 + X5 + X6 = 750000
 25percent_for_decision_variable_1: X1 <= 187500
 25percent_for_decision_variable_2: X2 <= 187500
 25percent_for_decision_variable_3: X3 <= 187500
 25percent_for_decision_variable_4: X4 <= 187500
 25percent_for_decision_variable_5: X5 <= 187500
 25percent_for_decision_variable_6: X6 <= 187500
 Long_Investment: X1 + X2 + X4 + X6 >= 375000
 High_Risk_Investment: X2 + X3 + X5 <= 262500
Bounds
End
