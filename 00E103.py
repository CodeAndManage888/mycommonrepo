#!/bin/bash
#**************************************************************
# Date: 092123 (Expected Solution with 26 Lines of Code)      *
# Title: Magic Dates                                          *
# Status: In Progress (In Progress / Testing / Working)       *
# A magic date is a date where the day multiplied by the      *
# month is equal to the two digit year. For example, June 10, *
# 1960 is a magic date because June is the sixth month, and 6 *
# times 10 is 60, which is equal to the two digit year. Write *
# a function that determines whether or not a date is a magic *
# date. Use your function to create a main program that ﬁnds  *
# and displays all of the magic dates in the 20th century.    *
# You will probably ﬁnd your solution to Exercise 100 helpful *
# when completing this exercise.                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
magic_dates_list = []
ctr = 0
#--------------------------------------------------------------
def magic_date(user_in):
  if usr_in1 != 2:
    final_data = month_dict.get(usr_in1)
  else:
    pRemYrs1 = usr_in2 % 400
    if pRemYrs1 != 0:
      pRemYrs2 = pRemYrs1 % 100
      if pRemYrs2 != 0:
        pRemYrs3 = pRemYrs2 % 4
        if pRemYrs3 != 0:
          final_data = 28
        else:
          final_data = 29
      else:
        final_data = 29
    else:
      final_data = 29
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  print("This program will display all magic dates in the 20th century.")
  user_in = input("Enter the month and day (e.g. January 8): ")
  while ctr <= len(magic_dates_list):
    print(magic_dates_list[ctr])
    ctr += 1
  print("Thank you for using this app.")
#**************************************************************
