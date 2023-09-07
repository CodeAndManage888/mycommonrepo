#!/bin/bash
#**************************************************************
# Date: 081523 (Expected Solution with 27 Lines of Code)      *
# Title: Next Prime                                           *
# Status: In Progress (In Progress / Testing / Working)       *
# In this exercise you will create a function named nextPrime *
# that finds and returns the ﬁrst prime number larger than    *
# some integer, n. The value of n will be passed to the       *
# function as its only parameter. Include a main program that *
# reads an integer from the user and displays the ﬁrst prime  *
# number larger than the entered value. Import and use your   *
# solution to Exercise 92 while completing this exercise.     *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import sys
sys.path.append('/home/runner/mycommonrepo/pythonwb_func')
import E092_test
#--------------------------------------------------------------
def next_prime(user_input):
  proc_num = user_input
  found_prime = False
  while not found_prime:
    response_ind = E092_test.prime_check(proc_num)
    next_prime = proc_num
    proc_num += 1
    if response_ind == 1 and next_prime != user_input:
      found_prime = True
  print("The next prime numer for " + str(user_input) + " is " + str(next_prime))
#--------------------------------------------------------------
if __name__ == "__main__":
  ask_integer = input("Please enter the number(integer only): ")
  next_prime(int(ask_integer))
  print("Thank you for using this app.")
#**************************************************************
