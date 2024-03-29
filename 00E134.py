#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 14 Lines of Code)      *
# Title: Unique Characters                                    *
# Status: In Progress (In Progress / Testing / Working)       *
# Create a program that determines and displays the number of *
# unique characters in a string entered by the user. For      *
# example, Hello, World! has 10 unique characters whilezzz    *
# has only one unique character. Use a dictionary or set to   *
# solve this problem.                                         *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def unique_letter(user_in):
  unique_char = set()
  for char in user_in:
    unique_char.add(char)
  return len(unique_char)
#--------------------------------------------------------------
if __name__ == "__main__":
  user_str = input("Enter a string: ")
  print("The number of unique characters in " + user_str + " is " + str(unique_letter(user_str))
  print("Thank you for using this app.")
#**************************************************************