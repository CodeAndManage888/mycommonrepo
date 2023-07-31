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
import random
#--------------------------------------------------------------
CoinFlip = ["H","T"]
SumCollect = []
Ctr, ThreeTimes, TotCnt = 10, 1, 0
#--------------------------------------------------------------
while Ctr != 0:
  CoinToss = random.choice(CoinFlip)
  LastToss = CoinToss
  while ThreeTimes != 3:
    print(CoinToss," ", end="")
    CoinToss = random.choice(CoinFlip)
    if LastToss == CoinToss:
      ThreeTimes += 1
    else:
      ThreeTimes = 0
    TotCnt += 1
    LastToss = CoinToss
#  print(CoinToss," ", end="")
  print("(%s flips)" % TotCnt)
  SumCollect.append(TotCnt)
  TotCnt, ThreeTimes = 0, 0
  Ctr -= 1
AveFlip = sum(SumCollect) / 10
print("On Average, %s flips were needed to get 3 consecutive same result" % AveFlip)
print("Thank you for using this app.")
#**************************************************************