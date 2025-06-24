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
fin_list = []
#--------------------------------------------------------------
def exp_list(input_lst, flist):
  for item in input_lst:
    print("item:", item)
    if item not in flist:
      flist.append(item)
    else:
      flist.append(item)
      flist.append(flist.count(item))
  return flist
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input_lst = input("Enter a charater list: ")
  print(user_input_lst)
  in_list = [item.strip() for item in user_input_lst.split(',')] 
  print("User Input:", in_list)
  print("The compressed list is: ", exp_list(in_list, fin_list))
  print("Thank you for using this app.")