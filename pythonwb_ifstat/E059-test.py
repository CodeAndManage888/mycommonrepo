#**************************************************************
# Date: 061523   (Expected Solution with 28 Lines of Code)    *
# Title: Is a License Plate Valid?                            *
# Status: Testing (In Progress / Testing / Working)           *
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
val_ltr_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U",
                "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", 
                "n", "p", "q", "r", "s", "t", "v", "w", "x", "z",
                "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", 
                "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
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
def char_check(UserIn2):
  for character in UserIn2:
    if character not in val_ltr_list:
      return "Invalid input data! Not a valid character for this plate number version."
  return "Y"
#--------------------------------------------------------------
iPlateNum = input("Please provide a valid plate number e.g. ABC123 or 1234ABC: ")
if len(iPlateNum) == 6:
  iLtrPart = iPlateNum[0:3]
  print(iLtrPart)
  LtrIndMsg = char_check(iLtrPart)
  if LtrIndMsg != "Y":
    print(LtrIndMsg)
  else:
    iNumPart = data_check(iPlateNum[3:6])
    print(iNumPart)
    if icheck == 0:
      print("Input data valid for an older version plate number!")
elif len(iPlateNum) == 7:
  print(iPlateNum[0:4])
  iNumPart = data_check(iPlateNum[0:4])
  if icheck == 0:
    iLtrPart = iPlateNum[4:7]
    print(iLtrPart)
    LtrIndMsg = char_check(iLtrPart)
    if LtrIndMsg != "Y":
      print(LtrIndMsg)
    else:
      print("Input data valid for a newer version plate number!")
else:
  print("Invalid input data! Unexpected plate number length")
#**************************************************************