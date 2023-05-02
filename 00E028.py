#**************************************************************
# Date: 050223                                                *
# Title: Wind Chill                                           *
# Status: In Progress (In Progress / Testing / Working)       *
# When the wind blows in cold weather, the air feels even     *
# colder than it actually is because the movement of the air  *
# increase the rate of cooling for warm objects, like people. *
# This effect is known as wind chill.                         *
# In 2001, Canada, the United Kindom and the United States    *
# adopted the following formula for computing the wind chill  *
# index. Within the formula Ta is the air temperature in      *
# degrees Celsius and V is the wind speed in kilometers per   *
# hour. A similar formula with different constant values can   *
# be used with temperatures in degrees Fahrenheit and wind    *
# speeds in miles per hour.                                   *
#                                                             *
#    WCI = 13.12 + 0.6215Ta - 11.37V^0.16 + 0.3965TaV^0.16    *
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

computed_value = 0
icheck = -1
iAirTemp, iWindSpeed, ciAirTemp, ciWindSpeed = (0, 0, 0, 0)
def data_check(UserIn1,UserIn2,cUserIn1,cUserIn2,):
  try:
    cUserIn1=float(UserIn1)
    cUserIn2=float(UserIn2)
    icheck = 0
    return UserIn1, UserIn2, cUserIn1, cUserIn2
  except:
    print("Invalid input data!")

while icheck == -1:
  print("Please provide the air temperature and wind speed.")
  iAirTemp=input("Please enter the Air Temperature in *C: ")
  iWindSpeed=input("Please enter the Wind Speed in KPH: ")
  iAirTemp, iWindSpeed, ciAirTemp, ciWindSpeed = data_check(iAirTemp, iWindSpeed, ciAirTemp, ciWindSpeed)
  if ciAirTemp <= 10 or ciWindSpeed > 4.8:
    computed_value = 13.12 + 0.6215*ciAirTemp - 11.37*(ciWindSpeed**0.16) + 0.3965*ciAirTemp*(ciWindSpeed**0.16)
    fcomputed_value = format(computed_value, '2f')
    final_value = str(fcomputed_value)
    print("Your computed WCI is " + final_value + ".")
    break
  else:
    print("Invalid Data: Air Temp must be LT 10 *C or Wind Speed must be GT 4.8 KPH")
    icheck = -1
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# Open Items:
# 1.) The program will start with *C and KPH. Still need to check
#     the exact formula for WCI if the data is for *F and MPH.
# 2.) Still need to validate the final computed value.
# 
# 
