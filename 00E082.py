#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 22 Lines of Code)    *
# Title: Taxi Fare                                            *
# Status: In Progress (In Progress / Testing / Working)       *
# In a particular jurisdiction, taxi fares consist of a base  *
# fare of $4.00, plus $0.25 for every 140 meters traveled.    *
# Write a function that takes the distance traveled (in       *
# kilometers) as its only parameter and returns the total     *
# fare as its only result. Write a main program that          *
# demonstrates the function.                                  *
# Hint: Taxi fares change over time. Use constants to         *
# represent the base fare and the variable portion of the     *
# fare so that the program can be updated easily when the     *
# rates increase.                                             *
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