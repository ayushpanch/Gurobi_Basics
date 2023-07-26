\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.043 A + 0.027 B + 0.025 C + 0.022 D + 0.045 E
Subject To
 initial_investment: A + B + C + D + E <= 10
 Government_and_Agency_Bond: B + C + D >= 4
 Avg_Quality_of_Portfolio: 0.6 A + 0.6 B - 0.4 C - 0.4 D + 3.6 E <= 0
 Years_of_maturity: 4 A + 10 B - C - 2 D - 3 E <= 0
 R4: A >= 0
 R5: B >= 0
 R6: C >= 0
 R7: D >= 0
 R8: E >= 0
Bounds
End
