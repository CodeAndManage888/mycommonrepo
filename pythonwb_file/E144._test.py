#!/bin/bash
#**************************************************************
# Date: 051224 (Expected Solution with 23 Lines of Code)      *
# Title: Number the Lines in a File                           *
# Status: Testing (In Progress / Testing / Working)           *
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
if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    file_list = file_name.split()
    # prep line number and colon with space for the line header
    line_num = 0
    line_header = "{:>4}: "
    output_lines = []
    # open and read the input file
    try:
        with open(file_list[0], "r") as file_handle:
            for line in file_handle:
                line_num += 1
                print(line_header.format(line_num) + line, end="")
                output_lines.append(line_header.format(line_num) + line)
            print("\n")
        with open(file_list[1], "w") as file_out:
            file_out.writelines(output_lines)
    except IOError:
        print("File Error for : ", file_name[0], file_name[1])

    print("Thank you for using this app.")
#**************************************************************