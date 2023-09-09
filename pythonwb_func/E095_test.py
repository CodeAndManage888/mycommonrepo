#!/bin/bash
#**************************************************************
# Date: 081523 (Expected Solution with 45 Lines of Code)      *
# Title: Random License Plate                                 *
# Status: Testing (In Progress / Testing / Working)           *
# In a particular jurisdiction, older license plates consist  *
# of three letters followed by three numbers. When all of the *
# license plates following that pattern had been used, the    *
# format was changed to four numbers followed by three        *
# letters. Write a function that generates a random license   *
# plate. Your function should have approximately equal odds   *
# of generating a sequence of characters for an old license   *
# plate or a new license plate. Write a main program that     *
# calls your function and displays the randomly generated     *
# license plate.                                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import random
#--------------------------------------------------------------
def gen_plate_num():
  comb_value = ""
  ctr = 4
  while ctr != 0:
    comb_value += str(random.randint(0, 9))
    ctr -= 1
  ctr = 3
  while ctr != 0:
    comb_value += chr(random.randint(65, 90))
    ctr -= 1
  return comb_value
#--------------------------------------------------------------
if __name__ == "__main__":
  print("The generated new plate number is", gen_plate_num())
  print("Thank you for using this app.")
#**************************************************************