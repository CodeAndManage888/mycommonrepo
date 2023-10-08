#!/bin/bash
#**************************************************************
# Date: 082423 (Expected Solution with 47 Lines of Code)      *
# Title: Days in a Month                                      *
# Status: Testing (In Progress / Testing / Working)           *
# Write a function that determines how many days there are in *
# a particular month. Your function will take two parameters: *
# The month as an integer between 1 and 12, and the year as a *
# four digit integer. Ensure that your function reports the   *
# correct number of days in February for leap years. Include  *
# a main program that reads a month and year from the user    *
# and displays the number of days in that month. You may ﬁnd  *
# your solution to Exercise 57 helpful when solving this      *
# problem.                                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
input_list = []
month_dict = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,
              10:31, 11:30, 12:31}
pRemYrs1, pRemYrs2, pRemYrs3 = 0, 0, 0
#--------------------------------------------------------------
def days_month(usr_in1, usr_in2):
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
  return final_data
#--------------------------------------------------------------
if __name__ == "__main__":
  user_inputs = input("Enter the month and the year e.g. 2 2000: ")
  input_list = user_inputs.split(" ")
  days_in_months = days_month(int(input_list[0]), int(input_list[1]))
  print("The number of days to the given month and year is %s" % days_in_months)
  print("Thank you for using this app.")
#**************************************************************
