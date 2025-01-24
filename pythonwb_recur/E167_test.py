#!/bin/bash
#**************************************************************
# Date: 080324 (Expected Solution with 29 Lines of Code)      *
# Title: Recursive Palindrome                                 *
# Status: Testing (In Progress / Testing / Working)           *
#  The notion of a palindrome was introduced previously in    *
# Exercise 72. In this exercise you will write a recursive    *
# function that determines whether or not a string is a       *
# palindrome. The empty string is a palindrome, as is any     *
# string containing only one character. Any longer string is  *
# a palindrome if its first and last characters match, and if *
# the string formed by removing the first and last characters *
# is also a palindrome.                                       *
# Write a main program that reads a string and from the user. *
# Use your recursive function to determine whether or not the *
# string is a palindrome. Then display an appropriate message *
# for the user.                                                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import string
#--------------------------------------------------------------
def pal_chck(str_data):
  if len(str_data) <= 1:
    return True
  elif str_data[0] == str_data[-1]:
    return pal_chck(str_data[1:-1])
#--------------------------------------------------------------
if __name__ == "__main__":
  user_data = input("Please enter a string: ")
  cleaned_string = user_data.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
  if pal_chck(cleaned_string) is True:
    print("The string %a that you entered is a palindrome." % (user_data))
  else:
    print("The string %a that you entered is NOT a palindrome." % (user_data))
  print("Thank you for using this app.")
#**************************************************************