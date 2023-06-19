#**************************************************************
# Date: 060223   (Expected Solution with 28 Lines of Code)    *
# Title: Assessing Employees                                  *
# Status: In Progress (In Progress / Testing / Working)       *
# At a particular company, employees are rated at the end of  *
# each year. The rating scale begins at 0.0, with higher      *
# values indicating better performance and resulting in       *
# larger raises. The value awarded to an employee is either   *
# 0.0, 0.4, or 0.6 or more. Values between 0.0 and 0.4, and   *
# between 0.4 and 0.6 are never used. The meaning associated  *
# with each rating is shown in the following table. The       *
# amount of an employee's raise is $2400.00 multiplied by     *
# their rating.                                               *
#                                                             *
# Rating              Meaning                                 *
# -----------         ---------------------------             *
# 0.0                 Unacceptable performance                *
# 0.4                 Acceptable performance                  *
# 0.6 or more         Meritorious performance                 *
#                                                             *
# Write a program that reads a rating from the user and       *
# indicates whether the performance was unacceptable,         *
# acceptable or meritorious. The amount of the employee's     *
# raise should also be reported. Your program should display  *
# an appropriate error message if an invalid rating is        *
# entered. 
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
rating_dict = {
   0.0: "Unacceptable Performance", 0.4: "Acceptable Performance", 
   0.6: "Meritorious Performance", 0.7: "Meritorious Performance",
   0.8: "Meritorious Performance", 0.9: "Meritorious Performance"}
ValRatingList = [0.0, 0.4, 0.6, 0.7, 0.8, 0.9]
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
iGradePts = input("What is the employee ratings(numeric only)? ==> ")
ciGradePts = data_check(iGradePts)
if icheck == 0:
  fin_key = ValRatingList
  fin_grade = letter_grade_dict[fin_key]
  print("The %s grade point(s) is equivalent to %s letter grade." % (ciGradePts, fin_grade))
else:
  print("The %s grade point(s) is invalid." % iGradePts)
print("Thank you for using this app.")
#**************************************************************