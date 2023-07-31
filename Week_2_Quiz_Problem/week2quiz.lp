\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  400 S1 + 600 S2 + 150 IC1 + 150 IT1 + 150 IC2 + 150 IT2
Subject To
 Production_capcacity_constraints_part_1: C1 + T1 <= 1000
 Production_capcacity_constraints_part_2: C2 + T2 <= 1000
 Steel_usage_constraints_part_1: C1 + 2 T1 - S1 = 0
 Steel_usage_constraints_part_2: C2 + 2 T2 - S2 = 0
 Material_balence__car_month_1: C1 - IC1 = 600
 Material_balence_truck_month_1: T1 - IT1 = 300
 Material_balence_car_month_2: C2 + IC1 - IC2 = 300
 Material_balence_Truck_month_2: T2 + IT1 - IT2 = 300
 fuel_eff_part_1: 4 C1 + 6 T1 >= 0
 fuel_eff_part_2: 4 C2 + 6 T2 >= 0
 fuel_eff_part_2: S1 >= 0
 fuel_eff_part_2: S2 >= 0
Bounds
End
