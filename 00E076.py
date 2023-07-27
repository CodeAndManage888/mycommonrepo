#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 27 Lines of Code)    *
# Title: Prime Factors                                        *
# Status: In Progress (In Progress / Testing / Working)       *
# The prime factorization of an integer, n, can be determined *
# using the following steps:                                  *
#                                                             *
# Initialize factor to two                                    *
# While factor is less than or equal to n do                  *
#   If n is evenly divisible by factor then                   *
#      Conclude that factor is a factor of n                  *
#      Divide n by factor using integer division              *
#   Else                                                      *
#      Increase factor by one                                 *
# Write a program that reads an integer from the user. If the *
# value entered by the user is less than 2 then your program  *
# should display an appropriate error message. Otherwise your *
# program should display the prime numbers that can be        *
# multiplied together to compute n, with one factor appearin  *
# on each line. For example:                                  *
#                                                             *
# Enter an integer (2 or greater): 72                         *
# The prime factors of 72 are: 2 2 2 3 3                      *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************