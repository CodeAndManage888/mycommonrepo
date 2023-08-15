#!/bin/bash
#**************************************************************
# Date: 081323 (Expected Solution with 48 Lines of Code)      *
# Title: Capitalize It                                        *
# Status: Testing (In Progress / Testing / Working)           *
# Many people do not use capital letters correctly,           *
# especially when typing on small devices like smart phones.  *
# In this exercise, you will write a function that            *
# capitalizes the appropriate characters in a string. A       *
# lowercase “i” should be replaced with an uppercase “I” if   *
# it is both preceded and followed by a space. The ﬁrst       *
# character in the string should also be capitalized, as well *
# as the ﬁrst non-space character after a “.”, “!” or “?”.    *
# For example, if the function is provided with the string    *
# “what time do i have to be there? what’s the address?” then *
# it should return the string “What time do I have to be      *
# there? What’s the address?”. Include a main program that    *
# reads a string from the user, capitalizes it using your     *
# function, and displays the result.                          *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def capitalize_func(string_input):
  for idx, char in enumerate(string_input):
    if idx == 0:
      print(char.capitalize(),end="")
      prev_space_flag, punc_mark_flag = False, False
    elif char == " ":
      prev_space_flag = True
      print(char,end="")
    elif (char == "." or char == "!" or char == "?"):
      punc_mark_flag = True
      print(char,end="")
    elif char == "i" and prev_space_flag and string_input[idx + 1] == " ":
      print(char.capitalize(),end="")
      prev_space_flag = False
    elif punc_mark_flag and string_input[idx - 1] == " ":
      print(char.capitalize(),end="")
      punc_mark_flag = False
    else:
      print(char,end="")
      prev_space_flag = False
#--------------------------------------------------------------
if __name__ == "__main__":
  user_string = input("Write anything to be capitalize: ")
  capitalize_func(user_string)
  print("")
  print("Thank you for using this app.")
#**************************************************************