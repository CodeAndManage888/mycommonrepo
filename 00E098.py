#!/bin/bash
#**************************************************************
# Date: 082223 (Expected Solution with 41 Lines of Code)      *
# Title: Hexadecimal and Decimal Digits                       *
# Status: In Progress (In Progress / Testing / Working)       *
# Write two functions, hex2int and int2hex , that convert     *
# between hexadecimal digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,   *
# A, B, C, D, E and F) and base 10 integers. The hex2int      *
# function is responsible for converting a string containing  *
# a single hexadecimal digit to a base 10 integer, while      *
# the int2hex function is responsible for converting an       *
# integer between 0 and 15 to a single hexadecimal digit.     *
# Each function will take the value to convert as its only    *
# parameter and return the converted value as the function’s  *
# only result. Ensure that the hex2int function works         *
# correctly for both uppercase and lowercase letters. Your    *
# functions should end the program with a meaningful error    *
# message if an invalid parameter is provided.                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def hex2int(user_in):
  hex_ltr_dict = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, 
                  "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
  cmp_idx = len(user_in) - 1
  for char in user_in:
    int_output += 
  return
def int2hex(user_in):
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  input_data = input("Enter hexadecimal or decimal number: ")
  hex2int(input_data)
  print("Thank you for using this app.")
#**************************************************************
