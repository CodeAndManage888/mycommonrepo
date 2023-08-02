#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 23 Lines of Code)    *
# Title: Shipping Calculator                                  *
# Status: In Progress (In Progress / Testing / Working)       *
# An online retailer provides express shipping for many of    *
# its items at a rate of $10.95 for the first item, and $2.95 *
# for each subsequent item. Write a function that takes the   *
# number of items in the order as its only parameter. Return  *
# the shipping charge for the order as the function's result. *
# Include a main program that reads the number of items       *
# purchased from the user and displays the shipping charge.   *
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