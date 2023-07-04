#!/bin/bash
#**************************************************************
# Date: 051123                                                *
# Title: Even or Odd                                          *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that reads an integer from the user. Then   * 
# your program should display a message indicating whether    * 
# the inter is even or odd.                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
computed_value, icheck, iInteger, ciInteger = (0, -1, 0, 0)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Integer input data only.")
#--------------------------------------------------------------    
iInteger = input("What number is in your mind (Integer Only)?==> ")
ciInteger = data_check(iInteger)
#--------------------------------------------------------------
if icheck == 0:
  if ciInteger > 0:
    computed_value = ciInteger % 2
    if computed_value == 1:
      print("Your number is an ODD number.")
    else:
      print("Your number is an EVEN number.")
  else:
    print("Invalid input data! Greater than zero integer input data only.")
print("Thank you for using this app.")
#**************************************************************