#!/bin/bash
#**************************************************************
# Date: 082523 (Expected Solution with 47 Lines of Code)      *
# Title: Reduce a Fraction to Lowest Terms                    *
# Status: Testing (In Progress / Testing / Working)           *
# Write a function that takes two positive integers that      *
# represent the numerator and denominator of a fraction as    *
# its only two parameters. The body of the function should    *
# reduce the fraction to lowest terms and then return both    *
# the numerator and denominator of the reduced fraction as    *
# its result. For example, if the parameters passed to the    *
# function are 6 and 63 then the function should return 2 and *
# 21. Include a main program that allows the user to enter a  *
# numerator and denominator. Then your program should display *
# the reduced fraction. Hint: In Exercise 75 you wrote a      *
# program for computing the greatest common divisor of two    *
# positive integers. You may ﬁnd that code useful when        *
# completing this exercise.                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
input_list = []
#--------------------------------------------------------------
def reduced_form(user_in1, user_in2):
  numerator, denominator, gcd_value, end_ind = 0, 0, 0, "N"
  gcd_value = user_in1 if user_in1 < user_in2 else user_in2
  while end_ind == "N":
    rem_val1, rem_val2 = user_in1 % gcd_value, user_in2 % gcd_value
    if rem_val1 == 0 and rem_val2 == 0:
      end_ind = "Y"
    else:
      gcd_value -= 1
  if end_ind == "Y":
    numerator, denominator = user_in1 // gcd_value, user_in2 // gcd_value
  return numerator, denominator  
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input = input("Enter the numerator and denominator: ")
  input_list = user_input.split(" ")
  out1, out2 = reduced_form(int(input_list[0]), int(input_list[1]))
  print("The reduced form of the given fraction is %s and %s" % (out1, out2))
  print("Thank you for using this app.")
#**************************************************************