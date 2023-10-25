#!/bin/bash
#**************************************************************
# Date: 101923 (Expected Solution with 21 Lines of Code)      *
# Title: Avoiding Duplicates                                  *
# Status: In Progress (In Progress / Testing / Working)       *
# In this exercise, you will create a program that reads      *
# words from the user until the user enters a blank line.     *
# After the user enters a blank line your program should dis- *
# play each word entered by the user exactly once. The words  *
# should be displayed in the same order that they were        *
# entered. For example, if the user enters: first second      *
# first third second then your program should display: first  *
# second third                                                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
word_list = []
user_word = " "
#--------------------------------------------------------------
def rem_dup(user_list):
  unique_list = []
  ctr = 0
  while user_list:
    word = user_list.pop(0)
    if word not in unique_list:
      unique_list.append(word)
    unique_list.reverse()
  while ctr <= len(unique_list) - 1:
    print(unique_list[ctr])
    ctr -= 1
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  while user_word != "":
    user_word = input("Enter a word: ")
    if user_word != "":
      word_list.append(user_word)
  rem_dup(word_list)
  print("Thank you for using this app.")
#**************************************************************
