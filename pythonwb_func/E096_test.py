#!/bin/bash
#**************************************************************
# Date: 081723 (Expected Solution with 40 Lines of Code)      *
# Title: Check a Password                                     *
# Status: Testing (In Progress / Testing / Working)           *
# In this exercise you will write a function that determines  *
# whether or not a password is good. We will deﬁne a good     *
# password to be a one that is at least 8 characters long and *
# contains at least one uppercase letter, at least one        *
# lowercase letter, and at least one number. Your function    *
# should return true if the password passed to it as its only *
# parameter is good. Otherwise it should return false.        *
# Include a main program that reads a password from the user  *
# and reports whether or not it is good. Ensure that your     *
# main program only runs when your solution has not been      *
# imported into another file                                  *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def password_chk(user_in):
  valid_ind = 0
  up_case, low_case, num_case = False, False, False
  if len(user_in) >= 8:
    len_correct = True
  for char in user_in:
    val_chck = ord(char)
    if val_chck >= 65 and val_chck <= 90:
      up_case = True
    elif val_chck >= 97 and val_chck <= 122:
      low_case = True
    elif val_chck >= 48 and val_chck <= 57:
      num_case = True
    else:
      continue
  if len_correct and up_case and low_case and num_case:
    valid_ind = 1
  else:
    valid_ind = 0
  return valid_ind
#--------------------------------------------------------------
if __name__ == "__main__":
  user_password = input("Please enter the password to check: ")
  if password_chk(user_password) == 1:
    print("Passed. The password meets all the 3 requirements")
  else:
    print("Failed. The password did not meet all the requirements")
  print("Thank you for using this app.")
#**************************************************************