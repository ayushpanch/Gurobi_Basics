\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  34 Camp_1_Base_1 + 26 Camp_1_Base_2 + 29 Camp_1_Base_3 + 31 Camp_1_Base_4
   + 42 Camp_2_Base_1 + 33 Camp_2_Base_2 + 28 Camp_2_Base_3
   + 35 Camp_2_Base_4 + 36 Camp_3_Base_1 + 29 Camp_3_Base_2
   + 32 Camp_3_Base_3 + 38 Camp_3_Base_4
Subject To
 Camp_Base_1_requirement: Camp_1_Base_1 + Camp_2_Base_1 + Camp_3_Base_1
   = 200
 Camp_Base_2_requirement: Camp_1_Base_2 + Camp_2_Base_2 + Camp_3_Base_2
   = 250
 Camp_Base_3_requirement: Camp_1_Base_3 + Camp_2_Base_3 + Camp_3_Base_3
   = 350
 Camp_Base_4_requirement: Camp_1_Base_4 + Camp_2_Base_4 + Camp_3_Base_4
   = 300
 Available_Resources_camp_1: Camp_1_Base_1 + Camp_1_Base_2 + Camp_1_Base_3
   + Camp_1_Base_4 <= 500
 Available_Resources_camp_2: Camp_2_Base_1 + Camp_2_Base_2 + Camp_2_Base_3
   + Camp_2_Base_4 <= 400
 Available_Resources_camp_3: Camp_3_Base_1 + Camp_3_Base_2 + Camp_3_Base_3
   + Camp_3_Base_4 <= 400
 R7: Camp_1_Base_1 >= 0
 R8: Camp_1_Base_2 >= 0
 R9: Camp_1_Base_3 >= 0
 R10: Camp_1_Base_4 >= 0
 R11: Camp_2_Base_1 >= 0
 R12: Camp_2_Base_2 >= 0
 R13: Camp_2_Base_3 >= 0
 R14: Camp_2_Base_4 >= 0
 R15: Camp_3_Base_1 >= 0
 R16: Camp_3_Base_2 >= 0
 R17: Camp_3_Base_3 >= 0
 R18: Camp_3_Base_4 >= 0
Bounds
End
