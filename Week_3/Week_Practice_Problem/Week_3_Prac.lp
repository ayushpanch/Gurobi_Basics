\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2200 A + 2200 B + 2200 C + 2200 D + 2200 E + 2200 F + 2000 G
Subject To
 employees_coming_on_sunday: B + C + D + E + F >= 22
 employees_coming_on_monday: C + D + E + F + G >= 17
 employees_coming_on_Tuesday: A + D + E + F + G >= 13
 employees_coming_on_Wensday: A + B + E + F + G >= 14
 employees_coming_on_Thursday: A + B + C + F + G >= 15
 employees_coming_on_Friday: A + B + C + D + G >= 18
 employees_coming_on_Saturday: A + B + C + D + E >= 24
 R7: A >= 0
 R8: B >= 0
 R9: C >= 0
 R10: D >= 0
 R11: E >= 0
 R12: F >= 0
 R13: G >= 0
Bounds
Generals
 A B C D E F G
End
