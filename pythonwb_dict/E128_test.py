#!/bin/bash
#**************************************************************
# Date: 120723 (Expected Solution with 40 Lines of Code)      *
# Title: Reverse Lookup                                       *
# Status: Testing (In Progress / Testing / Working)           *
# Write a function named reverseLookup that ﬁnds all of the   *
# keys in a dictionary that map to a speciﬁc value. The       *
# function will take the dictionary and the value to search   *
# for as its only parameters. It will return a (possibly      *
# empty) list of keys from the dictionary that map to the     *
# provided value. Include a main program that demonstrates    *
# the reverseLookup function as part of your solution to this *
# exercise. Your program should create a dictionary and then  *
# show that the reverseLookup function works correctly when   *
# it returns multiple keys, a single key, and no keys. Ensure *
# that your main program only runs when the ﬁle containing    *
# your solution to this exercise has not been imported into   *
# another program.                                            *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def reverseLookup(dict_a, user_in):
  user_in = user_in.lower()
  common_key = []
  for key in dict_a:
    if user_in == dict_a[key]:
      common_key.append(key)
  return common_key
#--------------------------------------------------------------
if __name__ == "__main__":
  print("This is the main program.")
  mainDictionary = {"a": "apple", "b": "banana", "c": "carrot", "d": "dog", "e": "elephant", "f": "frog", "g": "grape", "h": "horse", "i": "ice cream", "j": "jelly", "k": "kangaroo", "l": "lemon", "m": "mango", "n": "narwhal", "o": "orange", "p": "pineapple", "q": "quail", "r": "rabbit", "s": "strawberry", "t": "tiger", "u": "umbrella", "v": "vulture", "w": "whale", "x": "carrot", "y": "yak", "z": "zebra"}
  ValueSearch = input("Enter a value to search for: ")
  print(reverseLookup(mainDictionary, ValueSearch))
  print("Thank you for using this app.")
#**************************************************************
