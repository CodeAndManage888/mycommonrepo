#!/bin/bash
#**************************************************************
# Date: 051224 (Expected Solution with 23 Lines of Code)      *
# Title: Number the Lines in a File                           *
# Status: In Progress (In Progress / Testing / Working)       *
# Create a program that adds line numbers to a file. The name *
# of the input file will be read from the user, as with the   *
# name of the new file that your program will create. Each    *
# line in the output file should begin with the line number,  *
# followed by a colon and a space, followed by the line from  *
# the input ﬁle.                                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func(user_in):
    return
#--------------------------------------------------------------
if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    file_list = file_name.split()
    # prep line number and colon with space for the line header
    line_num = 0
    line_header = "{:>4}: "
    # create/open output file
    try:
        file_out = open(file_list[1], "w")
    except IOError:
        print("File cannot be created/open: ", file_list[1])

    # open first file for line reading
    try:
        file_handle = open(file_list[0], "r")
        # read each line from the file
        for line in file_handle:
            line_num += 1
            print(line + line_header.format(line_num), end="")
            file_out = line + line_header.format(line_num)
        # write line number and colon and line to second file
        file_handle.close()
    except IOError:
        print("File cannot be opened: ", file_name)
    
    # create second file for output
    #file_name = input("Enter the output file name: ")

    # open second file for line writing

    # read first file line by line

    

    # close second file
    print("Thank you for using this app.")
#**************************************************************