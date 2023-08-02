#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 42 Lines of Code)    *
# Title: Median of Three Values                               *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a functions that takes three numbers as parameters,   *
# and returns the median value of theose parameters as its    *
# result. Include a main program that reads three values from *
# the user and displays their median.                         *
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