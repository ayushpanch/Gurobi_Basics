\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  3 Staff_1_Room_1 + 2 Staff_1_Room_2 + Staff_1_Room_3 + 5 Staff_1_Room_4
   + 4 Staff_1_Room_5 + 2 Staff_2_Room_1 + 4 Staff_2_Room_2
   + 5 Staff_2_Room_3 + 3 Staff_2_Room_4 + Staff_2_Room_5
   + 5 Staff_3_Room_1 + 3 Staff_3_Room_2 + 4 Staff_3_Room_3
   + 2 Staff_3_Room_4 + Staff_3_Room_5 + 3 Staff_4_Room_1 + Staff_4_Room_2
   + 2 Staff_4_Room_3 + 5 Staff_4_Room_4 + 4 Staff_4_Room_5
   + 4 Staff_5_Room_1 + 5 Staff_5_Room_2 + 2 Staff_5_Room_3
   + Staff_5_Room_4 + 3 Staff_5_Room_5 + 2 Staff_6_Room_1 + Staff_6_Room_2
   + 4 Staff_6_Room_3 + 3 Staff_6_Room_4 + 5 Staff_6_Room_5
   + 4 Staff_7_Room_1 + 5 Staff_7_Room_2 + Staff_7_Room_3
   + 2 Staff_7_Room_4 + 3 Staff_7_Room_5 + 5 Staff_8_Room_1
   + 4 Staff_8_Room_2 + 2 Staff_8_Room_3 + 3 Staff_8_Room_4
   + Staff_8_Room_5
Subject To
 Room_1_2_staff_each: Staff_1_Room_1 + Staff_2_Room_1 + Staff_3_Room_1
   + Staff_4_Room_1 + Staff_5_Room_1 + Staff_6_Room_1 + Staff_7_Room_1
   + Staff_8_Room_1 = 2
 Room_2_2_staff_each: Staff_1_Room_2 + Staff_2_Room_2 + Staff_3_Room_2
   + Staff_4_Room_2 + Staff_5_Room_2 + Staff_6_Room_2 + Staff_7_Room_2
   + Staff_8_Room_2 = 2
 Room_3_2_staff_each: Staff_1_Room_3 + Staff_2_Room_3 + Staff_3_Room_3
   + Staff_4_Room_3 + Staff_5_Room_3 + Staff_6_Room_3 + Staff_7_Room_3
   + Staff_8_Room_3 = 2
 Room_4_1_staff_each: Staff_1_Room_4 + Staff_2_Room_4 + Staff_3_Room_4
   + Staff_4_Room_4 + Staff_5_Room_4 + Staff_6_Room_4 + Staff_7_Room_4
   + Staff_8_Room_4 = 1
 Room_5_1_staff_each: Staff_1_Room_5 + Staff_2_Room_5 + Staff_3_Room_5
   + Staff_4_Room_5 + Staff_5_Room_5 + Staff_6_Room_5 + Staff_7_Room_5
   + Staff_8_Room_5 = 1
 Staff_1_total: Staff_1_Room_1 + Staff_1_Room_2 + Staff_1_Room_3
   + Staff_1_Room_4 + Staff_1_Room_5 = 1
 Staff_2_total: Staff_2_Room_1 + Staff_2_Room_2 + Staff_2_Room_3
   + Staff_2_Room_4 + Staff_2_Room_5 = 1
 Staff_3_total: Staff_3_Room_1 + Staff_3_Room_2 + Staff_3_Room_3
   + Staff_3_Room_4 + Staff_3_Room_5 = 1
 Staff_4_total: Staff_4_Room_1 + Staff_4_Room_2 + Staff_4_Room_3
   + Staff_4_Room_4 + Staff_4_Room_5 = 1
 Staff_5_total: Staff_5_Room_1 + Staff_5_Room_2 + Staff_5_Room_3
   + Staff_5_Room_4 + Staff_5_Room_5 = 1
 Staff_6_total: Staff_6_Room_1 + Staff_6_Room_2 + Staff_6_Room_3
   + Staff_6_Room_4 + Staff_6_Room_5 = 1
 Staff_7_total: Staff_7_Room_1 + Staff_7_Room_2 + Staff_7_Room_3
   + Staff_7_Room_4 + Staff_7_Room_5 = 1
 Staff_8_total: Staff_8_Room_1 + Staff_8_Room_2 + Staff_8_Room_3
   + Staff_8_Room_4 + Staff_8_Room_5 = 1
Bounds
Binaries
 Staff_1_Room_1 Staff_1_Room_2 Staff_1_Room_3 Staff_1_Room_4 Staff_1_Room_5
 Staff_2_Room_1 Staff_2_Room_2 Staff_2_Room_3 Staff_2_Room_4 Staff_2_Room_5
 Staff_3_Room_1 Staff_3_Room_2 Staff_3_Room_3 Staff_3_Room_4 Staff_3_Room_5
 Staff_4_Room_1 Staff_4_Room_2 Staff_4_Room_3 Staff_4_Room_4 Staff_4_Room_5
 Staff_5_Room_1 Staff_5_Room_2 Staff_5_Room_3 Staff_5_Room_4 Staff_5_Room_5
 Staff_6_Room_1 Staff_6_Room_2 Staff_6_Room_3 Staff_6_Room_4 Staff_6_Room_5
 Staff_7_Room_1 Staff_7_Room_2 Staff_7_Room_3 Staff_7_Room_4 Staff_7_Room_5
 Staff_8_Room_1 Staff_8_Room_2 Staff_8_Room_3 Staff_8_Room_4 Staff_8_Room_5
End
