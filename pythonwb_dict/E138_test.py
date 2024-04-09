#!/bin/bash
#**************************************************************
# Date: 032724 (Expected Solution with 58 Lines of Code)      *
# Title: Create a Bingo Card                                  *
# Status: Testing (In Progress / Testing / Working)           *
# A Bingo card consists of 5 columns of 5 numbers. The        *
# columns are labeled with the letters B,I,N,G and O. There   *
# are 15 numbers that can appear under each letter. In        *
# particular, the numbers that can appear under the B range   *
# from 1 to 15, the numbers that can appear under the I range *
# from 16 to 30, the numbers that can appear under the N range*
# from 31 to 45, and so on. Write a function that creates a   *
# random Bingo card and stores it in a dictionary. The keys   *
# will be the letters B,I,N,G and O. The values will be the   *
# lists of ﬁve numbers that appear under each letter. Write a *
# second function that displays the Bingo card with the       *
# columns labeled appropriately. Use these functions to write *
# a program that displays a random Bingo card. Ensure         *
# that the main program only runs when the ﬁle containing     *
# your solution has not been imported into another program.   *
# You may be aware that Bingo cards often have a “free” space *
# in the middle of the card. We won’t consider the free space *
# in this exercise.                                           *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def bingo_card_gen():
  import random
  bingo_card = {}
  bingo_card["B"] = random.sample(range(1,16),5)
  bingo_card["I"] = random.sample(range(16,31),5)
  bingo_card["N"] = random.sample(range(31,46),5)
  bingo_card["G"] = random.sample(range(46,61),5)
  bingo_card["O"] = random.sample(range(61,76),5)
  return bingo_card
#--------------------------------------------------------------
if __name__ == "__main__":
  bingo_card = bingo_card_gen()
  print("B\tI\tN\tG\tO")
  for i in range(5):
    print(bingo_card["B"][i],"\t",bingo_card["I"][i],"\t",bingo_card["N"][i],"\t",bingo_card["G"][i],"\t",bingo_card["O"][i])
  print("Thank you for using this app.")
#**************************************************************
