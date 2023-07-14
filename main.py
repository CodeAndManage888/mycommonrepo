#!/bin/bash
#**************************************************************
# Date: 070823   (Expected Solution with 38 Lines of Code)    *
# Title: Admission Price                                      *
# Status: In Progress (In Progress / Testing / Working)       *
# A particular zoo determines the price of admission based on *
# the age of the guest. Guests 2 years of age and less are    *
# admitted without charge. Children between 3 and 12 years of *
# age cost $14.00. Seniors aged 65 years and over cost $18.00.*
# Admission for all other guests is $23.00.                   *
# Create a program that begins by reading the ages of all of  *
# the guests in a group from the user, with one age entered   *
# on each line. The user will enter a blank line to indicate  *
# that there are no more guests in the group. Then your       *
# program should display the admission cost for the group     *
# with an appropriate message. The cost should be displayed   *
# using two decimal places.                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck, GuestAge, cGuestAge, TotalCharge = (0, "", 0, 0.00)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
while GuestAge != " ":
  GuestAge = input("Input the age of the guess: ")
  if GuestAge != " ":
    cGuestAge = data_check(GuestAge)
    if icheck == -1:
      break
  if cGuestAge <= 2:
    TotalCharge = TotalCharge + 0.00
  elif cGuestAge >= 3 and cGuestAge <= 12:
    TotalCharge = TotalCharge + 14.00
  elif cGuestAge >= 65:
    TotalCharge = TotalCharge + 18.00
  else:
    TotalCharge = TotalCharge + 23.00
  print("Total admission cost is %s" % format(TotalCharge, '0.2f'))
print("Thank you for using this app.")
#**************************************************************