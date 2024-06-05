#!/bin/bash
#**************************************************************
# Date: 051224 (Expected Solution with 39 Lines of Code)      *
# Title: Find the Longest Word in a File                      *
# Status: Testing (In Progress / Testing / Working)           *
# In this exercise you will create a Python program that      *
# identifies the longest word(s) in a file. Your program      *
# should output an appropriate message that includes the      *
# length of the longest word, along with all of the words of  *
# that length that occurred in the file. Treat any group of   *
# non-white space characters as a word, even if it includes   *
# numbers or punctuation marks.                               *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
if __name__ == "__main__":
  user_in = input("Enter the file name: ")
  word_len = 0
  word_list = []
  with open(user_in, "r") as file_handle:
    for line in file_handle:
        print(line)
        word_dump = line.split()
        for word in word_dump:
            print(word)
            if len(word) > word_len:
                word_len = len(word)
                word_list.clear()
                word_list.append(word)
            elif len(word) == word_len:
                word_list.append(word)
            else:
                continue
  print("The longest word(s) in the file is/are:", ",".join(word_list), 
        "with a length of", word_len)
  print("Thank you for using this app.")
#**************************************************************