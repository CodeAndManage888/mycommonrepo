#!/bin/bash
#**************************************************************
# Date: 102123 (Expected Solution with 36 Lines of Code)      *
# Title: List of Proper Divisors                              *
# Status: Testing (In Progress / Testing / Working)           *
# A proper divisor of a positive integer, n, is a positive    *
# integer less than n which divides evenly into n. Write a    *
# function that computes all of the proper divisors of a      *
# positive integer. The integer will be passed to the         *
# function as its only parameter. The function will return a  *
# list containing all of the proper divisors as its only      *
# result. Complete this exercise by writing a main program    *
# that demonstrates the function by reading a value from the  *
# user and displaying the list of its proper divisors. Ensure *
# that your main program only runs when your solution has not *
# been imported into another ﬁle.                             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def prop_divisor(user_in):
  out_list = []
  for i in range(1, user_in):
    if user_in % i == 0:
      out_list.append(i)
  return out_list
#--------------------------------------------------------------
if __name__ == "__main__":
  user_int = input("Enter the number: ")
  final_list = prop_divisor(int(user_int))
  print("List of proper divisor for %s are %s." % (int(user_int), ', '.join(map(str, final_list))))
  print("Thank you for using this app.")
#**************************************************************