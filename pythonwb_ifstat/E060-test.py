#!/bin/python3
#**************************************************************
# Date: 061523   (Expected Solution with 45 Lines of Code)    *
# Title: Roulette Payouts                                     *
# Status: Testing (In Progress / Testing / Working)           *
# A roulette wheel has 38 spaces on it. Of these spaces, 18   *
# are black, 18 are red, and two are green. The green spaces  *
# are numbered 0 and 00. The red spaces are numbered 1, 3, 5, *
# 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 and    *
# 36. The remaining integers between 1 and 36 are used to     *
# number the black spaces.                                    *
# Many different bets can be placed in roulette. We will only *
# consider the following subset of them in this exercise:     *
#                                                             *
# a. Single number (1 to 36, 0, or 00)                        *
# b. Red versus Black                                         *
# c. Odd versus Even (Note that 0 and 00 do not pay out for   *
# even)                                                       *
# d. 1 to 18 versus 19 to 36                                  *
#                                                             *
# Write a program that simulates a spin of a roulette wheel   *
# by using Python's random number generator. Display the      *
# number that was selected and all of the bets that must be   *
# payed. For example, if 13 is selected then your program     *
# should display:                                             *
#                                                             *
# The spin resulted in 13 . . .                               *
# Pay 13                                                      *
# Pay Black                                                   *
# Pay Odd                                                     *
# Pay 1 to 18                                                 *
#                                                             *
# If the simulation results in 0 or 00 then your program      *
# should display Pay 0 or Pay 00 without any further output.  *
# Computed Result Validated:                                  *
#**************************************************************
import random
import time
status_bar = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
green_num_list = ["0", "00"]
red_num_list = ["1", "3", "5", "7", "9", "12", "14", "16", "18",
                "19", "21", "23", "25", "27", "30", "32", "34", 
                "36"]
black_num_list = ["2", "4", "6", "8", "10", "11", "13", "15", 
                  "17", "20", "22", "24", "26", "28", "29", "31",
                  "33", "35"]
odd_num_list = ["0", "00", "1", "3", "5", "7", "9", "11", "13", 
                "15", "17", "19", "21", "23", "25", "27", "29", 
                "31", "33", "35"]
even_num_list = ["2", "4", "6", "8", "10", "12", "14", "16", 
                 "18", "20", "22", "24", "26", "28", "30", "32", 
                 "34", "36"]
first_half_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", 
                   "10", "11", "12", "13", "14", "15", "16", "17",
                   "18"]
second_half_list = ["19", "20", "21", "22", "23", "24", "25", 
                    "26", "27", "28", "29", "30", "31", "32", "33", 
                    "34", "35", "36"]
sing_num_list = ["0", "00", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                 "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                 "31", "32", "33", "34", "35", "36"]
#--------------------------------------------------------------
print("Roulette Wheel is now closed for bets!")
#time.sleep(5)
print("Roulette Wheel is spining: ", end = "")
for character in status_bar:
  print(character, end = "")
  time.sleep(2)
print("\n")
selected_number = random.choice(sing_num_list)
print("The spin resulted in %s" % selected_number)
print("Please pay the following: ")
print("a.) Pay bets for %s" % selected_number)
if selected_number in green_num_list:
  print("b.) Pay bets for 0 or 00")
if selected_number in red_num_list:
  print("b.) Pay bets for red")
if selected_number in black_num_list:
  print("b.) Pay bets for black")
if selected_number in odd_num_list:
  print("c.) Pay bets for odd")
if selected_number in even_num_list:
  print("c.) Pay bets for even")
if selected_number in first_half_list:
  print("d.) Pay bets for 1 to 18")
if selected_number in second_half_list:
  print ("d.) Pay bets for 19 to 36")
print("Thank you for using this app.")
#**************************************************************
