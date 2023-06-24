#**************************************************************
# Date: 061323   (Expected Solution with 44 Lines of Code)    *
# Title: Cell Phone Bill                                      *
# Status: In Progress (In Progress / Testing / Working)       *
# A particular cell phone plan includes 50 minutes of air     *
# time and 50 text messages for $15.00 a month. Each          *
# additional minute of air time costs $0.25, while additional *
# text messages cost $0.15 each. All cell phone bills include *
# an additional charge of $0.44 to support 911 call centers,  *
# and the entire bill (including the 911 charge) is subject   *
# to 5 percent sales tax.                                     *
#                                                             *
# Write a program that read the number of minutes and text    *
# messages used in a month from the user. Display the base    *
# charge, additional minutes charge (if any), additional text *
# message charge (if any), the 911, tax and total bill amount.*
# Only display the additional minute and text message charges *
# if the user incurred costs in these categories. Ensure that *
# all of the charges are displayed using 2 decimal places.    *
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
iNoMin = input("How many minutes consumed this month? Numeric only e.g. (1, 3, 4)==> ")
iNoMsg = input("How many messages consumed this month? Numeric only e.g. (1, 3, 4)==> ")
piNoMin = data_check(iNoMin)
if icheck == 0:
  if piNoMin <= 50:
    print("The Total Bill for this Month")
    print("-----------------------------")
    print("")
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