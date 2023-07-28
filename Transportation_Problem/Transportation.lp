\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  21 Mesa_Houston + 50 Mesa_Las_Vegas + 40 Mesa_San_Diego
   + 35 Scottsdale_Houston + 30 Scottsdale_Las_Vegas
   + 22 Scottsdale_San_Diego + 55 Tuscon_Houston + 20 Tuscon_Las_Vegas
   + 25 Tuscon_San_Diego
Subject To
 Storage_capacity_in_Houston: Mesa_Houston + Scottsdale_Houston
   + Tuscon_Houston <= 200000
 Storage_capacity_in_Las_Vegas: Mesa_Las_Vegas + Scottsdale_Las_Vegas
   + Tuscon_Las_Vegas <= 600000
 Storage_capacity_in_San_Diego: Mesa_San_Diego + Scottsdale_San_Diego
   + Tuscon_San_Diego <= 225000
 Mesa_Manufacturing_plant: Mesa_Houston + Mesa_Las_Vegas + Mesa_San_Diego
   = 275000
 Scottsdale_Manufacturing_plant: Scottsdale_Houston + Scottsdale_Las_Vegas
   + Scottsdale_San_Diego = 400000
 Tuscon_Manufacturing_plant: Tuscon_Houston + Tuscon_Las_Vegas
   + Tuscon_San_Diego = 300000
 R6: Mesa_Houston >= 0
 R7: Mesa_Las_Vegas >= 0
 R8: Mesa_San_Diego >= 0
 R9: Scottsdale_Houston >= 0
 R10: Scottsdale_Las_Vegas >= 0
 R11: Scottsdale_San_Diego >= 0
 R12: Tuscon_Houston >= 0
 R13: Tuscon_Las_Vegas >= 0
 R14: Tuscon_San_Diego >= 0
Bounds
End
