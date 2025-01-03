#!/bin/bash
#**************************************************************
# Date: 073024 (Expected Solution with 28 Lines of Code)      *
# Title: Total the Values                                     *
# Status: In Progress (In Progress / Testing / Working)       *
#  Write a program that reads values from the user until a    *
# blank line is entered. Display the total of all of the      *
# values entered by the user (or 0.0 if the first value       *
# entered is a blank line). Complete this task using          *
# recursion. Your program may not use any loops. Hint: The    *
# body of your recursive function will need to read one value *
# from the user, and then determine whether or not to make a  *
# recursive call. Your function does not need to take any     *
# parameters, but it will need to return a numeric result.    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def recur():
  user_value = input("Please enter the data value: ")
  if user_value == "":
    return 0.0
  else:
    return float(user_value) + recur()
#--------------------------------------------------------------
if __name__ == "__main__":
  user_val1 = input("Please enter the 1st number: ")
  user_val2 = input("Please enter the 2nd number: ")
  print(recur())
  print("Thank you for using this app.")
#**************************************************************