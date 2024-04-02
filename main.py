#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 39 Lines of Code)      *
# Title: Anagrams                                             *
# Status: Testing (In Progress / Testing / Working)           *
# Two words are anagrams if they contain all of the same      *
# letters, but in a different order. For example, “evil” and  *
# “live” are anagrams because each contains one e, one i, one *
# l, and one v. Create a program that reads two strings from  *
# the user, determines whether or not they are anagrams, and  *
# reports the result.                                         *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def anagram_chk(user_str):
  anagram_dict = {}
  for char in user_str:
    if char in anagram_dict:
      anagram_dict[char] += 1
    else:
      anagram_dict[char] = 1
  return anagram_dict
#--------------------------------------------------------------
if __name__ == "__main__":
  user_str1 = input("Enter a string: ")
  user_str2 = input("Enter a string: ")
  if anagram_chk(user_str1) == anagram_chk(user_str2):
    print("The two strings are anagrams.")
  else:
    print("The two strings are not anagrams.")
  print("Thank you for using this app.")
#**************************************************************