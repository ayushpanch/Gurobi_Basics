\ Model basic_model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  Monday_ + Tuesday_ + Wensday_ + Thursday_ + Friday_ + Saturday_ + Sunday_
Subject To
 employees_coming_on_monday: Monday_ + Thursday_ + Friday_ + Saturday_
   + Sunday_ >= 17
 employees_coming_on_tuesday: Monday_ + Tuesday_ + Friday_ + Saturday_
   + Sunday_ >= 13
 employees_coming_on_wensday: Monday_ + Tuesday_ + Wensday_ + Saturday_
   + Sunday_ >= 15
 employees_coming_on_Thursday: Monday_ + Tuesday_ + Wensday_ + Thursday_
   + Sunday_ >= 19
 employees_coming_on_Friday: Monday_ + Tuesday_ + Wensday_ + Thursday_
   + Friday_ >= 14
 employees_coming_on_Saturday: Tuesday_ + Wensday_ + Thursday_ + Friday_
   + Saturday_ >= 16
 employees_coming_on_Saturday: Wensday_ + Thursday_ + Friday_ + Saturday_
   + Sunday_ >= 11
 R7: Monday_ >= 0
 R8: Tuesday_ >= 0
 R9: Wensday_ >= 0
 R10: Thursday_ >= 0
 R11: Friday_ >= 0
 R12: Saturday_ >= 0
 R13: Sunday_ >= 0
Bounds
Generals
 Monday_ Tuesday_ Wensday_ Thursday_ Friday_ Saturday_ Sunday_
End
