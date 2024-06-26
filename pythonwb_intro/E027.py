#**************************************************************
# Date: 020323 / 020523 / 050223                              *
# Title: Body Mass Index                                      *
# Status: Working     (In Progress / Testing / Working)       *
# Write a program that computes the body mass index (BMI) of  *
# an individual. Your program should begin by reading a height*
# and weight from the user. Then it should use one of the     *
# following two formulas to compute the BMI before displaying *
# it. If you read the height in inches and the weight in      *
# pounds then body mass index is computed using the following *
# formula:                                                    *
#                          weight                             *
#                 BMI = --------------- x 703                 *
#                       height x height                       *
#                                                             *
# If you read the height in meters and the weight in kilograms*
# then body mass index is compound using this slightly simpler*
# formula:                                                    *
#                          weight                             *
#                 BMI = ---------------                       *
#                       height x height                       *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
computed_value = 0
icheck = -1
ciWeight1, ciHeight1, ciWeight2, ciHeight2 = (0, 0, 0, 0)
#--------------------------------------------------------------
def data_check(UserIn, cUserIn):
  global icheck
  try:
    cUserIn = float(UserIn)
    icheck = 0
    return UserIn, cUserIn
  except:
    print("Invalid Data Type. Please input valid data type.")
#--------------------------------------------------------------
while icheck == -1:
  print("Please use zeroes if the data is not available")
  iWeight1 = input("Please enter your weight in lbs: ")
  iWeight1, ciWeight1 = data_check(iWeight1, ciWeight1)
  iHeight1 = input("Please enter your height in inches: ")
  iHeight1, ciHeight1 = data_check(iHeight1, ciHeight1)
  if ciWeight1 == 0 and ciHeight1 == 0:
    iWeight2 = input("Please enter your weight in kg: ")
    iWeight2, ciWeight2 = data_check(iWeight2, ciWeight2)
    iHeight2 = input("Please enter your height in meter: ")
    iHeight2, ciHeight2 = data_check(iHeight2, ciHeight2)
    if ciWeight2 != 0 and ciHeight2 != 0:
      computed_value2 = (ciWeight2 / ciHeight2**2)
      fcomputed_value2 = format(computed_value2, '2f')
      final_value2 = str(fcomputed_value2)
      print("Your computed BMI using formula 2 is " + final_value2 + ".")
      break
    else:
      if ciWeight2 == 0 and ciHeight2 == 0:
        break
      else:
        print("Invalid input combination: non zeroes for both fields or all zeroes only")
  else:
    if ciWeight1 != 0 and ciHeight1 != 0:
      computed_value1 = (ciWeight1 / ciHeight1**2) * 703
      fcomputed_value1 = format(computed_value1, '2f')
      final_value1 = str(fcomputed_value1)
      print("Your computed BMI using formula 1 is " + final_value1 + ".")
      break
    else:
      print("Invalid input combination: non zeroes for both fields or all zeroes only")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# Closed Items:
# 1.) Unable to code a way to determine which formula must be used
#     depending on the input data only.
# 2.) Uable to check the value of zero to prevent division of zero
#     error.
# 3.) Code needs to be simplified. Unable to remove unnecessary
#     computation if not needed.
# 4.) Need to remove the first message of requiring to input 0 the
#     programs should be able to handle any input combination.
# 5.) When zeros are entered first computation is halted. It needs
#     to continue the process for the other units.
# 6.) When the last 2 fields were used no computation is done.
# 7.) Still can't handle invalid combination of the user input.
# 8.) Can't handle decimal point input value.
