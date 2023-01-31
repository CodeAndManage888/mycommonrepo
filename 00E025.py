#**************************************************************
# Date: 01312023                                              *
# Title: Units of Time (Again)                                *
# Status: In Progress (In Progress / Testing / Working)       *
# In this exercise you will reverse the process described in  *
# the previous exercise.Develop a program that begins by      *
# reading a number of seconds from the user.Then your program *
# should display the equivalent amount of time in the form    *
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours,  *
# minutes and sec-onds respectively. The hours, minutes and   *
# seconds should all be formatted so thatthey occupy exactly  *
# two digits, with a leading 0 displayed if necessary.        *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
import math

computed_value = 0
icheck = -1
print("Convert seconds to this format DD:HH:MM:SS!")
while icheck == -1:
  iSeconds = int(input("Please provide the number of seconds ==> "))
  try:
    icheck = 0
  except:
    print("Please input number data only.")
#--------------------------------------------------------------
computed_value_days = iSeconds // 86400.00
computed_value_hours = (iSeconds % 86400) // 3600
computed_value_minutes = ((iSeconds % 86400) % 3600) // 60
computed_value_seconds = ((iSeconds % 86400) % 3600) % 60
fc_val_d = str(int(computed_value_days))
fc_val_h = str(int(computed_value_hours))
fc_val_m = str(int(computed_value_minutes))
fc_val_s = str(int(computed_value_seconds))
#--------------------------------------------------------------
print("The converted value is ",fc_val_d,":",fc_val_h,":",fc_val_m,":",fc_val_s)
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
# 1.)
