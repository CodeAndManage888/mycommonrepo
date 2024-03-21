#!/bin/bash
#**************************************************************
# Date: 022924 (Expected Solution with 15 Lines of Code)      *
# Title: Morse Code                                           *
# Status: Testing (In Progress / Testing / Working)           *
# Morse code is an encoding scheme that uses dashes and dots  *
# to represent numbers and letters. In this exercise, you     *
# will write a program that uses a dictionary to store the    *
# mapping from letters and numbers to Morse code. Use a       *
# period to represent a dot, and a hyphen to represent a      *
# dash. The mapping from letters and numbers to dashes and    *
# dots is shown in Table 6.1. Your program should read a      *
# message from the user. Then it should translate each letter *
# and number in the message to Morse code, leaving a space    *
# between each sequence of dashes and dots. Your program      *
# should ignore any characters that are not letters or        *
# numbers. The Morse code for Hello, World! is shown below:   *
# .... . .-.. .-.. --- .-- --- .-. .-.. -.. Table 6.1 Morse   *
# Code Letters and Numbers Letter Code Letter Code Letter     *
# Code Number Code A.- J.--- S... 1 .---- B-... K-.- T- 2     *
# ..--- C-.-. L.-.. U..- 3 ...-- D-.. M-- V...- 4 ....- E.    *
# N-. W.-- 5 ..... F..-. O--- X-..- 6 -.... G--. P.--. Y-.--  *
# 7 --... H.... Q--.- Z--.. 8 ---.. I.. R.-. 0----- 9 ----.   *
# Morse code was originally developed in the nineteenth       *
# century for use over telegraph wires. It is still used      *
# today, over 160 years after it was ﬁrst created.            *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def conv_morse(user_in):
  final_morse_msg = ""
  morse_code = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", 
                "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", 
                "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", 
                "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
                "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", 
                "Z":"--..", "0":"-----", "1":".----", "2":"..---", 
                "3":"...--", "4":"....-", "5":".....", "6":"-....", 
                "7":"--..." , "8":"---..", "9":"----."}
  for ltr in user_in:
    if ltr in morse_code:
      final_morse_msg += morse_code[ltr] + " "
  return final_morse_msg
#--------------------------------------------------------------
if __name__ == "__main__":
  user_msg = input("Enter a message: ")
  user_msg = user_msg.upper()
  print(conv_morse(user_msg))
  print("Thank you for using this app.")
#**************************************************************