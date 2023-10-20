#!/bin/bash
#**************************************************************
# Date: 101723 (Expected Solution with 43 Lines of Code)      *
# Title: Remove Outliers                                      *
# Status: In Progress (In Progress / Testing / Working)       *
# When analysing data collected as part of a science          *
# experiment it may be desirable to remove the most extreme   *
# values before performing other calculations. Write a        *
# function that takes a list of values and an non-negative    *
# integer, n, as its parameters. The function should create a *
# new copy of the list with the n largest elements and the    *
# n smallest elements removed. Then it should return the new  *
# copy of the list as the function’s only result. The order   *
# of the elements in the returned list does not have to match *
# the order of the elements in the original list. Write a     *
# main program that demonstrates your function. Your function *
# should read a list of numbers from the user and remove the  *
# two largest and two smallest values from it. Display the    *
# list with the outliers removed, followed by the original    *
# list. Your program should generate an appropriate error     *
# message if the user enters less than 4 values.              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def remove_outlier(num_list):
  if len(num_list) <= 4:
    print("Input Error: Incomplete dataset")
  else:
    num_list.sort()
    num_list.pop(0)
    num_list.pop(1)
    num_list.pop(-1)
    num_list.pop(-2)
  return num_list
#--------------------------------------------------------------
if __name__ == "__main__":
  user_in = []
  user_in = input("Enter a list of numbers separated by commas: ")
  user_in = user_in.split(",")
  out_list = remove_outlier(user_in)
  print("Original Number List: %s" % user_in)
  print("Outlier Removed List: %s" % out_list)
  print("Thank you for using this app.")
#**************************************************************