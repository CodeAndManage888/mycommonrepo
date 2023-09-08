#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 23 Lines of Code)    *
# Title: Shipping Calculator                                  *
# Status: Testing (In Progress / Testing / Working)           *
# An online retailer provides express shipping for many of    *
# its items at a rate of $10.95 for the first item, and $2.95 *
# for each subsequent item. Write a function that takes the   *
# number of items in the order as its only parameter. Return  *
# the shipping charge for the order as the function's result. *
# Include a main program that reads the number of items       *
# purchased from the user and displays the shipping charge.   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
DataCorrect = False
#--------------------------------------------------------------
def ship_chg(NoItems, FirstItem = 10.95, NextItems = 2.95):
  return ((NoItems - 1) * NextItems) + FirstItem
#--------------------------------------------------------------
UsrNoItems = input("Enter the total items for the order: ")
try:
  cUsrNoItems = int(UsrNoItems)
  DataCorrect = True
except:
  print("Invalid input data! Numeric input data only.")
if DataCorrect:
  print("The total shipping charge is $%s: " % format(ship_chg(cUsrNoItems),"0.2f"))
print("Thank you for using this app.")
#**************************************************************