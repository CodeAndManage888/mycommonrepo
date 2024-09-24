#!/bin/bash
#*************************************************************
# Date: 070324 (Expected Solution with 50 Lines of Code)     *
# Title: Names that Reached Number One                       *
# Status: In Progress (In Progress / Testing / Working)      *
#  The baby names data set consists of over 200 files. Each  *
# file contains a list of 100 names, along with the number of*
# times each name was used. There are two files for each     *
# year: one containing names used for girls and the other    *
# containing names used for boys. The data set includes data *
# for every year from 1900 to 2012. Write a program that     *
# reads every file in the data set and identifies all of the *
# names that were most popular in at least one year. Your    *
# program should output two lists: one containing the most   *
# popular names for boys and the other containing the most   *
# popular names for girls. Neither of your lists should      *
# include any repeated values.                               *
#                                                            *
# Computed Result Validated:                                 *
#*************************************************************
from os import write


year_list = ["2018f", "2018m", "2019f", "2019m", "2020f", 
             "2020m", "2021f", "2021m", "2022f", "2022m", 
             "2023f", "2023m"]
temp_male = ["Name", 0]
temp_female = ["Name", 0]
#-------------------------------------------------------------
def read_files(user_in):
  for file_name in year_list:
    file_path = f"{user_in}/{file_name}"
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
  return

def write_files(rec1_list, rec2_list):
  with open("boys.txt", "w") as file:
    for item in rec1_list:
      file.write(f"{item}\n")
  with open("girls.txt", "w") as file:
    for item in rec2_list:
      file.write(f"{item}\n")
  return
#-------------------------------------------------------------
if __name__ == "__main__":
  file_location = input("Enter file location: ")
  read_files(file_location)
  print("Thank you for using this app.")
#*************************************************************