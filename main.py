#!/bin/bash
#**************************************************************
# Date: 101923 (Expected Solution with 38 Lines of Code)      *
# Title: Negatives, Zeros and Positives                       *
# Status: Testing (In Progress / Testing / Working)           *
# Create a program that reads integers from the user until a  *
# blank line is entered. Once all of the integers have been   *
# read your program should display all of the negative        *
# numbers, followed by all of the zeros, followed by all of   *
# the positive numbers. Within each group the numbers should  *
# be displayed in the same order that they were entered       *
# by the user. For example, if the user enters the values 3,  *
# -4, 1, 0,-1, 0, and-2 then your program should output the   *
# values -4,-1,-2, 0, 0, 3, and 1. Your program should        *
# display each value on its own line.                         *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
# Variables
user_in_list = []
user_num = 0
#--------------------------------------------------------------
def arrange_integer(user_list):
  # Arrange the integers in the list
  ctr = 0
  user_list.sort()
  while ctr <= len(user_in_list) - 1:
    print(user_list[ctr])
    ctr += 1
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  while user_num != "":
    user_num = input("Enter a number (Negative, Zeroes and Positives): ")
    if user_num != "":
      user_in_list.append(int(user_num))
  arrange_integer(user_in_list)
  print("Thank you for using this app.")
#**************************************************************