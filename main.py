#!/bin/bash
#**************************************************************
# Date: 022624 (Expected Solution with 42 Lines of Code)      *
# Title: Two Dice Simulation                                  *
# Status: In Progress (In Progress / Testing / Working)       *
# In this exercise you will simulate 1,000 rolls of two dice. *
# Begin by writing a function that simulates rolling a pair   *
# of six-sided dice. Your function will not take any          *
# parameters. It will return the total that was rolled on two *
# dice as its only result. Write a main program that uses     *
# your function to simulate rolling two six-sided dice 1,000  *
# times. As your program runs, it should count the number of  *
# times that each total occurs. Then it should display a      *
# table that summarizes this data. Express the frequency for  *
# each total as a percentage of the total number of rolls.    *
# Your program should also display the percentage expected by *
# probability theory for each total. Sample output is shown   *
# below.                                                      *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def rollDice():
  import random
  return random.randint(1, 6) + random.randint(1, 6)
#--------------------------------------------------------------
if __name__ == "__main__":
  print("This is main program.")
  rolls = 1000
  roll_count = [0] * 11
  for i in range(rolls):
    roll_count[rollDice() - 2] += 1
  print("Roll\tCount\tExpected\tActual")
  for i in range(11):
    print(f"{i + 2}\t{roll_count[i]}\t{roll_count[i] / rolls * 100:.2f}%\t{(i + 2) / 36 * 100:.2f}%")
  print("Thank you for using this app.")
#**************************************************************
