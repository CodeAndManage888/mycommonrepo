#**************************************************************
# Date: 052323   (Expected Solution with 20 Lines of Code)    *
# Title: Name that Triangle                                   *
# Status: Testing (In Progress / Testing / Working)           *
# A triangle can be classified based on the lengths of its    *
# sides as equilateral, isosceles, or scalene. All 3 side of  *
# an equilateral triangle have the same length. An isosceles  *
# triangle has two sides that are the same lengths, and a     *
# third side that is a different length. If all of the sides  *
# have different lengths then the triangle is scalene.        *
# Write a program that reads the lengths of 3 sides of a      *
# triangle from the user. Display a message indicating the    *
# types of the triangle.                                      *
#                                                             *
# Coder Additional Features:                                  *
# 1.) The program will one use one input prompt and will      *
# extract the 3 data from one field.                          *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
no_spaces = " "
side_list = []
side_a, side_b, side_c, cUserIn1 = (0, 0, 0, 0)
pCombIn = 0
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
i3TriSides = input("Input the length of the 3 sides of the triangle e.g. (1, 3, 4)==> ")
no_spaces = i3TriSides.replace(" ","")
pCombIn = data_check(no_spaces)
if (icheck == 0):
  side_list = i3TriSides.split()
  if len(side_list) == 3:
    side_a, side_b, side_c = [int(side) for side in side_list]
    if (side_a != 0) and (side_b != 0) and (side_c != 0):
      if (side_a == side_b) and (side_a == side_c) and (side_b == side_c):
        print("The triangle is an equilateral triangle.")
      else:
        if (side_a != side_b) and (side_a != side_c) and (side_b != side_c):
          print("The triangle is a scalene triangle.")
        else:
          print("The triangle is an isosceles triangle.")
    else:
      print("Invalid input data! Please use a non zero data.")
  else:
    print("Incomplete number of sides. Three sides are required.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************