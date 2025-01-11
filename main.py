#!/bin/bash
#**************************************************************
# Date: 080224 (Expected Solution with 34 Lines of Code)      *
# Title: Recursive Decimal to Binary                          *
# Status: In Progress (In Progress / Testing / Working)       *
#  In Exercise 78 you wrote a program that used a loop to     *
# convert a decimal number to its binary representation. In   *
# this exercise you will perform the same task using          *
# recursion. Write a recursive function that converts a       *
# non-negative decimal number to binary. Treat 0 and 1 as     *
# base cases which return a string containing the appropriate *
# digit. For all other positive integers, n, you should       *
# compute the next digit using the remainder operator and     *
# then make a recursive call to compute the digits of n//2.   *
# Finally, you should concatenate the result of the recursive *
# call (which will be a string) and the next digit (which you *
# will need to convert to a string) and return this string as *
# the result of the function. Write a main program that uses  *
# your recursive function to convert a non-negative integer   *
# entered by the user from decimal to binary. Your program    *
# should display an appropriate error message if the user     *
# enters a negative value.                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def bin_func(dec_num):
  str_bin = ""
  bin_num = ""
  if dec_num // 2 == 0:
    bin_num = str(dec_num % 2)
    str_bin += bin_num
    print("cond 1", str_bin)
    return str_bin
  else:
    bin_num += str(dec_num % 2)
    str_bin += bin_num
    print("cond 2", str_bin)
    return bin_func(dec_num // 2)
#--------------------------------------------------------------
if __name__ == "__main__":
  user_num = int(input("Enter the decimal number: "))
  print("The binary representation of %d is %s." % (user_num, bin_func(user_num)))
  print("Thank you for using this app.")
#**************************************************************