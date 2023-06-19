#**************************************************************
# Date: 060123   (Expected Solution with 47 Lines of Code)    *
# Title: Grade Points to Letter Grade                         *
# Status: Testing (In Progress / Testing / Working)           *
# In the previous exercise you created a program that         *
# converts a letter grade into the equivalent number of grade *
# points. In this exercise you will create a program that     *
# reverses the process and converts from a grade point value  *
# entered by the user to a letter grade. Ensure that your     *
# program handles grade point values that fall between letter *
# grades. These should be rounded to the closest letter       *
# grade. Your program should report A+ for a 4.0 (or greater) *
# grade point average.                                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
letter_grade_dict = {
   4.0: "A+", 4.0: "A", 3.7: "A-", 3.3: "B+", 3.0: "B", 2.7: "B-",
   2.3: "C+", 2.0: "C", 1.7: "C-", 1.3: "D+", 1.0: "D", 0.0: "F"}
ValGrdPtsList = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 
                 1.0, 0.0]
iGradePts, icheck, ciGradePts, fin_grade = (0.0, -1, 0.0, " ")
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = float(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
def fnd_closest_val(UserIn2, ValList):
  return min(ValList, key=lambda x: abs(x - UserIn2)) # TAG001
#--------------------------------------------------------------
iGradePts = input("What is the grade points(numeric only)? ==> ")
ciGradePts = data_check(iGradePts)
if icheck == 0:
  fin_key = fnd_closest_val(ciGradePts, ValGrdPtsList)
  fin_grade = letter_grade_dict[fin_key]
  print("The %s grade point(s) is equivalent to %s letter grade." % (ciGradePts, fin_grade))
else:
  print("The %s grade point(s) is invalid." % iGradePts)
print("Thank you for using this app.")
#**************************************************************
# TAG001: what this line of code does is: it calculates the 
# absolute difference between UserIn2 and each item in the list 
# ValList, and it then returns the item from ValList for which 
# this difference is smallest. In other words, it finds the item 
# in ValList that is closest to UserIn2.