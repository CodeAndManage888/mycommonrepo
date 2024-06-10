#!/bin/bash
#**************************************************************
# Date: 051324 (Expected Solution with 37 Lines of Code)      *
# Title: Words that Occur Most                                *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that displays the word (or words) that      *
# occur most frequently in a file. Your program should begin  *
# by reading the name of the file from the user. Then it      *
# should find the word(s) by splitting each line in the file  *
# at each space. Finally, any leading or trailing punctuation  *
# marks should be removed from each word. In addition, your   *
# program should ignore capitalization. As a result, apple    *
# ,apple! , Apple and ApPlE should all be treated as the same *
# word. You will probably find your solution to Exercise 111  *
# helpful when completing this problem.                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
def words_func(user_str):
  word_list = {}
  for word in user_str.split():
    cleaned_word = word.strip(",.:;'\"?!\\").lower()
    if cleaned_word in word_list:
      word_list[cleaned_word] += 1
    else:
      word_list[cleaned_word] = 1
  return word_list
#--------------------------------------------------------------
if __name__ == "__main__":
  user_infile = input("Enter the name of the file to be processed: ")
  with open(user_infile, "r") as infile:
    user_string = infile.read()
  out_list = words_func(user_string)
  print("Word Frequencies:")
  for ltr in sorted(out_list):
    print(ltr, ":", out_list[ltr])
  print("Thank you for using this app.")
#**************************************************************