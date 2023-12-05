#!/bin/bash
#**************************************************************
# Date: 112423 (Expected Solution with 64 Lines of Code)      *
# Title: Tokenizing a String                                  *
# Status: In Progress (In Progress / Testing / Working)       *
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
symbol = ["+", "-", "*", "/", "(", ")"]
#--------------------------------------------------------------
# possible solution is to create a list with no spaces first
# then split the string into tokens
#--------------------------------------------------------------
# having issues with more than one space between tokens and
# more than 1 numbers together. parenthesis is also a problem
# tokens that are are in between numbers are also a problem
#--------------------------------------------------------------
def token_func(user_in):
  no_spaces_list = user_in.split()
  print(no_spaces_list)                    # test only
  token_list = []
  for i in range(len(no_spaces_list)):
    if len(no_spaces_list[i]) == 1:
      if no_spaces_list[i] in symbol:
        token_list.append(no_spaces_list[i])
      else:
        token_list.append(int(no_spaces_list[i]))
    else:
      for j in range(len(no_spaces_list[i])):
        if no_spaces_list[i][j] == "+" or no_spaces_list[i][j] == "-":
          if no_spaces_list[i].lstrip('-+').isdigit():
            token_list.append(int(no_spaces_list[i]))
            break
          elif no_spaces_list[i].isdigit():
            token_list.append(int(no_spaces_list[i]))
            break
        elif no_spaces_list[i][j] in symbol:
          token_list.append(no_spaces_list[i][j])
        else:
          token_list.append(int(no_spaces_list[i][j]))
  return token_list
#--------------------------------------------------------------
if __name__ == "__main__":
  math_exp = input("Enter a mathematical expression: ")
  print(token_func(math_exp))
  print("Thank you for using this app.")
#**************************************************************