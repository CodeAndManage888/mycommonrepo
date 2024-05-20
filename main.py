#!/bin/bash
#**************************************************************
# Date: 051224 (Expected Solution with 23 Lines of Code)      *
# Title: Number the Lines in a File                           *
# Status: In Progress (In Progress / Testing / Working)       *
# Create a program that adds line numbers to a file. The name *
# of the input file will be read from the user, as will the   *
# name of the new file that your program will create. Each    *
# line in the output file should begin with the line number,  *
# followed by a colon and a space, followed by the line from  *
# the input ﬁle.                                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func_name(user_in):
    return
#--------------------------------------------------------------
if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    file_list = file_name.split()
    for file_name in file_list:
        try:
            file_handle = open(file_name, "r")
            print(file_handle.read())
            file_handle.close()
        except IOError:
            print("File cannot be opened: ", file_name)
    print("Thank you for using this app.")
#**************************************************************