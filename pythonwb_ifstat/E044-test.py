#**************************************************************
# Date: 052623   (Expected Solution with 18 Lines of Code)    *
# Title: Date to Holiday Name                                 *
# Status: In Progress (In Progress / Testing / Working)       *
# Canada has three national holidays which fall on the same   *
# dates each year.                                            *
# Holiday            Date                                     *
# New Year's Day     January 1                                *
# Canada Day         July 1                                   *
# Christmas Day      December 25                              *
#                                                             *
# Write a program that reads a month and day from the user.   *
# If the month and day match one of the holidays listed       *
# previously then your program should display the holiday's   *
# name. Otherwise your program should indicate that the       *
# entered month and day do not correspond to the fixed-date   *
# holiday.                                                    *
# Canada has two additional national holidays, Good Friday    *
# and Labour Day, whose dates vary from year to year. There   *
# are also numerous provincial and territorial holidays, some *
# of which have fixed dates, and some of which have variable  *
# dates. We will not consider any of these additional         *
# holidays in this exercise.                                  *
#                                                             *
# Coder Additional Features:                                  *
# 1.) The program will be able to accept 1 format of the date *
#     but can distinguesh if it is written in upper or lower  *
#     case.                                                   *
# 2.) The program will only accept 1 input e.g. Jan 1 but no  *
#     year will be accepted.                                  *
# 3.) That program will be able to detect if the data is      *
#     valid or not e.g. Feb 30                                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
valid_day_dict = { 
   "Jan": 31,
   "Feb": 29,
   "Mar": 31,
   "Apr": 30,
   "May": 31,
   "Jun": 30,
   "Jul": 31,
   "Aug": 31,
   "Sep": 30,
   "Oct": 31,
   "Nov": 30,
   "Dec": 31
}
MonList = ["January", "Jan", "january", "jan", "JANUARY", "JAN",
           "February", "Feb", "february", "feb", "FEBRUARY", "FEB",
           "March", "Mar", "march", "mar", "MARCH", "MAR", "April", 
           "Apr", "april", "apr", "APRIL", "APR", "May", "may", "MAY", 
           "June", "Jun", "june", "jun", "JUNE", "JUN", "July", "Jul", 
           "july", "jul", "JULY", "JUL", "August", "Aug", "august", 
           "aug", "AUGUST", "AUG", "September", "Sep", "september", 
           "sep", "SEPTEMBER", "SEP", "October", "Oct", "october", 
           "oct", "OCTOBER", "OCT", "November", "Nov", "november", 
           "nov", "NOVEMBER", "NOV", "December", "Dec", "december", 
           "dec", "DECEMBER", "DEC"]
iMonDayOnly = " "
input_list = []
iMonth, iDay, pFirstLtr, p2nd3rdLtr, pKeyString = (" ", 0, " ",
                                                  " ", " ")
valid_day = 0
icheck = -1
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Integer input data only.")
    cUserIn1 = 0
    return cUserIn1
#--------------------------------------------------------------
iMonDayOnly = input("Enter the input date (Month & Day e.g. Jan 8): ")
input_list = iMonDayOnly.split()
iMonth = input_list[0]
iDay = data_check(input_list[1])
if iMonth in MonList:
  pFirstLtr = iMonth[0].capitalize()
  p2nd3rdLtr = iMonth[1:3].lower()
  pKeyString = pFirstLtr + p2nd3rdLtr
  valid_day = valid_day_dict[pKeyString]
  if iDay <= valid_day:
    if pKeyString == "Jan" and iDay == 1:
      print("It's New Year's Day")
    elif pKeyString == "Jul" and iDay == 1:
      print("It's Canada Day")
    elif pKeyString == "Dec" and iDay == 25:
      print("It's Christmas Day")
    else:
      print("The entered month and day do not correspond \
      to the fixed-date holiday")
  else:
    print("Invalid Input Data - Invalid day.")
else:
  print("Invalid Input Data - Invalid month.")
print("Thank you for using this app.")
#**************************************************************
# Open Items:
#
# CHistory:
# C0527231015
# - Finalize the requirement for exercise 44.
# C0528232030
# - Continued coding for exercise 44.
# C0529231600
# - 