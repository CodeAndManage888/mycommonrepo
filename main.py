#!/bin/bash
#**************************************************************
# Date: 092723 (Expected Solution with 21 Lines of Code)      *
# Title: Sorted Order                                         *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that reads integers from the user and       *
# stores them in a list. Your program should continue reading *
# values until the user enters 0. Then it should display all  *
# of the values entered by the user (except for the 0) in     *
# order from smallest to largest, with one value appearing on *
# each line. Use either the sort method or the sorted         *
# function to sort the list.                                  *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
usr_entry, ctr = -1, 0
usr_ent_list = []
#--------------------------------------------------------------
def sort_func(usr_in_list):
  usr_in_list.sort()
  return usr_in_list
#--------------------------------------------------------------
if __name__ == "__main__":
  while usr_entry != 0:
    usr_entry = int(input("Enter integers to be sorted. Enter 0 to end.: "))
    if usr_entry != 0:
      usr_ent_list.append(usr_entry)
  sort_func(usr_ent_list)
  while ctr <= (len(usr_ent_list) - 1):
    print(usr_ent_list[ctr])
    ctr += 1
  print("Thank you for using this app.")
#**************************************************************