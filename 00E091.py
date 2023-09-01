#!/bin/bash
#**************************************************************
# Date: 081523 (Expected Solution with 30 Lines of Code)      *
# Title: Operator Precedence                                  *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a function named precedence that returns an integer   *
# representing the precedence of a mathematical operator. A   *
# string containing the operator will be passed to the        *
# function as its only parameter. Your function should return *
# 1 for +and-, 2 for* and/, and 3 forˆ. If the string passed  *
# to the function is not one of these operators then the      *
# function should return -1. Include a main program that      *
# reads an operator from the user and either displays the     *
# operator’s precedence or an error message indicating that   *
# the input was not an operator. Your main program should     *
# only run when the ﬁle containing your solution has not been *
# imported into another program. In this exercise, along with *
# others that appear later in the book, we will use ˆto       *
# represent exponentiation. Using ˆinstead of Python’s choice *
# of **will make these exercises easier because an operator   *
# will always be a single character.                          *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def precedence(user_in):
  for idx, char in enumerate(user_in):
    valid_chk = False
    if char == "+" or char == "-":
      precedence_value = 1
      valid_chk = True
    elif char == "*" or char == "/":
      precedence_value = 2
      valid_chk = True
    elif char == "^":
      precedence_value = 3
      valid_chk = True
  if valid_chk is False:
      precedence_value = -1
  return precedence_value
#--------------------------------------------------------------
if __name__ == "__main__":
  math_equation = input("Enter the mathematical equation: ")
  print("Precedence value: " + str(precedence(math_equation)))
  print("Thank you for using this app.")
#**************************************************************