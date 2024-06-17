#!/bin/bash
#**************************************************************
# Date: 051324 (Expected Solution with 26 Lines of Code)      *
# Title: Sum a List of Numbers                                *
# Status: In Progress (In Progress / Testing / Working)       *
# Create a program that sums all of the numbers entered by    *
# the user while ignoring any lines entered by the user that  *
# are not valid numbers. Your program should display the      *
# current sum after each number is entered. It should display *
# an appropriate error message after any invalid input, and   *
# then continue to sum any additional numbers entered by      *
# the user. Your program should exit when the user enters a   *
# blank line. Ensure that your program works correctly for    *
# both integers and ﬂoating point numbers. Hint: This         *
# exercise requires you to use exceptions without using ﬁles. *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
if __name__ == "__main__":
  input_nums = ""
  sum_nums = 0
  while input_nums != " ":
    input_nums = input("Enter a number or blank to exit: ")
    try:
      sum_nums += int(input_nums)
      print("Input Number:", input_nums, "Current Sum:", sum_nums)
    except:
      if input_nums == " ":
        print("Thank you for using this app.")
        break
      print("Invalid input")
      continue
#**************************************************************