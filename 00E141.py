#!/bin/bash
#**************************************************************
# Date: 050424 (Expected Solution with 40 Lines of Code)      *
# Title: Display the Head of a File                           *
# Status: Testing (In Progress / Testing / Working)           *
# Unix-based operating systems usually include a tool named   *
# head. It displays the ﬁrst 10 lines of a file whose name is *
# provided as a command line parameter. Write a Python        *
# program that provides the same behavior. Display an         *
# appropriate error message if the file requested by the user *
# does not exist or if the command line parameter is omitted. *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func_name(user_in):
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_name = input("Enter the file name: ")
  if not file_name:
      print("Error: File name is required.")
  else:
      try:
          with open(file_name, 'r') as file:
              lines = file.readlines()
              if len(lines) > 10:
                  lines = lines[:10]
              for line in lines:
                  print(line.strip())
      except FileNotFoundError:
          print("Error: File not found.")
  print("Thank you for using this app.")
#**************************************************************
