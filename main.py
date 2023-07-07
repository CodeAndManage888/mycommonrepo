#!/bin/bash
#**************************************************************
# Date: 063023   (Expected Solution with 22 Lines of Code)    *
# Title: Compute the Perimeter of a Polygon                   *
# Status: In Progress (In Progress / Testing / Working)       *
# Write a program that computes the perimeter of a polygon.   *
# Begin by reading the x and y values for the first point on  *
# the perimeter of the polygon from the user. Then continue   *
# reading pairs of x and y values until the user enters a     *
# blank line for the x-coordinate. Each time you read an      *
# additional coordinate you should compute the distance to    *
# the previous point and add it to the perimeter. When a      *
# blank line is entered for the x-coordinate your program     *
# should add the distance from the last point back to the     *
# first point to the perimeter. Then it should display the    *
# total perimeter. Sample input and output is shown below,    *
# with user input shown in bold:                              *
#                                                             *
# Enter the x part of the coordinate: 0                       *
# Enter the y part of the coordinate: 0                       *
# Enter the x part of the coordinate (blank to quit): 1       *
# Enter the y part of the coordinate: 0                       *
# Enter the x part of the coordinate (blank to quit): 0       *
# Enter the y part of the coordinate: 1                       *
# Enter the x part of the coordinate (blank to quit):         *
# The perimeter of the polygon is 3.414213562373095           *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import math
#--------------------------------------------------------------
UserInX, UserInY = ("", "")
XCoorList = []
YCoorList = []
NumXCoorList = []
NumYCoorList = []
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
def comp_length(PtX1, PtY1, PtX2, PtY2):
  fin_length = math.sqrt((PtX2**2 - PtX1**2) + (PtY2**2 - PtY1**2))
  return fin_length
#--------------------------------------------------------------
PtNum = 1
while UserInX != " ":
  if PtNum == 1:
    UserInX = input("Enter the X%s part of the coordinate: " % PtNum)
    XCoorList.append(UserInX)
    UserInY = input("Enter the Y%s part of the coordinate: " % PtNum)
    YCoorList.append(UserInY)
  else:
    UserInX = input("Enter the X%s part of the coordinate (blank to quit): " % PtNum)
    XCoorList.append(UserInX)
    if UserInX != " ":
      UserInY = input("Enter the Y%s part of the coordinate: " % PtNum)
      YCoorList.append(UserInY)
    else:
      YCoorList.append(UserInX)
  PtNum = PtNum + 1
#--------------------------------------------------------------
PtNum = 0
while XCoorList[PtNum] != " ":
  NumXCoorList.append(data_check(XCoorList[PtNum]))
  NumYCoorList.append(data_check(YCoorList[PtNum]))
  PtNum = PtNum + 1
  if icheck == -1:
    break
#--------------------------------------------------------------
PtNum, SampleSumX, SampleSumY = (0, 0, 0)
for ptsX in NumXCoorList:
  SampleSumX = SampleSumX + ptsX
for ptsY in NumYCoorList:
   SampleSumY = SampleSumY + ptsY
#--------------------------------------------------------------
print("--------------------To Be Deleted----------------------")
print(XCoorList)
print(YCoorList)
print(NumXCoorList)
print(NumYCoorList)
print("--------------------To Be Deleted----------------------")
print("Total Sum of X is %s." % SampleSumX)
print("Total Sum of Y is %s." % SampleSumY)
print("Thank you for using this app.")
#--------------------------------------------------------------
#**************************************************************