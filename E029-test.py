#**************************************************************
# Date: 050423                                                *
# Title: Celsius to Fahrenheit and Kelvin                     *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that begins by reading a temperature from   *
# the user in degrees Celsius. Then your program should       *
# display the equivalent temperature in degrees Fahrenheit    *
# and degrees Kelvin. The calculations needed to convert      *
# between different units of temperature can be found on the  *
# internet:                                                   *
#         F = (9/5)*C + 32                                    *
#         K = C + 273.15                                      *
#         C = (5/9)(F - 32)                                   *
#         K = (5/9)(F - 32) + 273.15                          *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
computed_value = 0
icheck = -1
iTempCel, ciTempCel = (0,0)
#--------------------------------------------------------------
def data_check(UserIn1,cUserIn1):
  global icheck
  try:
    cUserIn1=float(UserIn1)
    icheck = 0
    return UserIn1, cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------    
while icheck == -1:
  print("Please provide the temperature in Celsuis.")
  iTempCel = input("What is the temperature in Celsuis? ==> ")
  iTempCel, ciTempCel = data_check(iTempCel, ciTempCel)
#--------------------------------------------------------------
computed_value1 = (9/5)*ciTempCel + 32
computed_value2 = ciTempCel + 273.15
#--------------------------------------------------------------
print("The temperature in Fahrenheit and Kelvin are " + str(format(computed_value1, '2f')) + 
      " and " + str(format(computed_value2, '2f')) + " degrees.")
print("Thank you for using this app.")
#**************************************************************
# Open Items:
# 1.) Why did icheck resets to 0 in E028 without declaring it 
#     as a global variable?
#
