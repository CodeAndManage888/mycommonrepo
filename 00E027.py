#**************************************************************
# Date: 020323                                                *
# Title: Body Mass Index                                      *
# Status: In Progress (In Progress / Testing / Working)       *
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
import math

computed_value = 0
icheck = -1
while icheck == -1:
  iWeight = input("Please enter your weight in lbs or kg: " )
  iHeight = input("Please enter your height in inches or meter: ")
  iUnits = input("Is the data in lbs/inches (Y/N)? ")
#--------------------------------------------------------------
  try:
    ciWeight = float(iWeight)
    ciHeight = float(iHeight)
    icheck = 0
    result = isinstance(iUnits,int)
    if result == True:
      print("Invalid Data Type. Please input valid data type.")
  except:
    print("Invalid Data Type. Please input valid data type.")
#--------------------------------------------------------------
if iUnits == "Y":
    computed_value = (ciWeight / ciHeight**2)*703
else:
    computed_value = (ciWeight / ciHeight**2)
 
fcomputed_value = format(computed_value, '2f')
final_value = str(fcomputed_value)
#--------------------------------------------------------------
print("Your computed BMI is", final_value,".")
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
# 1.) 
