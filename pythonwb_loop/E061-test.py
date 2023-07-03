#!/bin/bash
#**************************************************************
# Date: 063023   (Expected Solution with 26 Lines of Code)    *
# Title: Average                                              *
# Status: Testing (In Progress / Testing / Working)           *
# In this exercise you will create a program that computes    *
# the average of a collection of values entered by the user.  *
# The user will enter 0 as a sentinel value to indicate that  *
# no further values will be provided. Your program should     *
# display an appropriate error message if the first value     *
# entered by the user is 0.                                   *
#                                                             *
# Hint: Because the 0 marks the end of the input it should    *
# not be included in the average.                             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
Processed_List = [" "]
CollectCheck, Value_Counter, Total_Value, Ave_Value = (0, 0, 0, 0.0)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
#-------------------------------------------------------------- 
iCollectValues = input("Please enter set of numeric value: ")
CollectCheck = data_check(iCollectValues.replace(" ",""))
if icheck == 0:
  Processed_List = iCollectValues.split()
  for values in Processed_List:
    if values != "0":
      Value_Counter = Value_Counter + 1
      Total_Value = Total_Value + int(values)
    else:
      Ave_Value = Total_Value / Value_Counter
      print("The average of the collection is %s." % Ave_Value)
print("Thank you for using this app.")
#**************************************************************