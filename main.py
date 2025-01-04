#!/bin/bash
#**************************************************************
# Date: 073024 (Expected Solution with 24 Lines of Code)      *
# Title: Greatest Common Divisor                              *
# Status: In Progress (In Progress / Testing / Working)       *
#  Euclid was a Greek mathematician who lived approximately   *
# 2,300 years ago. His algorithm for computing the greatest   *
# common divisor of two positive integers, a and b, is both   *
# efﬁcient and recursive. It is outlined below: If b is 0 then*
# Return a Else Set c equal to the remainder when a is divided*
# by b Return the greatest common divisor of b and c. Write a *
# program that implements Euclid’s algorithm and uses it to   *
# determine the greatest common divisor of two integers       *
# entered by the user.                                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def GCD(num1, num2):
  if num2 == 0:
    return num1
  else:
    return GCD(num2, num1 % num2)
#--------------------------------------------------------------
if __name__ == "__main__":
  user_num1 = int(input("Enter the 1st number: "))
  user_num2 = int(input("Enter the 2nd number: "))
  print("The GCD of %d and %d is %d." % (user_num1, user_num2, GCD(user_num1, user_num2)))

  print("Thank you for using this app.")
#**************************************************************