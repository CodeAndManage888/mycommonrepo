#!/bin/bash
#**************************************************************
# Date: 080123                                                *
# Title: List of Common User Functions                        *
# Status: In Progress (In Progress / Testing / Working)       *
# a.) Integer Check - accepts 1 string input data and checks  *
#     if it is numeric.                                       *
# Computed Result Validated:                                  *
#**************************************************************
def int_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------