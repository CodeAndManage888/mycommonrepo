#**************************************************************
# Date: 061523   (Expected Solution with 28 Lines of Code)    *
# Title: Is a License Plate Valid?                            *
# Status: In Progress (In Progress / Testing / Working)       *
# In a particular jurisdiction, older license plates consist  *
# of three uppercase letters followed by three numbers. When  *
# all of the license plates following that pattern had been   *
# used, the format was changed to four numbers followed by    *
# three uppercase letters.                                    *
# Write a program that begins by reading a string of          *
# characters from the user. Then your program should display  *
# a message indicating whether the characters are valid for   *
# an older style license plate or a newer style license plate.*
# Your program should display an appropriate message if the   *
# string entered by the user is not valid for either style of *
# license plate.                                              *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
iPlateNum = input("Please provide a valid plate number e.g. 123ABC or 1234ABC: ")
if len(iPlateNum) == 6:
  iNumPart = data_check(iPlateNum[])
  iLtrPart = iPlateNum[]
elif len(iPlateNum) == 7:
  iNumPart = data_check(iPlateNum[])
  iLtrPart = iPlateNum[]
else:
  print("Invalid input data! Unexpected plate number length")
#**************************************************************