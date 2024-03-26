#!/bin/bash
#**************************************************************
# Date: 030124 (Expected Solution with 65 Lines of Code)      *
# Title: Write Out Numbers in English                         *
# Status: Testing (In Progress / Testing / Working)           *
# While the popularity of cheques as a payment method has     *
# diminished in recent years, some companies still issue them *
# to pay employees or vendors. The amount being paid normally *
# appears on a cheque twice, with one occurrence written      *
# using digits, and the other occurrence written using        *
# English words. Repeating the amount in two different forms  *
# makes it much more difﬁcult for an unscrupulous employee or *
# vendor to modify the amount on the cheque before depositing *
# it. In this exercise, your task is to create a function     *
# that takes an integer between 0 and 999 as its only         *
# parameter, and returns a string containing the English      *
# words for that number. For example, if the parameter to the *
# function is 142 then your function should return “one       *
# hundred forty two ”. Use one or more dictionaries to        *
# implement your solution rather than large if/elif/else      *
# constructs. Include a main program that reads an integer    *
# from the user and displays its value in English words.      *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def num_word(user_num):
  num_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
              5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 
              10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
              14: 'fourteen', 15: 'fifteen' , 16: 'sixteen', 
              17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 
              20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 
              60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
  if user_num < 20:
    return num_dict[user_num]
  elif user_num < 100:
    return num_dict[user_num // 10 * 10] + ' ' + num_dict[user_num % 10]
  elif user_num < 1000:
    return num_dict[user_num // 100] + ' hundred ' + num_word(user_num % 100)
  else:
    return 'Invalid number'
#--------------------------------------------------------------
if __name__ == "__main__":
  user_num = int(input("Please enter a number: "))
  print(num_word(user_num))
  print("Thank you for using this app.")
#**************************************************************