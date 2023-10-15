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
formated_date = ""
month_dict = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,
              10:31, 11:30, 12:31}
conv_month = {1:"January", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September",
              10:"October", 11:"November", 12:"December"}
#--------------------------------------------------------------
def magic_date(usr_in1, usr_in2, usr_in3):
  if usr_in1 != 2:
    if usr_in2 <= month_dict.get(usr_in1):
      if usr_in1 * usr_in2 == usr_in3:
        formated_date = conv_month.get(usr_in1) + " " + str(usr_in2) + ", " + str(1900 + usr_in3)
    else:
      print("Invalid Data: Invalid Input Day")
      return
  else: 
    pRemYrs1 = (usr_in3 + 1900) % 400
    if pRemYrs1 != 0:
      pRemYrs2 = pRemYrs1 % 100
      if pRemYrs2 != 0:
        pRemYrs3 = pRemYrs2 % 4
        feb_days = 28 if pRemYrs3 != 0 else 29
      else:
        feb_days = 29
    else:
      feb_days = 29
    if usr_in2 <= feb_days:
      if usr_in1 * usr_in2 == usr_in3:
        formated_date = "February" + " " + str(usr_in2) + ", " + str(1900 + usr_in3)
    else:
      print("Invalid Data: Invalid Input Day")
      return
  return formated_date
#--------------------------------------------------------------
if __name__ == "__main__":
  print("This program will determine if the input date is a magic date.")
  user_in = input("Enter the month and day (e.g. 1 8 99): ")
  user_in_list = user_in.split()
  output_data = magic_date(int(user_in_list[0]), int(user_in_list[1]), int(user_in_list[2]))
  print("The date %s is a magic date." % output_data)
  print("Thank you for using this app.")
#**************************************************************