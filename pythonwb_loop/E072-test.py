#!/bin/bash
#**************************************************************
# Date: 071023   (Expected Solution with 23 Lines of Code)    *
# Title: Is a String a Palindrome                             *
# Status: Testing (In Progress / Testing / Working)           *
# A string is a palindrome if it is identical forward and     *
# backward. For example "anna", "civic", "level" and "hannah" *
# are all examples of palindromic words. Write a program that *
# reads a string from the user and uses a loop to determines  *
# whether or not it is a palindrome. Display the result,      *
# including a meaningful output message.                      *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
PosCtr, LtrEqCtr = (0, 0)
#--------------------------------------------------------------
InWord = input("Enter the word to be checked: ")
FwdWord = InWord.lower()
BwdWord = FwdWord
BPosCtr = len(InWord) - 1
while PosCtr < len(InWord):
  if FwdWord[PosCtr] != BwdWord[BPosCtr - PosCtr]:
    LtrEqCtr = LtrEqCtr + 1
  PosCtr = PosCtr + 1
if LtrEqCtr == 0:
  print("The input word '%s' is a palindrome." % InWord)
else:
  print("The input word '%s' is NOT a palindrome." % InWord)
print("Thank you for using this app.")
#**************************************************************