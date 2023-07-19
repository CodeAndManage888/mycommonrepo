#!/bin/bash
#**************************************************************
# Date: 070823   (Expected Solution with 25 Lines of Code)    *
# Title: Parity Bits                                          *
# Status: Testing (In Progress / Testing / Working)           *
# A parity bit is a simple mechanism for detecting errors in  *
# data transmitted over an unreliable connection such as a    *
# telephone line. The basic idea is that an additional bit is *
# transmitted after each group of 8 bits so that a single bit *
# error in the transmission can be detected.                  *
# Parity bits can be computed for either even parity or odd   *
# parity. If even parity is selected then the parity bit that *
# is transmitted is chosen so that the total number of one    *
# bit transmitted (8 bits of data plus the parity bit) is     *
# even. When odd parity is selected the parity bit is chosen  *
# so that the total number of one bits transmitted is odd.    *
# Write a program that compute the parity bit for groups of 8 *
# bits entered by the user using even parity. Your program    *
# should read strings containing 8 bits until the user enters *
# a blank line. After each string is entered by the user your *
# program should display a clear message indicating whether   *
# the parity bit should be 0 or 1. Display an appropriate     *
# error message if the user enters something other than 8     *
# bits.                                                       *
#                                                             *
# Hint: You should read the input from the user as a string.  *
# Then you can use the count method to help you determine the *
# number of zeroes and ones in the string. Information about  *
# the count method is available online.                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
UserInputBits = ""
#--------------------------------------------------------------
while UserInputBits != " ":
  UserInputBits = input("Enter the 8 bits combination data for transmission: ")
  if len(UserInputBits) != 8 and UserInputBits != " ":
    print("Invalid data length for transmission.")
  else:
    if UserInputBits != " ":
      input_chk = UserInputBits.count("1") + UserInputBits.count("0")
      if input_chk == 8:
        total_bit = UserInputBits.count("1")
        odd_even_ind = total_bit % 2
        if odd_even_ind == 1:
          print("Parity bit should be 1.")
        else:
          print("Parity bit should be 0.")
      else:
        print("Invalid data. Use 1 and 0 only.")
print("Thank you for using this app.")
#**************************************************************