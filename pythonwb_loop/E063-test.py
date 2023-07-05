#!/bin/bash
#**************************************************************
# Date: 063023   (Expected Solution with 22 Lines of Code)    *
# Title: Temperature Conversion Table                         *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that displays a temperature conversion      *
# table for degrees Celsius and degrees Fahrenheit. The table *
# should include rows for all temperature between 0 and 100   *
# degrees Celsius that are multiples of 10 degrees Celsius.   *
# Include appropriate heading on your columns. The formula    *
# for converting between degrees Celsius and degrees          *
# Fahrenheit can be found on the internet.                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
print("Degree Celsius | Degree Fahrenheit")
print("----------------------------------")
DegCel = 00.00
while DegCel < 100.00:
  DegFah = format(((9/5)*DegCel + 32), "0.2f")
  print("{:>14} | {:>17}".format(format(DegCel, "0.2f"), DegFah))
  DegCel = DegCel + 10.00
print("----------------------------------")
print("Thank you for using this app.")
#**************************************************************