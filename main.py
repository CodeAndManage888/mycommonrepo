#!/bin/bash
#*************************************************************
# Date: 070224 (Expected Solution with 49 Lines of Code)     *
# Title: A Book with No “e” …                                *
# Status: In Progress (In Progress / Testing / Working)      *
#  The novel “Gadsby” is over 50,000 words in length. While  *
# 50,000 words isn’t normally remarkable for a novel, it is  *
# in this case because none of the words in the book use the *
# letter “e”. This is particularly noteworthy when one       *
# considers that “e” is the most common letter in English.   *
# Write a program that reads a list of words from a file and *
# determines what proportion of the words use each letter    *
# of the alphabet. Display the result for all 26 letters.    *
# Include an additional message identifying the letter that  *
# is used in the smallest proportion of the words. Your      *
# program should ignore any punctuation marks and it should  *
# treat uppercase and lowercase letters as equivalent.       *
#                                                            *
# Computed Result Validated:                                 *
#*************************************************************
#--------------------------------------------------------------
alpha_list = {"a":0.00, "b":0.00, "c":0.00, "d":0.00, "e":0.00, 
              "f":0.00, "g":0.00, "h":0.00, "i":0.00, "j":0.00, 
              "k":0.00, "l":0.00, "m":0.00, "n":0.00, "o":0.00, 
              "p":0.00, "q":0.00, "r":0.00, "s":0.00, "t":0.00, 
              "u":0.00, "v":0.00, "w":0.00, "x":0.00, "y":0.00, 
              "z":0.00}
tot_ltr = 0
#--------------------------------------------------------------
if __name__ == "__main__":
  with open("test06.txt", "r") as wordlist:
    word_list = wordlist.readlines()
  
  for idx, word in enumerate(word_list):
    word_list[idx] = word.lower()
    for letter in word:
      if letter in alpha_list:
        alpha_list[letter] += 1
    tot_ltr = len(word)

  for idx, keys in enumerate(alpha_list):
    alpha_list[keys] = alpha_list[keys] / tot_ltr

  for idx, keys in enumerate(alpha_list):
    print(f"{keys}: {alpha_list[keys]:.4f}")
    
  print("Thank you for using this app.")
#**************************************************************