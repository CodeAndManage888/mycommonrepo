#!/bin/bash
#**************************************************************
# Date: 081323 (Expected Solution with 30 Lines of Code)      *
# Title: Does a String Represent an Integer?                  *
# Status: Testing (In Progress / Testing / Working)           *
# In this exercise you will write a function named isInteger  *
# that determines whether or not the characters in a string   *
# represent a valid integer. When determining if a string     *
# represents an integer you should ignore any leading or      *
# trailing white space. Once this white space is ignored, a   *
# string represents an integer if its length is at least 1    *
# and it only contains digits, or if its ﬁrst character is    *
# either +or- and the ﬁrst character is followed by one or    *
# more characters, all of which are digits. Write a main      *
# program that reads a string from the user and reports       *
# whether or not it represents an integer. Ensure that the    *
# main program will not run if the ﬁle containing your        *
# solution is imported into another program. Hint: You may    *
# ﬁnd the lstrip ,rstrip and/orstrip methods for strings      *
# helpful when completing this exercise. Documentation for    *
# these methods is available online.                          *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
valid_char = ["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#--------------------------------------------------------------
def isInteger(user_input):
  char_chk = True
  proc_data_one = user_input.strip()
  if proc_data_one != "":
    for idx, char in enumerate(proc_data_one):
      if char in valid_char:
        continue
      else:
        char_chk = False
        break
  else:
    char_chk = False
  if char_chk:
    print("User input is an integer!")
  else:
    print("User input is NOT an integer")
#--------------------------------------------------------------
if __name__ == "__main__":
  input_string = input("Enter the data to be checked: ")
  isInteger(input_string)
  print("Thank you for using this app.")
#**************************************************************