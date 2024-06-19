#!/bin/bash
#**************************************************************
# Date: 050924 (Expected Solution with 23 Lines of Code)      *
# Title: Number the Lines in a File                           *
# Status: In Progress (In Progress / Testing / Working)       *
# Create a program that adds line numbers to a file. The name *
# of the input file will be read from the user, as will the   *
# name of the new file that your program will create. Each    *
# line in the output file should begin with the line number,  *
# followed by a colon and a space, followed by the line from  *
# the input file.                                             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
if __name__ == "__main__":
  file_names = input("Enter the file names: ")
  file_list = []
  file_list = file_names.split()
  with open(file_list[0], "r") as file:
    line_num = 1
    with open(file_list[1], "w") as file2:
      for line in file:
        print(f"{line_num}: {line}", end="")
        file2.write(f"{line_num}: {line}")
        line_num += 1
  print("\n"+"Thank you for using this app.")
#**************************************************************