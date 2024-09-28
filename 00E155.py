#!/bin/bash
#*************************************************************
# Date: 072824 (Expected Solution with 56 Lines of Code)     *
# Title: Gender Neutral Names                                *
# Status: In Progress (In Progress / Testing / Working)      *
#  Some names, like Ben and Jonathan, are normally only used *
# for boys while names like Rebbecca and Flora are normally  *
# only used for girls. Other names, like Chris and Alex, may *
# be used for both boys and girls. Write a program that      *
# determines and displays all of the baby names that were    *
# used for both boys and girls in a year speciﬁed by the     *
# user. Your program should generate an appropriate message  *
# if there were no gender neutral names in the selected year.*
# Display an appropriate error message if you do not have    *
# data for the year requested by the user. Additional details*
# about the baby names data set are included in Exercise 154.*
#                                                            *
# Computed Result Validated:                                 *
#*************************************************************
input_list = []
#--------------------------------------------------------------
def read_files(user_in1, user_in2):
  input_list.append(user_in2+"f")
  input_list.append(user_in2+"m")
  file_name = 
  for file_name in input_list:
    file_path = f"{user_in1}/{file_name}"
    with open(file_path, "r") as file_handle:
      file_data = file_handle.readlines()
    for line_item in file_data:
      temp_name, temp_count = line_item.split(",")
      temp_count = int(temp_count)
      if file_name.endswith("f") and temp_female[-1] < temp_count and temp_name != temp_female[-2]:
        if temp_female[-1] == 0:
          temp_female[0] = temp_name
          temp_female[1] = temp_count
        else:
          temp_female.append(temp_name)
          temp_female.append(temp_count)        
      elif file_name.endswith("m") and temp_male[-1] < temp_count and temp_name != temp_male[-2]:
        if temp_male[-1] == 0:
          temp_male[0] = temp_name
          temp_male[1] = temp_count
        else:
          temp_male.append(temp_name)
          temp_male.append(temp_count)
  print("Record: ", temp_male, temp_female)
  write_files(temp_male, temp_female)
  #github connection was not working. This is a comment that Replit is not connected.
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_location = input("Enter file location: ")
  target_year = input("Enter target year: ")
  read_files(file_location, target_year)
  print("Thank you for using this app.")
#**************************************************************
