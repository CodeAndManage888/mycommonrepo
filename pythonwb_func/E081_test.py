#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 23 Lines of Code)    *
# Title: Compute the Hypotenuse                               *
# Status: Testing (In Progress / Testing / Working)           *
# Write a function that takes the lengths of the two shorter  *
# sides of a right triangle as its parameters. Return the     *
# hypotenuse of the triangle, computed using Pythagorean      *
# theorem, as the function's result. Include a main program   *
# that reads the lengths of the shorter sides of a right      *
# triangle from the user, uses your function to compute the   *
# length of the hypotenuse, and displays the result.          *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import math
#--------------------------------------------------------------
Input_List = []
#--------------------------------------------------------------
def cal_long_side(UserIn1, UserIn2):
#  return (UserIn1**2 + UserIn2**2)**.5
  return math.sqrt(UserIn1**2 + UserIn2**2)
#--------------------------------------------------------------
UserNum = input("Enter the 2 short side of the triangle: ")
try:
  cUserNum = int(UserNum.replace(" ", ""))
  icheck = 0
except:
  icheck = -1
  print("Invalid input data! Numeric input data only.")
if icheck != -1:
  Input_List = UserNum.split()
  if len(Input_List) == 2:
    OutPrint = cal_long_side(int(Input_List[0]), int(Input_List[1]))
    print("The hypotenuse of the triangle is", format(OutPrint,"0.2f"))
  else:
    print("Invalid input data! Incomplete input data.")
print("Thank you for using this app.")
#**************************************************************