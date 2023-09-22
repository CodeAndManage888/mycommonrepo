#!/bin/bash
#**************************************************************
# Date: 082223 (Expected Solution with 41 Lines of Code)      *
# Title: Hexadecimal and Decimal Digits                       *
# Status: Testing (In Progress / Testing / Working)           *
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
def hex2int(user_in):
  hex_ltr_dict = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, 
                  "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
  num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  int_output = 0
  for idx, char in enumerate(reversed(user_in)):
    if char not in num_list:
      int_output += hex_ltr_dict[char] * 16**idx
    else:
      int_output += int(char) * 16**idx
  return int_output
def int2hex(user_in):
  int_ltr_dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
  fin_nums = []
  fin_out = ""
  int_num = int(user_in)
  while int_num // 16 >= 0:
    remainder = int_num % 16
    if remainder > 9:
      fin_nums.append(int_ltr_dict[remainder])
    else:
      fin_nums.append(str(remainder))
    int_num = int_num // 16
    if int_num == 0:
      fin_nums.reverse()
      for item in fin_nums:
        fin_out += item
      break
  return fin_out
#--------------------------------------------------------------
if __name__ == "__main__":
  input_data = input("Enter hexadecimal or decimal number and put H or D at the start:")
  if input_data[0:1] == "H" or input_data[0:1] == "h":
    func_in = input_data[1:len(input_data)]
    print("The equivalent integer for", func_in, "is", hex2int(func_in))
  elif input_data[0:1] == "D" or input_data[0:1] == "d":
    func_in = input_data[1:len(input_data)]
    print("The equivalent hexadecimal for", func_in, "is", int2hex(func_in))
  print("Thank you for using this app.")
#**************************************************************