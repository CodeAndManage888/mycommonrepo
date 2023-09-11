#!/bin/bash
#**************************************************************
# Date: 081523 (Expected Solution with 28 Lines of Code)      *
# Title: Is a Number Prime?                                   *
# Status: Testing (In Progress / Testing / Working)           *
# A prime number is an integer greater than 1 that is only    *
# divisible by one and itself. Write a function that          *
# determines whether or not its parameter is prime, returning *
# True if it is, and False otherwise. Write a main program    *
# that reads an integer from the user and displays a message  *
# indicating whether or not it is prime. Ensure that the main *
# program will not run if the ﬁle containing your solution is *
# imported into another program.                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def prime_check(user_input):
  prime_factor_list = []
  factor = 2
  while factor <= user_input:
    remainder = user_input % factor
    if remainder == 0:
      prime_factor_list.append(factor)
      user_input = user_input // factor
    else:
      factor += 1
  if len(prime_factor_list) == 1:
    prime_flag = 1
  else:
    prime_flag = 0
  return prime_flag
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input = input("Please enter the number(integer only): ")
  if prime_check(int(user_input)) == 1:
    print("The number is a prime number.")
  else:
    print("The number is NOT a prime number.")
  print("Thank you for using this app.")
#**************************************************************