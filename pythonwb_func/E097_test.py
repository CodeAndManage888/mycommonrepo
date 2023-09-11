#!/bin/bash
#**************************************************************
# Date: 082123 (Expected Solution with 22 Lines of Code)      *
# Title: Random Good Password                                 *
# Status: Testing (In Progress / Testing / Working)           *
# Using your solutions to Exercises 94 and 96, write a        *
# program that generates a random good password and displays  *
# it. Count and display the number of attempts that were      *
# needed before a good password was generated. Structure your *
# solution so that it imports the functions you wrote         *
# previously and then calls them from a function named main in*
# the file that you create for this exercise.                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import sys
sys.path.append('/home/runner/mycommonrepo/pythonwb_func')
import E094_test
#import E094
import E096_test
#import E096
#--------------------------------------------------------------
def main():
  gen_password = E094_test.ran_password()
  gen_pass_ctr = 1
  while E096_test.password_chk(gen_password) != 1:
    gen_pass_ctr += 1
    gen_password = E094_test.ran_password()
  print("The generated good password is", gen_password)
  print("It took %s attempts to generate the good password." % gen_pass_ctr)
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  main()
  print("Thank you for using this app.")
#**************************************************************