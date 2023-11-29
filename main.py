#!/bin/bash
#**************************************************************
# Date: 111323 (Expected Solution with 49 Lines of Code)      *
# Title: Count the Elements                                   *
# Status: In Progress (In Progress / Testing / Working)       *
# Python’s standard library includes a method named count     *
# that determines how many times a speciﬁc value occurs in a  *
# list. In this exercise, you will create a new function      *
# named countRange which determines and returns the number of *
# elements within a list that are greater than or equal to    *
# some minimum value and less than some maximum value. Your   *
# function will take three parameters: the list, the minimum  *
# value and the maximum value. It will return an integer      *
# result greater than or equal to 0. Include a main program   *
# that demonstrates your function for several different       *
# lists, minimum values and maximum values. Ensure that your  *
# program works correctly for both lists of integers and      *
# lists of ﬂoating point numbers.                             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def countRange(user_lst, minVal, maxVal):
  # Count the number of elements in the list that are greater
  # than or equal to the minimum value and less than the maximum
  # value.
  count = len([x for x in user_lst if x >= minVal and x < maxVal])
  return count
#--------------------------------------------------------------
if __name__ == "__main__":
  print("Enter a list of numbers separated by commas: ", end="")
  user_in = input()
  user_in = user_in.split(",")
  user_in = [int(i) for i in user_in]
  print("Enter a minimum value: ", end="")
  min_val = int(input())
  print("Enter a maximum value: ", end="")
  max_val = int(input())
  print("The number of elements in the list that are greater than or equal to", min_val, "and less than", max_val, "is", countRange(user_in, min_val, max_val))
  print("Thank you for using this app.")
#**************************************************************