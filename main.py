#!/bin/bash
#**************************************************************
# Date: 072623   (Expected Solution with 26 Lines of Code)    *
# Title: Decimal to Binary                                    *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that converts a decimal (base 10) number to *
# binary (base 2). Read the decimal number from the user as an*
# integer and then use the division algorithm shown below to  *
# perform the conversion. When the algorithm completes, result*
# contains the binary representation of the number. Display   *
# the result, along with an appropriate message.              *
#                                                             *
# Let result be an empty string                               *
# Let q represent the number to convert                       *
# repeat                                                      *
#    Set r equal to the remainder when q is divided by 2      *
#    Convert r to a string and add it to the beginning of     *
#    result                                                   *
#    Divide q by 2, discarding any remainder, and store the   *
#    result back into q                                       *
# until q is 0                                                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
Temp_Bin_List = []
Fin_Bin_Val = ""
InvDataChk = False
#--------------------------------------------------------------
try: 
  UserNum = int(input("Enter the input number: "))
  cUserNum = UserNum
except:
  print("Invalid input data! Numeric input data only.")
  InvDataChk = True
if InvDataChk == False:
  while cUserNum != 0:
    BinDgt = cUserNum % 2
    Temp_Bin_List.append(str(BinDgt))
    cUserNum //= 2
  Temp_Bin_List.reverse()
  for Bit in Temp_Bin_List:
    Fin_Bin_Val += Bit
  print("The binary equivalent of the decimal number %s is %s." % (UserNum, Fin_Bin_Val))
print("Thank you for using this app.")
#**************************************************************