#**************************************************************
# Date: 052923   (Expected Solution with 22 Lines of Code)    *
# Title: What Color is that Square                            *
# Status: Testing (In Progress / Testing / Working)           *
# Positions on a chess board are identified by a letter and a *
# number. The letter identifies the column, while the number  *
# identifies the row.                                         *
# Write a program that reads a position from the user. Use an *
# if statement to determine if the column begins with a black *
# square or a white square. Then use modular arithmetic to    *
# report the color of the square in that row. For example, if *
# the user enters a1 then your program should report that the *
# square is black. If the user enters d5 then yur program     *
# should report the square is white. Your program may assume  *
# that a valid position will alwaqys be entered. It does not  *
# need to perform any error checking                          *
#                                                             *
# Coder Additional Features:                                  *
# 1.) The program will be able to validate the input data and *
#     display an error message.                               *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
valid_column = ("a", "b", "c", "d", "e", "f", "g", "h",
                "A", "B", "C", "D", "E", "F", "G", "H")
black_column_start = ("a", "A", "c", "C", "e", "E", "g", "G")
white_column_start = ("b", "B", "d", "D", "f", "F", "h", "H")
iCol, iRow, pOddEvenInd, final_value, icheck = (" ", 0, 0, " ", -1)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid Data - 2nd character must be integer.")
    cUserIn1 = 0
    return cUserIn1
#--------------------------------------------------------------
iPosition = input("Please provide a valid chess position e.g. a1: ")
iCol, iRow = iPosition[0], data_check(iPosition[1])
if icheck == 0:
  if iCol in valid_column:
    if iCol in black_column_start:
      if (0 < iRow < 9):
        pOddEvenInd = iRow % 2
        if pOddEvenInd == 1:
          final_value = iCol.lower() + iPosition[1]
          print("The chess position %s is black." % final_value)
      else:
        print("Invalid Data - Incorrect Row Number")
    else:
      if (0 < iRow < 9):
        pOddEvenInd = iRow % 2
        if pOddEvenInd == 1:
          final_value = iCol.lower() + iPosition[1]
          print("The chess position %s is white." % final_value)
      else:
        print("Invalid Data - Incorrect Row Number")
  else:
    print("Invalid Data - Incorrect Column Letter")
print("Thank you for using this app.")
#**************************************************************