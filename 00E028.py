#**************************************************************
# Date: 050223                                                *
# Title: Wind Chill                                           *
# Status: In Progress (In Progress / Testing / Working)       *
# When the wind blows in cold weather, the air feels even     *
# colder thatn it actually is because the movement of the air *
# increase the rate of coolin for warm objects, like people.  *
# This effect is known as wind chill.                         *
# In 2001, Canada, the United Kindom and the United States    *
# adopted the following formula for computing the wind chill  *
# index. Within the formula Ta is the air temperature in      *
# degrees Celsius and V is the wind speed in kilometers per   *
# hour. A similar fomula with different constant values can   *
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

while icheck == -1:

#--------------------------------------------------------------



#--------------------------------------------------------------



#--------------------------------------------------------------


while icheck == -1:
  iLength = input("What is the length of the sides? ==> ")
  iSides = input("How many sides does the polygon have? ==> ")
  try:
    ciLength = float(iLength)
    ciSides = float(iSides)
    icheck = 0
  except:
    print("Please input number data only.")

computed_value = (ciSides * ciLength**2) / (4 * math.tan(math.pi/ciSides))
fcomputed_value = format(computed_value, '2f')
final_value = str(fcomputed_value)

print("The area of the polygon is", final_value, "sq. units.")
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
# 
# 
