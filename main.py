#!/bin/bash
#**************************************************************
# Date: 072924 (Expected Solution with 44 Lines of Code)      *
# Title: Missing Comments                                     *
# Status: In Progress (In Progress / Testing / Working)       *
#  When one writes a function, it is generally a good idea to *
# include a comment that outlines the function’s purpose, its *
# parameters and its return value. However, sometimes         *
# comments are forgotten, or left out by well-intentioned     *
# programmers that plan to write them later but then never    *
# get around to it. Create a python program that reads one or *
# more Python source files and identifies functions that are  *
# not immediately preceded by a comment. For the purposes of  *
# this exercise, assume that any line that begins with def,   *
# followed by a space, is the beginning of a function         *
# definition. Assume that the comment character, will be the  *
# first character on the previous line when the function has  *
# a comment. Display the names of all of the functions that   *
# are missing comments, along with the file name and line     *
# number where the function deﬁnition is located. The user    *
# will provide the names of one or more Python files as       *
# command line parameters. If your program encounters a file  *
# that doesn’t exist or can’t be opened then it should display*
# an appropriate error message before moving on and processing*
# the remaining files.                                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func_chck(file_input):
  with open(file_input, "r") as f:
    file_data = f.readlines()

  for line in file_data:
    print(line)
    if line.startswith("def"):
      print("Function Found")

  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_loc = input(str("Please enter the file location: "))
  file_name = input(str("Please enter the file name: "))
  func_chck(file_loc + "/" + file_name)
  print("Thank you for using this app.")
#**************************************************************