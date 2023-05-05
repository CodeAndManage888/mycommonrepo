#**************************************************************
# Date: 050223                                                *
# Title: Wind Chill                                           *
# Status: Testing (In Progress / Testing / Working)           *
# When the wind blows in cold weather, the air feels even     *
# colder than it actually is because the movement of the air  *
# increase the rate of cooling for warm objects, like people. *
# This effect is known as wind chill.                         *
# In 2001, Canada, the United Kindom and the United States    *
# adopted the following formula for computing the wind chill  *
# index. Within the formula Ta is the air temperature in      *
# degrees Celsius and V is the wind speed in kilometers per   *
# hour. A similar formula with different constant values can  *
# be used with temperatures in degrees Fahrenheit and wind    *
# speeds in miles per hour.                                   *
#                                                             *
#    WCI = 13.12 + 0.6215Ta - 11.37V^0.16 + 0.3965TaV^0.16    *
#    WCI = 35.74 + 0.6215Ta * (0.4275Ta - 35.75) * V^0.16     *
#                                                             *
# Write a program that begins by reading the air temperature  *
# and wind speed from the user. Once these values have been   *
# read your program should display the wind chill index       *
# rounded to the closest integer.                             *
#                                                             *
# The wind chill index is only considered valid for           *
# temperatures less than or equal to 10 degrees Celsius and   *
# wind speeds excceding 4.8 kilometers per hour               *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
import math
#--------------------------------------------------------------
computed_value = 0
icheck = -1
iAirTemp, iWindSpeed, ciAirTemp, ciWindSpeed, iOptionData = (0, 0, 0, 0, "X")
myInOptList = ["Y", "N", "y", "n"]
myYesList = ["Y", "y"]
#--------------------------------------------------------------
def data_check(UserIn1,UserIn2,cUserIn1,cUserIn2):
  try:
    cUserIn1=float(UserIn1)
    cUserIn2=float(UserIn2)
    icheck = 0
    return UserIn1, UserIn2, cUserIn1, cUserIn2
  except:
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------    
while icheck == -1:
  print("Please provide the air temperature and wind speed (*C/KPH or *F/MPH).")
  iAirTemp=input("Please enter the Air Temperature: ")
  iWindSpeed=input("Please enter the Wind Speed: ")
  iAirTemp, iWindSpeed, ciAirTemp, ciWindSpeed = data_check(iAirTemp, iWindSpeed, ciAirTemp, ciWindSpeed)
  iOptionData=input("Are the input data in *C & KPH (Y or N only): ")
  print("Data fetched from the file==>", iAirTemp, iWindSpeed, iOptionData, ciAirTemp, ciWindSpeed)
#--------------------------------------------------------------
  if iOptionData not in myInOptList:
    print("Invalid Option! Try again please")
    icheck = -1
    continue
#--------------------------------------------------------------
  if iOptionData in myYesList:
    if ciAirTemp <= 10 and ciWindSpeed > 4.8:
      computed_value = 13.12 + 0.6215*ciAirTemp - 11.37*(ciWindSpeed**0.16) + 0.3965*ciAirTemp*(ciWindSpeed**0.16)
      rounded_value = round(computed_value, 4)
      fcomputed_value = format(rounded_value, '4f')
      final_value = str(fcomputed_value)
      print("Your computed WCI is " + final_value + ".")
      break
    else:
      print("Invalid Data: Air Temp must be LET 10 *C or Wind Speed must be GT 4.8 KPH.")
  else:
    if ciAirTemp <= 50.0 and ciWindSpeed > 2.98:
      computed_value = 35.74 + (0.6215*ciAirTemp) * ((0.4275*ciAirTemp) - 35.75) * (ciWindSpeed**0.16)
      rounded_value = round(computed_value, 4)
      fcomputed_value = format(rounded_value, '4f')
      final_value = str(fcomputed_value)
      print("Your computed WCI is " + final_value + ".")
      break
    else:
      print("Invalid Data: Air Temp must be LET 50 *F or Wind Speed must be GT 2.98 MPH.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# Open Items:
# 1.) The program will start with *C and KPH. Still need to check
#     the exact formula for WCI if the data is for *F and MPH.
# 2.) Still need to validate the final computed value.
#     The following formula is for *F & MPH:
#     WCI = 35.74 + 0.6215Ta * (0.4275Ta - 35.75) * V^0.16
# 3.) Validation of of the input data in terms of accepted value 
#     is erratic. This needs to be tested further. 
# C0505231400:
# - remove the icheck = -1 after ever error message
# - set the format to 4 decimal place with round syntax
# - remove test print line of codes
# - remove all new line for all messages
# - remove the math import syntax
# - fix the data value validation "or" instead of "and"