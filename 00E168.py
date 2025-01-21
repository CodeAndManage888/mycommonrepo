#!/bin/bash
#**************************************************************
# Date: 080324 (Expected Solution with 20 Lines of Code)      *
# Title: Recursive Square Root                                *
# Status: In Progress (In Progress / Testing / Working)       *
#  Exercise 71 explored how iteration can be used to compute  *
# the square root of a number. In that exercise a better      *
# approximation of the square root was generated with each    *
# additional iteration of a loop. In this exercise you will   *
# use the same approximation strategy, but you will use       *
# recursion instead of iteration. Create a square root        *
# function that takes two parameters. The first parameter, n, *
# will be the number for which the square root is being       *
# computed. The second parameter, guess , will be the current *
# guess for the square root. The guess parameter should have  *
# a default value of 1.0. Do not provide a default value for  *
# the first parameter. Your square root function will be      *
# recursive. The base case occurs when guess 2 is within      *
# 10−12 of n. In this case your function should return guess  *
# because it is close enough to the square root of n.         *
# Otherwise your function should return the result of calling *
# itself recursively with n as the first parameter and guess  *
# +n guess 2 as the second parameter. Write a main program    *
# that demonstrate your square root function by computing the *
# square root of several different values. When you call your *
# square root function from the main program you should only  *
# pass one parameter to it so that the default value for      *
# guess is used.                                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
GuessOne = 1.000000000000
#--------------------------------------------------------------
def sqr_root(data_in, GOne):
  GuessTwo = (GOne + data_in/GOne) / 2
  GuessDiff = GuessTwo - GOne
  if GuessDiff == 0.000000000000:
    return GuessTwo
  else:
    GOne = GuessTwo
    sqr_root(GuessTwo, GOne)
#--------------------------------------------------------------
if __name__ == "__main__":
  user_in = input("Enter a number: ")
  c_user_in = int(user_in)
  print("The square root of %s is %s" % (c_user_in, sqr_root(c_user_in, GuessOne)))
  print("Thank you for using this app.")
#**************************************************************
