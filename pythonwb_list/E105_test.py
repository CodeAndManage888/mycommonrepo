#!/bin/bash
#**************************************************************
# Date: 100223 (Expected Solution with 20 Lines of Code)      *
# Title: Reverse Order                                        *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that reads integers from the user and       *
# stores them in a list. Use 0 as a sentinel value to mark    *
# the end of the input. Once all of the values have been read *
# your program should display them (except for the 0) in      *
# reverse order, with one value appearing on each line.       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
user_value = ""
user_list = []
#--------------------------------------------------------------
def reverse_func(user_in):
  user_in.reverse()
  ctr = 0
  while ctr <= len(user_in) - 1:
    print("User input order: %s is number %s." % (len(user_in) - ctr, user_in[ctr]))
    ctr += 1
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  while user_value != "0":
    user_value = input("Enter an integer: ")
    user_list.append(user_value)
  user_list.remove("0")
  reverse_func(user_list)
  print("Thank you for using this app.")
#**************************************************************