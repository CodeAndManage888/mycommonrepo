#!/bin/bash
#**************************************************************
# Date: 051024 (Expected Solution with 46 Lines of Code)      *
# Title: Remove Comments                                      *
# Status: Testing (In Progress / Testing / Working)           *
# Python uses the # character to mark the beginning of a      *
# comment. The comment ends at the end of the line containing *
# the # character. In this exercise, you will create a program*
# that removes all of the comments from a Python source file. *
# Check each line in the file to determine if a # character is*
# present. If it is then your program should remove all of    *
# the characters from the # character to the end of the line  *
# (we’ll ignore the situation where the comment character     *
# occurs inside of a string). Save the modiﬁed file using a   *
# new name that will be entered by the user. The user will    *
# also enter the name of the input file. Ensure that an        *
# appropriate error message is displayed if a problem is      *
# encountered while accessing the ﬁles.                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func_name(user_in):
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  input_files = input("Enter the name of the input and output file: ")
  input_file = input_files.split(" ")[0]
  output_file = input_files.split(" ")[1]
  try:
    with open(input_file, "r") as input_file:
      with open(output_file, "w") as output_file:
        for line in input_file:
          if "#" in line:
            line = line.split("#")[0]
          output_file.write(line)
  except:
    print("Error: File not found.")
  print("Thank you for using this app.")
#**************************************************************