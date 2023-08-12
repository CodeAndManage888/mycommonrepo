#!/bin/bash
#**************************************************************
# Date: 081123 (Expected Solution with (3 Lines of Code)      *
# Title: Is it a Valid Triangle?                              *
# Status: In Progress (In Progress / Testing / Working)       *
# If you have 3 straws, possibly of differing lengths, it may *
# or may not be possible to lay them down so that they form a *
# triangle when their ends are touching. For example, if all  *
# of the straws have a length of 6 inches. then one can       *
# easily construct an equilateral triangle using them.        *
# However, if one straw is 6 inches. long, while the other    *
# two are each only 2 inches. long, then a triangle cannot be *
# formed. In general, if any one length is greater than or    *
# equal to the sum of the other two then the lengths cannot   *
# be used to form a triangle. Otherwise they can form a       *
# triangle. Write a function that determines whether or not   *
# three lengths can form a triangle. The function will take 3 *
# parameters and return a Boolean result. In addition, write  *
# a program that reads 3 lengths from the user and            *
# demonstrates the behaviour of this function.                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def check_triangle_sides(side_1st, side_2nd, side_3rd):
  comb_data = side_1st + side_2nd + side_3rd
  invalid_check = False
  try:
    conv_comb_data = int(comb_data)
  except:
    invalid_check = True
    print("Invalid input data! Numeric input data only.")
  if not invalid_check:
    sum_1st = int(side_1st) + int(side_2nd)
    sum_2nd = int(side_2nd) + int(side_3rd)
    sum_3rd = int(side_3rd) + int(side_1st)
    if int(side_3rd) > sum_1st or int(side_1st) > sum_2nd or int(side_2nd) > sum_3rd:
      valid_triangle = False
    else:
      valid_triangle = True
    if valid_triangle:
      print("Input sides are for a valid triangle!")
    else:
      print("Input sides are not for a valid triangle!")
#--------------------------------------------------------------
if __name__ == "__main__":
  side_length = input("Enter the length of each triangle sides: ")
  temp_val = side_length.split(" ")
  check_triangle_sides(temp_val[0], temp_val[1], temp_val[2])
  print("Thank you for using this app.")
#**************************************************************