#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 47 Lines of Code)    *
# Title: Convert an Integer to its Ordinal Number             *
# Status: Testing (In Progress / Testing / Working)           *
# Words like first, second and third are referred to as       *
# ordinal numbers. In this exercise, you will write a         *
# function that takes an integer as its only parameter and    *
# returns a string containing the appropriate English ordinal *
# number as its only result. Your function must handle the    *
# integers between 1 and 12 (inclusive). It should return an  *
# empty string if a value outside of this range is provided   *
# as a parameter. Include a main program that demonstrates    *
# your function by displaying each integer from 1 to 12 and   *
# its ordinal number. Your main program should only run when  *
# your file has not been imported into another program.       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
ordinal_dict = {1:"First", 2:"Second", 3:"Third", 4:"Fourth",
                5:"Fifth", 6:"Sixth", 7:"Seventh", 8:"Eighth", 
                9:"Ninth:", 10:"Tenth", 11:"Eleventh", 12:"Twelfth"}
NumFlag = False
#--------------------------------------------------------------
def ordinal_conv(InputVal):
  outvalue = ordinal_dict.get(InputVal, " ")
  return outvalue
#--------------------------------------------------------------
UserIn = input("What is the input number: ")
try:
  cUserIn = int(UserIn)
  NumFlag = True
except:
  print("Invalid input data! Numeric input data only.")
if NumFlag:
  ordinal_num = ordinal_conv(cUserIn)
  if ordinal_num != " ":
    print("The ordinal number equivalent of %s is %s." % (UserIn, ordinal_num))
  else:
    print("The ordinal number is not available for %s." % UserIn)
print("Thank you for using this app.")
#**************************************************************