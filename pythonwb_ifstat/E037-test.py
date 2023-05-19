#**************************************************************
# Date: 051923  (Expected Solution with 31 Lines of Code)     *
# Title: Name that Shape                                      *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that determines the name of a shape from    *
# its number of sides. Read the number of sides from the user *
# and then report the appropriate name as part of a           *
# meaningful message. Your program should support shapes with *
# anywhere from 3 up to (and including) 10 sides. If a number *
# of sides outside of this range is entered then your program *
# should display an appropriate error message.                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
data_side_dict = { 
   3: "Triangle",
   4: "Quadrilateral",
   5: "Pentagon",
   6: "Hexagon",
   7: "Heptagon",
   8: "Octagon",
   9: "Nonagon",
  10: "Decagon"
}
iNumSidesOnly = " "
ciNumSidesOnly = 0
fin_data = " "
icheck = -1
#--------------------------------------------------------------
def data_check(UserIn1, cUserIn1):
  global icheck
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return UserIn1, cUserIn1
  except:
    print("Invalid input data! Integer input data only.")
    print("Thank you for using this app.")
    return UserIn1, cUserIn1
#--------------------------------------------------------------    
iNumSidesOnly = input("How many sides does the shape have(Integer Only)?==> ")
if len(iNumSidesOnly) > 2:
  print("Invalid input data! Up to two charater data only.")
  print("Thank you for using this app.")
else:
  iNumSidesOnly, ciNumSidesOnly = data_check(iNumSidesOnly, ciNumSidesOnly)
  if not (3 <= ciNumSidesOnly <= 10):
    if ciNumSidesOnly != 0 and icheck == 0:
      print("'" + iNumSidesOnly + "'" + " is an invalid input data(3 to 10 sides only).")
      print("Thank you for using this app.")
  else:
    fin_data = data_side_dict[ciNumSidesOnly]
    print("The shape's name with " + "'" + iNumSidesOnly + "'" + " sides is " + fin_data + ".")
    print("Thank you for using this app.")
#**************************************************************
# Open Items:
#
# CHistory:
# c0519231430
# - completed the code for exercise 37.