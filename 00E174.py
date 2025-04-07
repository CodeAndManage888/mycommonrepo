#!/bin/bash
#**************************************************************
# Date: 082424 (Expected Solution with 36 Lines of Code)      *
# Title: Run-Length Encoding                                  *
# Status: In Progress (In Progress / Testing / Working)       *
#  Write a recursive function that implements the run-length  *
# compression technique described in Exercise 173. Your       *
# function will take a list or a string as its only para-     *
# meter. It should return the run-length compressed list as   *
# its only result. Include a main program that reads a string *
# from the user, compresses it, and displays the run-length   *
# encoded result. Hint: You may want to include a loop inside *
# the body of your recursive function.                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def exp_list(input_lst):
  if len(input_lst) == 0:
    return []
  if isinstance(input_lst[0], int):
    return [input_lst[1]] * input_lst[0] + exp_list(input_lst[2:])
  else:
    return [input_lst[0]] + exp_list(input_lst[1:])  
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input_lst = input("Enter a charater list: ")
  print(user_input_lst)
  in_list = [int(item.strip()) if item.strip().isdigit() else item.strip() for item in user_input_lst.split(',')]
  print(in_list)
  print("The uncompressed list is: ", exp_list(in_list))
  print("Thank you for using this app.")
#**************************************************************