#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 47 Lines of Code)    *
# Title:                                                      *
# Status: In Progress (In Progress / Testing / Working)       *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
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