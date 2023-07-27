\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  0.026 Perosnal + 0.0509 Car + 0.0864 Home + 0.068 Farm + 0.078 Commercial
Subject To
 Bank_Investment: Perosnal + Car + Home + Farm + Commercial <= 10
 Farm_and_Commercial: - 0.3 Perosnal - 0.3 Car - 0.3 Home + 0.7 Farm
   + 0.7 Commercial >= 0
 Home_Loans: - 0.4 Perosnal - 0.4 Car + 0.6 Home >= 0
 Bad_Debts: 0.06 Perosnal + 0.03 Car - 0.01 Home + 0.01 Farm
   - 0.02 Commercial <= 0
 R4: Perosnal >= 0
 R5: Car >= 0
 R6: Home >= 0
 R7: Farm >= 0
 R8: Commercial >= 0
Bounds
End
