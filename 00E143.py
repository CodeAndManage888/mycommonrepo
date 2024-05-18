#!/bin/bash
#**************************************************************
# Date: 050524 (Expected Solution with 27 Lines of Code)      *
# Title: Concatenate Multiple Files                           *
# Status: Testing (In Progress / Testing / Working)           *
# Unix-based operating systems typically include a tool named *
# cat, which is short for concatenate. Its purpose is to      *
# concatenate and display one or more files whose names are   *
# provided as command line parameters. The files are displayed*
# in the same order that they appear on the command line.     *
# Create a Python program that performs this task. It should  *
# generate an appropriate error message for any file that     *
# cannot be displayed, and then proceed to the next file.     *
# Display an appropriate error message if your program is     *
# started without any command line parameters.                *
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