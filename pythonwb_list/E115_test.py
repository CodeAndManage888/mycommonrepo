#!/bin/bash
#**************************************************************
# Date: 110323 (Expected Solution with 32 Lines of Code)      *
# Title: Pig Latin                                            *
# Status: Testing (In Progress / Testing / Working)           *
# Pig Latin is a language constructed by transforming English *
# words. While the origins of the language are unknown, it    *
# is mentioned in at least two documents from the nineteenth  *
# century, suggesting that it has existed for more than 100   *
# years. The following rules are used to translate English    *
# into Pig Latin:  If the word begins with a consonant       *
# (including y), then all letters at the beginning of the     *
# word, up to the ﬁrst vowel (excluding y), are removed and   *
# then added to the end of the word, followed by "ay". For    *
# example, computer becomes omputercay and think becomes      *
# inkthay. If the word begins with a vowel (not including    *
# y), then "way" is added to the end of the word. For example,*
# algorithm becomes algorithmway and office becomes officeway.*
# Write a program that reads a line of text from the user.    *
# Then your program should translate the line into Pig Latin  *
# and display the result. You may assume that the string      *
# entered by the user only contains lowercase letters and     *
# spaces.                                                     *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def pig_ltn_trans(user_str):
  pig_ltn_str = ""
  vowels = ["a", "e", "i", "o", "u"]
  word_list = []
  word_list = user_str.split()
  for word in word_list:  
    ctr = 0
    for ltr in word:
      if ltr in vowels:
        if ctr == 0:
          pig_ltn_str += word + "way "
          break
        else:
          pig_ltn_str += word[ctr:] + word[0:ctr] + "ay "
          break
      else:
        ctr += 1
  return pig_ltn_str
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input = input("Enter a string of words in lowercase only: ")
  print("Translated string: ", pig_ltn_trans(user_input))
  print("Thank you for using this app.")
#**************************************************************