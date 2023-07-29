#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 18 Lines of Code)    *
# Title: Binary to Decimal                                    *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that converts a binary (base 2) number to   *
# decimal (base 10). Your program should begin by reading the *
# binary number from the user as a string. Then it should     *
# compute the quivalent decimal number by processing each     *
# digit in the binary number. Finally, your program should    *
# display the equivalent decimal number with an appropriate   *
# message.                                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
binary_digit_list = []
datachk = False
totsum, ctr = 0, 0
#--------------------------------------------------------------
BinaryNum = input("Enter the binary number: ")
for digit in BinaryNum:
  if digit == "1" or digit == "0":
     binary_digit_list.append(digit)
  else:
    print("Invalid input data! Data is not a binary number.")
    datachk = True
if datachk == False:
  binary_digit_list.reverse()
  while ctr < len(binary_digit_list):
    totsum += int(binary_digit_list[ctr]) * (2 ** ctr)
    ctr += 1
  print("The decimal equivalent of the binary number %s is %s" % (BinaryNum, totsum))
print("Thank you for using this app.")
#**************************************************************