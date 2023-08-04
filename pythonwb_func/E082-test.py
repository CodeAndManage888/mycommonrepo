#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 22 Lines of Code)    *
# Title: Taxi Fare                                            *
# Status: Testing (In Progress / Testing / Working)           *
# In a particular jurisdiction, taxi fares consist of a base  *
# fare of $4.00, plus $0.25 for every 140 meters traveled.    *
# Write a function that takes the distance traveled (in       *
# kilometers) as its only parameter and returns the total     *
# fare as its only result. Write a main program that          *
# demonstrates the function.                                  *
# Hint: Taxi fares change over time. Use constants to         *
# represent the base fare and the variable portion of the     *
# fare so that the program can be updated easily when the     *
# rates increase.                                             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
DataCorrect = False
#--------------------------------------------------------------
def taxi_fare(Distance, Base = 4.00, Per140Mtrs = 0.25):
  return ((Distance / .14) * Per140Mtrs) + Base
#--------------------------------------------------------------
UserDis = input("Enter the distance traveled in kilometers: ")
try:
  cUserDis = int(UserDis)
  DataCorrect = True
except:
  print("Invalid input data! Numeric input data only.")
if DataCorrect:
  print("The total taxi fare is $%s: " % format(taxi_fare(cUserDis),"0.2f"))
print("Thank you for using this app.")
#**************************************************************