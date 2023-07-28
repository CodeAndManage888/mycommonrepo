#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 47 Lines of Code)    *
# Title: Coin Flip Simulation                                 *
# Status: In Progress (In Progress / Testing / Working)       *
# What's the minimum number of times you have to flip a coin  *
# before you can have three consecutive flips that results in *
# the same outcome (either all three are heads or all three   *
# are tails)? What's the maximum number of flips that might   *
# be needed? How many flips are needed on average? In this    *
# exercise we will explore these questions by creating a      *
# program that simulates several series of coin flips.        *
# Create a program that uses Python's random number generator *
# to simulate flipping a coin several times. The simulated    *
# coins until either 3 consecutive heads or 3 consecutive     *
# tails occur. Display an H each time the outcome is heads,   *
# and a T each time the outcome is tails, with all of the     *
# outcomes shown of the same line. Then display the number of *
# flips needed to reach 3 consecutive flips with the same     *
# outcome. When your program is run it should perform the     *
# simulation 10 times and report the average number of flips  *
# needed. Sample output is shown below:                       *
# H T T T (4 flips)                                           *
# H H T T H T H T T H H T H T T H T T T (19 flips)            *
# T T T (3 flips)                                             *
# T H H H (4 flips)                                           *
# H H H (3 flips)                                             *
# T H T T H T H H T T H H T H T H H H (18 flips)              *
# H T T H H H (6 flips)                                       *
# T H T T T (5 flips)                                         *
# T T H T T H T H T H H H (12 flips)                          *
# T H T T T (5 flips)                                         *
# On Average, 7.9 flips were needed                           *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
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
print("Thank you for using this app.")
#**************************************************************