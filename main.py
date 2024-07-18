#!/bin/bash
#**************************************************************
# Date: 051124 (Expected Solution with 59 Lines of Code)      *
# Title: What’s that Element Again?                           *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that reads a file containing information    *
# about chemical elements and stores it in one or more        *
# appropriate data structures. Then your program should read  *
# and process input from the user. If the user enters an      *
# integer then your program should display the symbol and     *
# name of the element with the number of protons entered. If  *
# the user enters a string then your program should display   *
# the number of protons for the element with that name or     *
# symbol. Your program should display an appropriate error    *
# message if no element exists for the name, symbol or num-   *
# ber of protons entered. Continue to read input from the     *
# user until a blank line is entered.                         *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def read_element_info(user_data):
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  
  user_input = input("Please enter the element's name, symbol or number of proton: ")
  while user_input != "":
    if user_input.isdigit():
      print("The element's name and symbol is: ", read_element_info(user_input))
    elif user_input.isalpha():
      print("The element's number of protons is: ", read_element_info(user_input))
    else:
      print("Invalid Input!")
  print("Thank you for using this app.")
#**************************************************************