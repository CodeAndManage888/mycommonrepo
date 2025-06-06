#!/bin/bash
#**************************************************************
# Date: 072824 (Expected Solution with 61 Lines of Code)      *
# Title: Repeated Words                                       *
# Status: Testing (In Progress / Testing / Working)           *
#  Spelling mistakes are only one of many different kinds of  *
# errors that might appear in a written work. Another error   *
# that is common for some writers is a repeated word. For     *
# example, an author might inadvertently duplicate a word, as *
# shown in the following sentence: At least one value must be *
# entered entered in order to compute the average. Some word  *
# processors will detect this error and identify it when a    *
# spelling or grammar check is performed. In this exercise    *
# you will write a program that detects repeated words in a   *
# text file. When a repeated word is found your program should*
# display a message that contains the line number and the     *
# repeated word. Ensure that your program correctly handles   *
# the case where the same word appears at the end of one line *
# and the beginning of the following line, as shown in the    *
# previous example. The name of the file to examine will be   *
# provided as the program’s only command line parameter.      *
# Display an appropriate error message if the user fails to   *
# provide a command line parameter, or if an error occurs     *
# while processing the file.                                  *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def dup_words(floc,fname):
  prev_word = ""
  line_num = 0
  file_path = f"{floc}/{fname}"
  try:
    with open(file_path, "r") as file_handle:
      file_data = file_handle.readlines()
  except FileNotFoundError:
    print("Error: File not found.")
    return
  except PermissionError:
    print("Error: Permission denied.")
    return
  except IsADirectoryError:
    print("Error: Is a directory.")
    return
  except IOError as e:
    print(f"An IO error has occured: {e}")
    return
  
  for index, line in enumerate(file_data):
    line = line.lower()
    line = line.strip(",.:;'\"?!\\")
    lines = line.split()
    for word in lines:
      if word == prev_word:
        print(f"Duplicate word: {word} at line {index+1}: ")
      else:
        prev_word = word
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_loc = input("Please enter the file location: ")
  file_name = input(f"Please enter the file name: ")
  dup_words(file_loc,file_name)
  print("Thank you for using this app.")
#**************************************************************
