#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 23 Lines of Code)    *
# Title: Compute the Hypotenuse                               *
# Write a function that takes the lengths of the two shorter  *
# sides of a right triangle as its parameters. Return the     *
# hypotenuse of the triangle, computed using Pythagorean      *
# theorem, as the function's result. Include a main program   *
# that reads the lengths of the shorter sides of a right      *
# triangle from the user, uses your function to compute the   *
# length of the hypotenuse, and displays the result.          *
# Status: In Progress (In Progress / Testing / Working)       *
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
UserNum = input("Enter the 2 short side of the triangle: ")


print("Thank you for using this app.")
#**************************************************************