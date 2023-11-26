#!/bin/bash
#**************************************************************
# Date: 111323 (Expected Solution with 41 Lines of Code)      *
# Title: Is a List already in Sorted Order?                   *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a function that determines whether or not a list of   *
# values is in sorted order (either ascending or descending). *
# The function should return True if the list is already      *
# sorted. Otherwise it should return False . Write a main     *
# program that reads a list of numbers from the user and then *
# uses your function to report whether or not the list is     *
# sorted. Make sure you consider these questions when         *
# completing this exercise: Is a list that is empty in sorted *
# order? What about a list containing one element?            *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def sorted_list(data_list):
  # Determine if the list is already sorted.
  return data_list == sorted(data_list)
#--------------------------------------------------------------
if __name__ == "__main__":
  user_in = input("Enter a list of numbers separated by commas: ")
  user_in = user_in.split(",")
  user_in = [int(x) for x in user_in]
  print("Is the list already sorted? ", sorted_list(user_in ))
  print("Thank you for using this app.")
#**************************************************************