#!/bin/bash
#**************************************************************
# Date: 102923 (Expected Solution with 38 Lines of Code)      *
# Title: Only the Words                                       *
# Status: Testing (In Progress / Testing / Working)           *
# In this exercise you will create a program that identiﬁes   *
# all of the words in a string entered by the user. Begin by  *
# writing a function that takes a string of text as its only  *
# parameter. Your function should return a list of the words  *
# in the string with the punctuation marks at the edges of    *
# the words removed. The punctuation marks that you must      *
# remove include commas, periods, question marks, hyphens,    *
# apostrophes, exclamation points, colons, and semicolons.    *
# Do not remove punctuation marks that appear in the middle   *
# of a words, such as the apostrophes used to form a          *
# contraction. For example, if your function is provided      *
# with the string "Examples of contractions include: don’t,   *
# isn’t, and wouldn’t." then your function should return the  *
# list ["Examples", "of", "contractions", "include",          *
# "don’t","isn’t","and","wouldn’t"] . Write a main program    *
# that demonstrates your function. It should read a string    *
# from the user and display all of the words in the string    *
# with the punctuation marks removed. You will need to import *
# your solution to this exercise when completing Exercise 158.*
# As a result, you should ensure that your main program only  *
# runs when your ﬁle has not been imported into another       *
# program.                                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def words_func(user_str):
  word_list = []
  for word in user_str.split(" "):
    word_list.append(word.strip(",.:;'\"?!"))
  return word_list
#--------------------------------------------------------------
if __name__ == "__main__":
  user_string = input("Enter the string of words as an input: ")
  out_list = words_func(user_string)
  print("The words in the string are: %s" % ', '.join(map(str, out_list)))
  print("Thank you for using this app.")
#**************************************************************