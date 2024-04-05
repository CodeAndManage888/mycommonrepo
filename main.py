#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 48 Lines of Code)      *
# Title: Anagrams Again                                       *
# Status: In Progress (In Progress / Testing / Working)       *
# The notion of anagrams can be extended to multiple words.   *
# For example, “William Shakespeare” and “I am a weakish      *
# speller” are anagrams when capitalization and spacing are   *
# ignored. Extend your program from Exercise 135 so that it   *
# is able to check if two phrases are anagrams. Your program  *
# should ignore capitalization, punctuation marks and spacing *
# when making the determination.                              *
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
  print(anagram_dict)
  return anagram_dict
#--------------------------------------------------------------
if __name__ == "__main__":
  user_str1 = input("Enter the first string: ")
  clean_user_str1 = user_str1.lower()
  user_str2 = input("Enter the second string: ")
  clean_user_str2 = user_str2.lower()
  if anagram_chk(clean_user_str1.replace(" ", "")) == anagram_chk(clean_user_str2.replace(" ", "")):
    print("The two strings are anagrams.")
  else:
    print("The two strings are not anagrams.")
  print("Thank you for using this app.")
#**************************************************************
