#!/bin/bash
#**************************************************************
# Date: 071023   (Expected Solution with 14 Lines of Code)    *
# Title: Square Root                                          *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that implements Newton's method to compute  *
# and display the square root of a number entered by the user.*
# The algorithm for Newton's method follows:                  *
#                                                             *
# Read x from the user                                        *
# Initialize guess to x/2                                     *
# While guess is not good enough do                           *
#    Update guess to be the average of guess and x/guess      *
#                                                             *
# When this algorithm completes, guess contains an            *
# approximation of the square root. The quality of the        *
# appoximation depends on how you define "good enough". In    *
# the author's solution, guess was considered good enough     *
# when the absolute value of the difference between guess *   *
# guess and x was less than or equal to 10^-12.               *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
CompInd, GuessOne = ("N", 1.000000000000)
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
UserNum = input("Enter a number: ")
cUserNum = data_check(UserNum)
if icheck == 0:
  while CompInd == "N":
    GuessTwo = (GuessOne + cUserNum/GuessOne) / 2
    GuessDiff = GuessTwo - GuessOne
    if GuessDiff == 0.000000000000:
      print(GuessDiff, GuessOne, GuessTwo)
      CompInd = "Y"
      print("The square root of %s is %s" % (cUserNum, GuessTwo))
    else:
      GuessOne = GuessTwo
print("Thank you for using this app.")
#**************************************************************