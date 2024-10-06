#!/bin/bash
#**************************************************************
# Date: 072824 (Expected Solution with 76 Lines of Code)      *
# Title: Most Births in a given Time Period                   *
# Status: Testing (In Progress / Testing / Working)           *
#  Write a program that uses the baby names data set          *
# described in Exercise 154 to determine which names were     *
# used most often within a time period. Have the user supply  *
# the ﬁrst and last years of the range to analyze. Display    *
# the boy’s name and the girl’s name given to the most        *
# children during the indicated years.                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def common_name(file_loc, yr_range):
  boy_name_common = []
  girl_name_common = ""
  boy_name_count = 0
  girl_name_count = 0
  for year in yr_range:
    file_name = year + "f"
    file_path = f"{file_loc}/{file_name}"
    with open(file_path, "r") as file_handle:
      file_data = file_handle.readlines()
    for line_item in file_data:
      temp_name, temp_count = line_item.split(",")
      if girl_name_common == temp_name:
        girl_name_count += int(temp_count)
      elif girl_name_common != temp_name and girl_name_count < int(temp_count):
        girl_name_common = temp_name
        girl_name_count = int(temp_count)
    file_name = year + "m"
    file_path = f"{file_loc}/{file_name}"
    with open(file_path, "r") as file_handle:
      file_data = file_handle.readlines()
    for line_item in file_data:
      temp_name, temp_count = line_item.split(",")
      if boy_name_common == temp_name:
        boy_name_count += int(temp_count)
      elif boy_name_common != temp_name and boy_name_count < int(temp_count):
        boy_name_common = temp_name
        boy_name_count = int(temp_count)
  print(f"The most common boy name is {boy_name_common} with {boy_name_count} births.")
  print(f"The most common girl name is {girl_name_common} with {girl_name_count} births.")
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_location = input("Please enter the file location: ")
  year_range = input("Please enter the year range(separated by ,): ")
  year_range = year_range.split(", ")
  common_name(file_location, year_range)
  print("Thank you for using this app.")
#**************************************************************
