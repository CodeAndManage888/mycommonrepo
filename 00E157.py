#!/bin/bash
#**************************************************************
# Date: 072824 (Expected Solution with 41 Lines of Code)      *
# Title: Distinct Names                                       *
# Status: In Progress (In Progress / Testing / Working)       *
#  In this exercise, you will create a program that reads     *
# every file in the baby names data set described in Exercise *
# 154. As your program reads the files, it should keep track  *
# of each name used for a boy and each name used for a girl.  *
# Your program should output two lists. One list will         *
# contain all of the names that have been used for girls. The *
# other list will contain all of the names that have been     *
# used for boys. Neither of your lists should contain any     *
# repeated values.                                            *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import os
male_names = []
#--------------------------------------------------------------
def list_down_names(file_loc, user_files):
  for rawfile in user_files:
    file_path = f"{file_loc}/{rawfile}"
    print(file_path)
    with open(file_path, "r") as file_handle:
      file_data = file_handle.readlines()
    for line_item in file_data:
      temp_name, temp_count = line_item.split(",")
      #print(temp_name)
      if temp_name not in male_names:
        male_names.append(temp_name)
    print(male_names)
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_location = input("Please enter the file location: ")
  file_list = os.listdir(file_location)
  print(file_list)
  list_down_names(file_location, file_list)
  print("Thank you for using this app.")
#**************************************************************