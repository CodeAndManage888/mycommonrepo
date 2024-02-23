#!/bin/bash
#**************************************************************
# Date: 112423 (Expected Solution with 64 Lines of Code)      *
# Title: Tokenizing a String                                  *
# Status: Testing (In Progress / Testing / Working)           *
# Tokenizing is the process of converting a string into a     *
# list of substrings, known as tokens. In many circumstances, *
# a list of tokens is far easier to work with than the        *
# original string because the original string may have        *
# irregular spacing. In some cases substantial work is also   *
# required to determine where one token ends and the next one *
# begins. In a mathematical expression, tokens are items such *
# as operators, numbers and parentheses. Some tokens, such as *
# *, /, ˆ, ( and ) are easy to identify because the token is a*
# single character, and the character is never part of        *
# another token. The + and - symbols are a little bit more    *
# challenging to handle because they might represent the      *
# addition or subtraction operator, or they might be part of  *
# a number token. Hint: A + or - is an operator if the        *
# non-whitespace character immediately before it is part of a *
# number, or if the non-whitespace character immediately      *
# before it is a close parenthesis. Otherwise it is part of a *
# number. Write a function that takes a string containing a   *
# mathematical expression as its only parameter and breaks it *
# into a list of tokens. Each token should be a parenthesis,  *
# an operator, or a number with an optional leading + or - (  *
# for simplicity we will only work with integers in this      *
# problem). Return the list of tokens as the function’s       *
# result. You may assume that the string passed to your       *
# function always contains a valid mathematical expression    *
# consisting of parentheses, operators and integers. However, *
# your function must handle variable amounts of whitespace    *
# between these elements. Include a main program that         *
# demonstrates your tokenizing function by reading an         *
# expression from the user and printing the list of tokens.   *
# Ensure that the main program will not run when the file     *
# containing your solution is imported into another program.  *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
symbol = ["*", "/", "(", ")"]
#--------------------------------------------------------------
def token_func(math_str):
  token_list = []
  no_spaces_list = math_str.split()
  print("Input: ", no_spaces_list)
  for exp in no_spaces_list:
    if len(exp) == 1:
      token_list.append(exp)
    else:
      signed_char = ""
      for char in exp:
        if char in symbol:
          if len(signed_char) != 0:
            token_list.append(signed_char)
            signed_char = ""
          token_list.append(char)
        elif char == "+" or char == "-" or char.isdigit():
          signed_char += char
      if signed_char != "":
        token_list.append(signed_char)
  return token_list
#--------------------------------------------------------------
if __name__ == "__main__":
  math_exp = input("Enter a mathematical expression: ")
  print(token_func(math_exp))
  print("Thank you for using this app.")
#**************************************************************
# Open Issues:
# 1.) The exercise 122 solution can't handle signed number that
#     affects the exercise 123 and 124 solutions.