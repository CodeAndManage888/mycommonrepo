#!/bin/bash
#**************************************************************
# Date: 081123 (Expected Solution with 31 Lines of Code)      *
# Title: Center a String in the Terminal                      *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a function that takes a string of characters as its   *
# ﬁrst parameter, and the width of the terminal in characters *
# as its second parameter. Your function should return a new  *
# string that consists of the original string and the correct *
# number of leading spaces so that the original string will   *
# appear centered within the provided width when it is        *
# printed. Do not add any characters to the end of the        *
# string. Include a main program that demonstrates your       *
# function.                                                   *
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