\ Model Avocado_Price_Allocation
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 price[Great_Lakes] + 0 price[Midsouth] + 0 price[Northeast]
   + 0 price[Northern_New_England] + 0 price[SouthCentral]
   + 0 price[Southeast] + 0 price[West] + 0 price[Plains]
Subject To
 R0: supplied_avacadoes_each_region[Great_Lakes]
   + supplied_avacadoes_each_region[Midsouth]
   + supplied_avacadoes_each_region[Northeast]
   + supplied_avacadoes_each_region[Northern_New_England]
   + supplied_avacadoes_each_region[SouthCentral]
   + supplied_avacadoes_each_region[Southeast]
   + supplied_avacadoes_each_region[West]
   + supplied_avacadoes_each_region[Plains] = 30
 R1: - supplied_avacadoes_each_region[Great_Lakes]
   + predicted_avacadoes_sold_each_region[Great_Lakes] <= 0
 R2: - supplied_avacadoes_each_region[Midsouth]
   + predicted_avacadoes_sold_each_region[Midsouth] <= 0
 R3: - supplied_avacadoes_each_region[Northeast]
   + predicted_avacadoes_sold_each_region[Northeast] <= 0
 R4: - supplied_avacadoes_each_region[Northern_New_England]
   + predicted_avacadoes_sold_each_region[Northern_New_England] <= 0
 R5: - supplied_avacadoes_each_region[SouthCentral]
   + predicted_avacadoes_sold_each_region[SouthCentral] <= 0
 R6: - supplied_avacadoes_each_region[Southeast]
   + predicted_avacadoes_sold_each_region[Southeast] <= 0
 R7: - supplied_avacadoes_each_region[West]
   + predicted_avacadoes_sold_each_region[West] <= 0
 R8: - supplied_avacadoes_each_region[Plains]
   + predicted_avacadoes_sold_each_region[Plains] <= 0
 R9: predicted_avacadoes_sold_each_region[Great_Lakes]
   - demand[Great_Lakes] <= 0
 R10: predicted_avacadoes_sold_each_region[Midsouth] - demand[Midsouth]
   <= 0
 R11: predicted_avacadoes_sold_each_region[Northeast] - demand[Northeast]
   <= 0
 R12: predicted_avacadoes_sold_each_region[Northern_New_England]
   - demand[Northern_New_England] <= 0
 R13: predicted_avacadoes_sold_each_region[SouthCentral]
   - demand[SouthCentral] <= 0
 R14: predicted_avacadoes_sold_each_region[Southeast] - demand[Southeast]
   <= 0
 R15: predicted_avacadoes_sold_each_region[West] - demand[West] <= 0
 R16: predicted_avacadoes_sold_each_region[Plains] - demand[Plains] <= 0
 R17: - supplied_avacadoes_each_region[Great_Lakes]
   + predicted_avacadoes_sold_each_region[Great_Lakes]
   + predicted_avacadoes_wasted_each_region[Great_Lakes] = 0
 R18: - supplied_avacadoes_each_region[Midsouth]
   + predicted_avacadoes_sold_each_region[Midsouth]
   + predicted_avacadoes_wasted_each_region[Midsouth] = 0
 R19: - supplied_avacadoes_each_region[Northeast]
   + predicted_avacadoes_sold_each_region[Northeast]
   + predicted_avacadoes_wasted_each_region[Northeast] = 0
 R20: - supplied_avacadoes_each_region[Northern_New_England]
   + predicted_avacadoes_sold_each_region[Northern_New_England]
   + predicted_avacadoes_wasted_each_region[Northern_New_England] = 0
 R21: - supplied_avacadoes_each_region[SouthCentral]
   + predicted_avacadoes_sold_each_region[SouthCentral]
   + predicted_avacadoes_wasted_each_region[SouthCentral] = 0
 R22: - supplied_avacadoes_each_region[Southeast]
   + predicted_avacadoes_sold_each_region[Southeast]
   + predicted_avacadoes_wasted_each_region[Southeast] = 0
 R23: - supplied_avacadoes_each_region[West]
   + predicted_avacadoes_sold_each_region[West]
   + predicted_avacadoes_wasted_each_region[West] = 0
 R24: - supplied_avacadoes_each_region[Plains]
   + predicted_avacadoes_sold_each_region[Plains]
   + predicted_avacadoes_wasted_each_region[Plains] = 0
Bounds
 0.1 <= price[Great_Lakes] <= 1.86
 0.1 <= price[Midsouth] <= 1.86
 0.1 <= price[Northeast] <= 1.86
 0.1 <= price[Northern_New_England] <= 1.86
 0.1 <= price[SouthCentral] <= 1.86
 0.1 <= price[Southeast] <= 1.86
 0.1 <= price[West] <= 1.86
 0.1 <= price[Plains] <= 1.86
 2.06357351 <= supplied_avacadoes_each_region[Great_Lakes] <= 7.09476473
 1.84544313 <= supplied_avacadoes_each_region[Midsouth] <= 6.16857161
 2.36442449 <= supplied_avacadoes_each_region[Northeast] <= 8.836406220000001
 0.2196899 <= supplied_avacadoes_each_region[Northern_New_England] <= 0.91798395
 3.68713018 <= supplied_avacadoes_each_region[SouthCentral] <= 10.32317459
 2.1977637 <= supplied_avacadoes_each_region[Southeast] <= 7.81047462
 3.26010217 <= supplied_avacadoes_each_region[West] <= 11.27474911
 1.05893809 <= supplied_avacadoes_each_region[Plains] <= 3.57549921
 demand[Great_Lakes] free
 demand[Midsouth] free
 demand[Northeast] free
 demand[Northern_New_England] free
 demand[SouthCentral] free
 demand[Southeast] free
 demand[West] free
 demand[Plains] free
End
