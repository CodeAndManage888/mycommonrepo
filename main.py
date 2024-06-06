#!/bin/bash
#**************************************************************
# Date: 051324 (Expected Solution with 43 Lines of Code)      *
# Title: Letter Frequencies                                   *
# Status: In Progress (In Progress / Testing / Working)       *
# One technique that can be used to help break some simple    *
# forms of encryption is frequency analysis. This analysis    *
# examines the encrypted text to determine which characters   *
# are most common. Then it tries to map the most common       *
# letters in English, such as E and T, to the most commonly   *
# occurring characters in the encrypted text. Write a program *
# that initiates this process by determining and displaying   *
# the frequencies of all letters in a file. Ignore spaces,    *
# punctuation marks, and numbers as you perform this          *
# analysis. Your program should be case insensitive, treating *
# a and A as equivalent. The user will provide the filename   *
# as a command line parameter. Your program should display a  *
# meaningful error message if the user provides the wrong     *
# number of command line parameters, or if the program is     *
# unable to open the ﬁle indicated by the user.               *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
if __name__ == "__main__":
  input_file = input("Enter the file name: ")
  if input_file == "":
    print("Error: No file name was provided.")
  else:
    ltr_dict = {}
    with open(input_file, "r") as file_handle:
      for line in file_handle:
        #print(line)
        for char in line:
          #print(char)
          if char.isalpha():
            if char.upper() in ltr_dict:
              ltr_dict[char.upper()] += 1
            else:
              ltr_dict[char.upper()] = 1

            #print(char)
          else:
            continue
  sorted_by_keys = dict(sorted(ltr_dict.items()))
  print("Letter Frequencies:")
  for ltr in sorted_by_keys:
    print(ltr, ":", sorted_by_keys[ltr])
  print("Thank you for using this app.")
#**************************************************************