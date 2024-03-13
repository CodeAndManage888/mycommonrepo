#!/bin/bash
#**************************************************************
# Date: 022624 (Expected Solution with 21 Lines of Code)      *
# Title: Text Messaging                                       *
# Status: In Progress (In Progress / Testing / Working)       *
# On some basic cell phones, text messages can be sent using  *
# the numeric keypad. Because each key has multiple letters   *
# associated with it, multiple key presses are needed for     *
# most letters. Pressing the number once generates the ﬁrst   *
# letter on the key. Pressing the number 2, 3, 4 or 5 times   *
# generates the second, third, fourth or ﬁfth character       *
# listed for that key. Key Symbols 1 .,?!: 2 ABC 3 DEF 4 GHI  *
# 5 JKL 6 MNO 7 PQRS 8 TUV 9 WXYZ 0 space. Write a program    *
# that displays the key presses that must be made to enter a  *
# text message read from the user. Construct a dictionary     *
# that maps from each letter or symbol to the key presses.    *
# Then use the dictionary to generate and display the presses *
# for the user’s message. For example, if the user enters     *
# Hello ,World! then your program should output               *
# 4433555555666110966677755531111 . Ensure that your program  *
# handles both uppercase and lowercase letters. Ignore any    *
# characters that aren’t listed in the table above such as    *
# semicolons and brackets.                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def convKeyPad(user_input):
  key_pad = {1:".,?!:", 2:"ABCabc", 3:"DEFdef", 4:"GHIghi",
             5:"JKLjkl",6:"MNOmno", 7:"PQRSpqrs", 8:"TUVtuv",
             9:"WXYZwxyz", 0:" "}
  num_seq = ""
  for char in user_input:
    ctr = 0
    while ctr < len(key_pad):
      print("Key:", ctr,"Value:", key_pad[ctr])
      if char in key_pad[ctr]:
        for c in key_pad[ctr]:
          times = 1
          if c == char:
            num_seq += str(ctr) * (times)
            break
          times += 1         
#       num_seq += str(ctr) * (char.index(key_pad[ctr]) + 1)
        print(num_seq)
        break
      ctr += 1
  return num_seq
#--------------------------------------------------------------
if __name__ == "__main__":
  user_string = input("Enter your text message: ")
  print("Press these numbers:",convKeyPad(user_string))
  print("Thank you for using this app.")
#**************************************************************
