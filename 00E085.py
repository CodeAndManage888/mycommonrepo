#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 47 Lines of Code)    *
# Title: Convert an Integer to its Ordinal Number             *
# Status: In Progress (In Progress / Testing / Working)       *
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
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************