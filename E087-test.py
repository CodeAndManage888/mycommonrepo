#!/bin/bash
#**************************************************************
# Date: 081123 (Expected Solution with 31 Lines of Code)      *
# Title: Center a String in the Terminal                      *
# Status: Testing (In Progress / Testing / Working)           *
# Write a function that takes a string of characters as its   *
# ﬁrst parameter, and the width of the terminal in characters *
# as its second parameter. Your function should return a new  *
# string that consists of the original string and the correct *
# number of leading spaces so that the original string will   *
# appear centered within the provided width when it is        *
# printed. Do not add any characters to the end of the        *
# string. Include a main program that demonstrates your       *
# function.                                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def text_center(str_input, terminal_length):
  invalid_flag = False
  try:
    cterminal_length = int(terminal_length)
  except:
    print("Numeric input data only for terminal length.")
    invalid_flag = True
  if not invalid_flag:
#    print("-" * cterminal_length)
    num_spaces = (cterminal_length - len(str_input) // 2)
    print("-" * num_spaces + "-" * len(str_input) + "-" * num_spaces,)
    print(" " * num_spaces + str_input + " " * num_spaces,)
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input = input("Enter the string and terminal length separating it with '|': ")
  temp_data = user_input.split("|")
  text_center(temp_data[0], temp_data[1])
  print("Thank you for using this app.")
#**************************************************************