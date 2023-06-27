#**************************************************************
# Date: 061423   (Expected Solution with 22 Lines of Code)    *
# Title: Next Day                                             *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that reads a date from the user and         *
# computes its immediate succcessor. For example, if the user *
# enters values that represent 2013-11-18 then your program   *
# should display a message indicating the day immediately     *
# after 2013-11-18 is 2013-11-19. If the user enter value     *
# represent 2013-11-30 then the program should indicate that  *
# the next day is 2013-12-01. If the user enter values that   *
# represent 2013-12-31 then the program should indicate that  *
# the next day is 2014-01-01. The date will be entered in     *
# numeric form with three separate input statements: one for  *
# the year, one for the month, and one for the day. Ensure    *
# that your program works correctly for leap years.           *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
iYear, iMonth, iDay, iCnvYear, pRemYrs1, pRemYrs2, pRemYrs3 = (" ", " ", " ", 0, 0, 0, 0)
ciYear, ciMonth, ciDay, con_input, data_chkd, YearCheck, MonthCheck= (0, 0, 0, 0, 0, " ", 0)
fin_year, fin_month, fin_day = (" ", " ", " ")
valid_day_dict = {"01": 31, "02": 29, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31,
   "08": 31, "09": 30, "10": 31, "11": 30, "12": 31}
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    cUserIn1 = -1
    return cUserIn1
#--------------------------------------------------------------
def leap_year(UserIn2):
  if len(UserIn2) <= 4:
    iCnvYear = data_check(UserIn2)
    if icheck == 0:
      pRemYrs1 = iCnvYear % 400
      if pRemYrs1 != 0:
        pRemYrs2 = pRemYrs1 % 100
        if pRemYrs2 != 0:
          pRemYrs3 = pRemYrs2 % 4
          if pRemYrs3 != 0:
            print("The %s year is not a leap year." % UserIn2)
            LeapYrInd = "N"
            return LeapYrInd
          else:
            print("The %s year is a leap year." % UserIn2)
            LeapYrInd = "Y"
            return LeapYrInd
        else:
          print("The %s year is a leap year." % UserIn2)
          LeapYrInd = "Y"
          return LeapYrInd
      else:
        print("The %s year is a leap year." % UserIn2)
        LeapYrInd = "Y"
        return LeapYrInd
  else:
    LeapYrInd = "X"
    return LeapYrInd
#--------------------------------------------------------------
iYear = input("Enter the input year. Numeric only e.g. 1999: ")
iMonth = input("Enter the input month. Numeric only e.g. 01: ")
iDay = input("Enter the input day. Numeric only e.g. 31: ")
con_input = iYear + iMonth + iDay
data_chkd = data_check(con_input)
if icheck == 0:
  ciDay = int(iDay)
  ciMonth = int(iMonth)
  ciYear = int(iYear)
  if len(iYear) == 4 and len(iMonth) == 2 and len(iDay) == 2:
    YearCheck = leap_year(iYear)
    MonthCheck = valid_day_dict[iMonth]
    if ciMonth == 2 and ciDay  == 28:
      if YearCheck == "Y":
        fin_month = iMonth
        fin_day = str(ciDay + 1)
        fin_year = iYear
      elif YearCheck == "N":
        fin_month = str(ciMonth + 1)
        fin_day = "01"
        fin_year = iYear
      else:
        print("Invalid Input Data. Invalid Input Data Length.")
    elif ciDay == 30 and ciMonth != 12:
      if MonthCheck == ciDay:
        fin_month = str(ciMonth + 1)
        fin_day = "01"
        fin_year = iYear
      else:
        print("Invalid data. Incorrect day for the month.")
    elif ciDay == 31 and ciMonth == 12:
        fin_month = "01"
        fin_day = "01"
        fin_year = str(ciYear + 1)
    elif (ciDay == 31 and ciMonth != 12) or (ciDay == 29 and ciMonth == 2):
      if YearCheck == "N" and ciMonth == 2:
        fin_month = str(ciMonth + 1)
        fin_day = "01"
        fin_year = iYear
      elif MonthCheck == ciDay:
        fin_month = str(ciMonth + 1)
        fin_day = "01"
        fin_year = iYear
      else:
        print("Invalid data. Incorrect day for the month.")
    else:
      fin_month = iMonth
      fin_day = str(ciDay + 1)
      fin_year = iYear
  else:
    print("Invalid Input Data. Data length is wrong.")     
else:
  print("Invalid input data! Integer input data only.")
print("The next day for the input date is %s-%s-%s" % (fin_year, fin_month, fin_day))
print("Thank you for using this app.")
#**************************************************************