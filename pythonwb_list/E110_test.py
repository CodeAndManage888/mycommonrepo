#!/bin/bash
#**************************************************************
# Date: 102223 (Expected Solution with 35 Lines of Code)      *
# Title: Perfect Numbers                                      *
# Status: In Progress (In Progress / Testing / Working)       *
# An integer, n, is said to be perfect when the sum of all of *
# the proper divisors of n is equal to n. For example, 28 is a*
# perfect number because its proper divisors are 1, 2, 4 ,7   *
# and 14 ,and 1+2+4+7+14 = 28 . Write a function that         *
# determines whether or not a positive integer is perfect.    *
# Your function will take one parameter. If that parameter is *
# a perfect number then your function will return true.       *
# Otherwise it will return false. In addition, write a main   *
# program that uses your function to identify and display all *
# of the perfect numbers between 1 and 10,000. Import your    *
# solution to Exercise 109 when completing this task.         *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import E109
#--------------------------------------------------------------
def perfect_mun(user_int):
  prop_list = []
  prop_list = E109.prop_divisor(user_int)
  sum_prop = 0
  for i in range(len(prop_list)):
    sum_prop += prop_list[i]
  if sum_prop == user_int:
    print(user_int, "is a perfect number")
    return True
  else:
#    print(user_int, "is not a perfect number")
    return False
#--------------------------------------------------------------
if __name__ == "__main__":
  for i in range(1,1000):
    perfect_mun(i)
  print("Thank you for using this app.")
#**************************************************************
