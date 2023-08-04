#!/bin/bash
#**************************************************************
# Date: 080123   (Expected Solution with 42 Lines of Code)    *
# Title: Median of Three Values                               *
# Status: Testing (In Progress / Testing / Working)           *
# Write a functions that takes three numbers as parameters,   *
# and returns the median value of these parameters as its     *
# result. Include a main program that reads three values from *
# the user and displays their median.                         *
# Hint: The median value is the middle of the three values    *
# when they are sorted into ascending order. It can be found  *
# using if statements, or with a little bit of mathematical   *
# creativity.                                                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
Input_List = []
DataCorrect = False
#--------------------------------------------------------------
def median_cal(UNum1, UNum2, UNum3):
  NumList = []
  NumList.append(UNum1)
  NumList.append(UNum2)
  NumList.append(UNum3)
  NumList.sort()
  return NumList[1]
#--------------------------------------------------------------
UserNum = input("Enter the three integer: ")
try:
  cUserNum = int(UserNum.replace(" ", ""))
  DataCorrect = True
except:
  DataCorrect = False
  print("Invalid input data! Numeric input data only.")
if DataCorrect:
  Input_List = UserNum.split()
  if len(Input_List) == 3:
    OutPrint = median_cal(Input_List[0], Input_List[1], Input_List[2])
    print("The median of numbers %s is %s" % (", ".join(Input_List), OutPrint))
print("Thank you for using this app.")
#**************************************************************