#!/bin/bash
#**************************************************************
# Date: 071023   (Expected Solution with 35 Lines of Code)    *
# Title: Multiple Word Palindromes                            *
# Status: Testing (In Progress / Testing / Working)           *
# There are numerous phrases that are palindromes when        *
# spacing is ignored. Examples include "go dog", "flee to me  *
# remote elf" and "some men interpret nine memos", among many *
# other, Extend your solution to Exercise 72 so that it       *
# ignores spacing while determining whether or not a string   *
# is a palindrome. For an additional challenge, extend your   *
# solution so that is also ignores punctuation marks and      *
# treats uppercase and lowrcase letters as equivalent.        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
PosCtr, LtrEqCtr = (0, 0)
#--------------------------------------------------------------
InWord = input("Enter the groups of words to be checked: ")
FwdWord = InWord.lower().replace(" ", "").replace(".", "").replace("?", "")
BwdWord = FwdWord
BPosCtr = len(FwdWord) - 1
while PosCtr < len(FwdWord):
  if FwdWord[PosCtr] != BwdWord[BPosCtr - PosCtr]:
    LtrEqCtr = LtrEqCtr + 1
  print(PosCtr, FwdWord[PosCtr], BwdWord[BPosCtr - PosCtr], LtrEqCtr)
  PosCtr = PosCtr + 1
if LtrEqCtr == 0:
  print("The group of words '%s' is a palindrome." % InWord)
else:
  print("The group of words '%s' is NOT a palindrome." % InWord)
print("Thank you for using this app.")
#**************************************************************