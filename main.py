#!/bin/bash
#**************************************************************
# Date: 110323 (Expected Solution with 28 Lines of Code)      *
# Title: Random Lottery Numbers                               *
# Status: In Progress (In Progress / Testing / Working)       *
# In order to win the top prize in a particular lottery, one  *
# must match all 6 numbers on his or her ticket to the 6      *
# numbers between 1 and 49 that are drawn by the lottery      *
# organizer. Write a program that generates a random          *
# selection of 6 numbers for a lottery ticket. Ensure that    *
# the 6 numbers selected do not contain any duplicates.       *
# Display the numbers in ascending order.                     *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import random
lotto_num = []
#--------------------------------------------------------------
def gen_six_num():
  num_list = []
  ran_num = random.randint(1,49)
  while len(num_list) != 6:
    if ran_num not in num_list:
      num_list.append(ran_num)
      ran_num = random.randint(1,49)
    num_list.sort()
  return num_list
#--------------------------------------------------------------
if __name__ == "__main__":
  lotto_num = gen_six_num()
  print("The winning numbers are: %s" % ', '.join(map(str, lotto_num)))
  print("Thank you for using this app.")
#**************************************************************
