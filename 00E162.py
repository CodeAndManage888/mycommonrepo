#!/bin/bash
#**************************************************************
# Date: 072924 (Expected Solution with 45 Lines of Code)      *
# Title: Consistent Line Lengths                              *
# Status: In Progress (In Progress / Testing / Working)       *
#  While 80 characters is a common width for a terminal       *
# window, some terminals are narrow or wider. This can        *
# present challenges when displaying documents containing     *
# paragraphs of text. The lines might be too long and wrap,   *
# making them difficult to read, or they might be too short   *
# and fail to make use of the available space. Write a        *
# program that opens a file and displays it so that each line *
# is filled as full as possible. If you read a line that is   *
# too long then your program should break it up into words    *
# and add words to the current line until it is full. Then    *
# your program should start a new line and display the        *
# remaining words. Similarly, if you read a line that is too  *
# short then you will need to use words from the next line of *
# the file to finish filling the current line of output. For  *
# example, consider a file containing the following lines from*
# “Alice’s Adventures in Wonderland”: Alice was beginning to  *
# get very tired of sitting by her sister on the bank, and of *
# having nothing to do: once or twice she had peeped into the *
# book her sister was reading, but it had no pictures or      *
# conversations in it,"and what is the use of a book,"        *
# thought Alice, "without pictures or conversations?" When    *
# formatted for a line length of 50 characters, it should be  *
# displayed as: Alice was beginning to get very tired of      *
# sitting by her sister on the bank, and of having nothing to *
# do: once or twice she had peeped into the book her sister   *
# was reading, but it had no pictures or conversations in it, *
# "and what is the use of a book," thought Alice, "without    *
# pictures or conversations?"                                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func_justify(data_input):
  with open(data_input, "r") as f:
    file_data = f.readlines()

  
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_loc = input("Please enter the file location: ")
  file_name = input(f"Please enter the file name: ")
  input_data = file_loc + file_name
  func_justify(input_data)
  print("Thank you for using this app.")
#**************************************************************