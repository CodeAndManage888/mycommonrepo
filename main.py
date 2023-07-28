#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 18 Lines of Code)    *
# Title: Binary to Decimal                                    *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that converts a binary (base 2) number to   *
# decimal (base 10). Your program should begin by reading the *
# binary number from the user as a string. Then it should     *
# compute the quivalent decimal number by processing each     *
# digit in the binary number. Finally, your program should    *
# display the equivalent decimal number with an appropriate   *
# message.                                                    *
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