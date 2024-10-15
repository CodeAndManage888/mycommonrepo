#!/bin/bash
#**************************************************************
# Date: 072824 (Expected Solution with 51 Lines of Code)      *
# Title: Spell Checker                                        *
# Status: In Progress (In Progress / Testing / Working)       *
#  A spell checker can be a helpful tool for people who       *
# struggle to spell words correctly. In this exercise, you    *
# will write a program that reads a file and displays all of  *
# the words in it that are misspelled. Misspelled words will  *
# be identiﬁed by checking each word in the file against a    *
# list of known words. Any words in the user’s file that do   *
# not appear in the list of known words will be reported as   *
# spelling mistakes. The user will provide the name of the    *
# file to check for spelling mistakes as a command line       *
# parameter. Your program should display an appropriate error *
# message if the command line parameter is missing. An error  *
# message should also be displayed if your program is unable  *
# to open the user’s file. Use your solution to Exercise 111  *
# when creating your solution to this exercise so that words  *
# followed by a comma, period or other punctuation mark are   *
# not reported as spelling mistakes. Ignore the               *
# capitalization of the words when checking their spelling.   *
# Hint: While you could load all of the English words from    *
# the words data set into a list, searching a list is slow if *
# you use Python’s in operator. It is much faster to check if *
# a key is present in a dictionary, or if a value is present  *
# in a set. If you use a dictionary, the words will be the    *
# keys. The values can be the integer 0 (or any other value)  *
# because the values will never be used.                      *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
spell_dict = {"the": 0,"be": 0,"to": 0,"of": 0,"and": 0,"a": 0,"in": 0, 
              "that": 0,"have": 0,"I": 0,"it": 0,"for": 0,"not": 0,"on": 0,
              "with": 0,"he": 0,"as": 0,"you": 0,"do": 0,"at": 0,"this": 0,
              "but": 0,"his": 0,"by": 0,"from": 0,"they": 0,"we": 0,"say": 0,
              "her": 0,"she": 0,"or": 0,"an": 0,"will": 0,"my": 0,"one": 0,
              "all": 0,"would": 0,"there": 0,"their": 0,"what": 0,"so": 0,
              "up": 0,"out": 0,"if": 0,"about": 0,"who": 0,"get": 0,"which": 0,
              "go": 0,"me": 0}
mispelled = []
#--------------------------------------------------------------
def spell_check(file_loc, user_file):
  file_path = f"{file_loc}/{user_file}"

  try:
    with open(file_path, "r") as file_handle:
      file_data = file_handle.read()
      word_list = file_data.split()
  except FileNotFoundError:
    print("Error: File not found.")
  except PermissionError:
    print("Error: Permission denied.")
  except IsADirectoryError:
    print("Error: Is a directory.")
  except IOError as e:
    print(f"An IO error has occured: {e}")

  for word in word_list:
    word = word.lower()
    word = word.strip(",.:;'\"?!\\")
    value = spell_dict.get(word, 1)
    if value == 1:
      mispelled.append(word)

  if len(mispelled) == 0:
    print("No misspelled words found.")
  else:
    print("The following words are misspelled:")
    for word in mispelled:
      print(word)
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  file_loc = input("Please enter the file location: ")
  file_name = input("Please enter the file name: ")
  if file_name == "":
    print("Error: File name is missing.")
  else:
    spell_check(file_loc, file_name)
  print("Thank you for using this app.")
#**************************************************************