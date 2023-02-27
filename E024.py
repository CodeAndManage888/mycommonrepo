#**************************************************************
# Date: 012923 / 013123                                       *
# Title: Units of Time                                        *
# Status: Testing (In Progress / Testing / Working)           *
# Create a program that reads a duration from the user as a   *
# number of days, hours, minutes, and seconds. Compute and    *
# display the total number of seconds representedby this      *
# duration.                                                   *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
import math

computed_value = 0
icheck = -1
print("Convert the input data to total seconds!")
while icheck == -1:
  iDays = input("Please provide the number of days ==> ")
  iHours = input("Please provde the number of hours ==> ")
  iMinutes = input("Please provide the number of minutes ==> ")
  iSeconds = input("Please provide the number of seconds ==> ")
  try:
    ciDays = float(iDays)
    ciHours = float(iHours)
    ciMinutes = float(iMinutes)
    ciSeconds = float(iSeconds)
    icheck = 0
  except:
    print("Please input number data only.")
#--------------------------------------------------------------
computed_value = (ciSeconds + (ciMinutes*60) + (ciHours*60*60) + (ciDays*24*60*60))
fcomputed_value = format(computed_value, '2f')
final_value = str(fcomputed_value)
#--------------------------------------------------------------
print("The converted total is", final_value, " seconds.")
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
# 1.)
