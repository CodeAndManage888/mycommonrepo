#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 26 Lines of Code)    *
# Title: Decimal to Binary                                    *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that converts a decimal (base 10) number to *
# binary (base 2). Read the decimal number from the user as an*
# integer and then use the division algorithm shown below to  *
# perform the conversion. When the algorithm completes, result*
# contains the binary representation of the number. Display   *
# the result, along with an appropriate message.              *
#                                                             *
# Let result be an empty string                               *
# Let q represent the number to convert                       *
# repeat                                                      *
#    Set r equal to the remainder when q is divided by 2      *
#    Convert r to a string and add it to the beginning of     *
#    result                                                   *
#    Divide q by 2, discarding any remainder, and store the   *
#    result back into q                                       *
# until q is 0                                                *
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