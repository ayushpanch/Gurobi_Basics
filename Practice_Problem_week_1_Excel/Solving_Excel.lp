\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  4.3 A + 2.7 B + 2.5 C + 2.2 D + 4.5 E
Subject To
 initial_investment: A + B + C + D + E <= 10
 Government_and_Agency_Bond: B + C + D >= 4
 Government_and_Agency_Bond: B + C + D >= 4
 Avg_Quality_of_Portfolio: 0.6 A + 0.6 B - 0.4 C - 0.4 D + 3.6 E <= 0
 Years_of_maturity: 4 A + 10 B - C - 2 D - 3 E <= 0
 R5: A >= 0
 R6: B >= 0
 R7: C >= 0
 R8: D >= 0
 R9: E >= 0
Bounds
End
