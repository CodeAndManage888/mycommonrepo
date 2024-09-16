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
#-------------------------------------------------------------
def func_name(user_in):
  return
#-------------------------------------------------------------
if __name__ == "__main__":
  file_location = input("Enter file location: ")
  file_name = input("Enter file name: ")
  file_path = f"{file_location}/{file_name}"
  file_handle = open(file_path, "r")
  file_data = file_handle.read()
  print("Thank you for using this app.")
#*************************************************************