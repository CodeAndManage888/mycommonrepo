#!/bin/bash
#**************************************************************
# Date: 071123   (Expected Solution with 17 Lines of Code)    *
# Title: Greatest Common Divisor                              *
# Status: Testing (In Progress / Testing / Working)           *
# The greatest common divisor of two positive integers, n and *
# m, is the largest number, d, which divides evenly into both *
# n and m. There are algorithms that can be used to solve     *
# this problem, including:                                    *
#                                                             *
# Initialize d to the smaller of m and n.                     *
# While d does not evenly divide m or d does not evenly       *
# divide n do                                                 *
#    Decrease the value of d by 1                             *
# Report d as the greatest common divisor of n and m          *
#                                                             *
# Write a program that reads two positive integers from the   *
# user and uses this algorithm to determine and report their  *
# greatest common divisor.                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
InNumList = []
StopInd = "N"
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
UserIn = input("Find the GCF of these 2 numbers: ")
CombValue = UserIn.replace(" ","")
cCombValue = data_check(CombValue)
if icheck == 0:
  InNumList = UserIn.split()
  if len(InNumList) == 2:
    Num1, Num2 = [int(Num) for Num in InNumList]
    if Num1 < Num2:
      gcd_value = Num1
    else:
      gcd_value = Num2
    while StopInd == "N":
      rem_val1, rem_val2 = Num1 % gcd_value, Num2 % gcd_value
      if rem_val1 == 0 and rem_val2 == 0:
        StopInd = "Y"
      else:
        gcd_value -= 1
    if StopInd == "Y":
      print("The GCF of the numbers %s and %s is %s." % (Num1, Num2, gcd_value))
  else:
    print("Invalid input data. Not enough input data.")
print("Thank you for using this app.")
#**************************************************************