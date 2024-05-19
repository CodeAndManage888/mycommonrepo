#!/bin/bash
#**************************************************************
# Date: 050424 (Expected Solution with 35 Lines of Code)      *
# Title: Display the Tail of a File                           *
# Status: Testing (In Progress / Testing / Working)           *
# Unix-based operating systems also typically include a tool  *
# named tail. It displays the last 10 lines of a file whose   *
# name is provided as a command line parameter. Write a       *
# Python program that provides the same behavior. Display an  *
# appropriate error message if the file requested by the user *
# does not exist or if the command line parameter is omitted. *
# There are several different approaches that can be taken to *
# solve this problem. One option is to load the entire        *
# contents of the ﬁle into a list and then display the last   *
# 10 elements. Another option is to read the contents of the  *
# file twice, once to count the lines, and a second time to   *
# display the last 10 lines. However, both of these solutions *
# are undesirable when working with large ﬁles. Another       *
# solution exists that only requires you to read the file     *
# once, and only requires you to store 10 lines from the file *
# at one time. For an added challenge, develop such a         *
# solution.                                                   *
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