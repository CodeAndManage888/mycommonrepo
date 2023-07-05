#!/bin/bash
#**************************************************************
# Date: 063023   (Expected Solution with 18 Lines of Code)    *
# Title: Discount Table                                       *
# Status: Testing (In Progress / Testing / Working)           *
# A particular retailer is having a 60 percent off sale on a  *
# variety of discontinued products. The retailer would like   *
# to help its customers determine the reduced price of the    *
# merchandise by having a printed discount table on the shelf *
# that shows the original prices and the prices after the     *
# discount has been applied. Write a program that uses a loop *
# to generate this table, showing the orginal price. the      *
# discount amount, and the new price for purchase of $4.95,   *
# $9.95, $14.95, $19.95 and $25.95. Ensure that the discount  *
# amounts and the new prices are rounded to 2 decimal places  *
# when they are displayed.                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
price_list = [4.95, 9.95, 14.95, 19.95, 25.95]
#--------------------------------------------------------------
print("Orginal Price | Discount Amount | New Price")
print("-------------------------------------------")
for price in price_list:
  DiscountAmt = format((price * .6),'0.2f')
  NewPrice = format((price * 1.6), '0.2f')
  print("$ {:>11} | $ {:>13} | $ {:>7}".format(price, DiscountAmt, NewPrice)) #TAG02
print("-------------------------------------------")
print("Thank you for using this app.")
#--------------------------------------------------------------
#**************************************************************
# TAG02: 
# 1.) " $ {:<11}": This is the format specifier for the first 
# value (price). It consists of three parts:
#     -> " $": This is a literal string representing the dollar 
#     sign symbol followed by a space.
#     -> "{:<11}": This is the format specification. The < sign 
#     indicates left alignment, and 11 represents the width of 
#     the column (11 characters). The value will be left-aligned 
#     within this width.
#
# 2.) " | $ {:<13}": This is the format specifier for the second 
# value (DiscountAmt). Similar to the first part, it adds a "|" 
# character and a dollar sign symbol before the value. The :<13 
# specifies left alignment within a column width of 13 characters.
# 
# 3.) " | $ {:<10}": This is the format specifier for the third 
# value (NewPrice). Again, it adds a "|" character and a dollar 
# sign symbol before the value. The :<10 specifies left alignment 
# within a column width of 10 characters.