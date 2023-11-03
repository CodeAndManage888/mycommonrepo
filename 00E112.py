#!/bin/bash
#**************************************************************
# Date: 103023 (Expected Solution with 44 Lines of Code)      *
# Title: Below and Above Average                              *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that reads numbers from the user until a    *
# blank line is entered. Your program should display the      *
# average of all of the values entered by the user. Then the  *
# program should display all of the below average values,     *
# followed by all of the average values (if any), followed by *
# all of the above average values. An appropriate label       *
# should be displayed before each list of values.             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
user_num = ""
user_int_list = []
input_ave = 0
first_list = []
middle_list = []
last_list = []

#--------------------------------------------------------------
def average_func(num_list):
  above_list = []
  below_list = []
  equal_list = []
  ave_val = num_list.sum() / len(num_list)
  for num in num_list:
    if num < ave_val:
      below_list.append(num)
    elif num > ave_val:
      above_list.append(num)
    else:
      equal_list.append(num)
  return ave_val, below_list, equal_list, above_list
#--------------------------------------------------------------
if __name__ == "__main__":
  while user_num != " ":
    user_num = input("Enter a number: ")
    user_int_list.append(int(user_num))
  input_ave, first_list, middle_list, last_list = average_func(user_int_list)
  print("Average:", input_ave)
  print("Below Average: %s" % ', '.join(map(first_list)))
  print("Equal to Average: %s" % ', '.join(map(middle_list)))
  print("Above Average: %s" % ', '.join(map(last_list)))
  print("Thank you for using this app.")
#**************************************************************
