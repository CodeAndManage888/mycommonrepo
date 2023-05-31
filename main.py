#**************************************************************
# Date: 052923   (Expected Solution with 40 Lines of Code)    *
# Title: Season from Month and Day                            *
# Status: Testing (In Progress / Testing / Working)           *
# The year is divided into four seasons: spring, summer, fall *
# and winter. While the exact dates that the seasons change   *
# vary a little bit from year to year because of the way that *
# the calendar is constructed, we will use the following      *
# dates for this exercise:                                    *
# Season                First Day                             *
# Spring                March 20                              *
# Summer                June 21                               *
# Fall                  September 22                          *
# Winter                December 21                           *
# Create a program that reads a month and day from the user.  *
# The user will enter the name of the month as a string,      *
# followed by the day within the month as an integer. Then    *
# your program should display the season associated with the  *
# date that was entered.                                      *
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
ValMonList = ["January", "Jan", "january", "jan", "JANUARY", "JAN",
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
SpringMon = ["Apr", "May"]
SummerMon = ["Jul", "Aug"]
FallMon = ["Oct", "Nov"]
WinterMon = ["Jan", "Feb"]
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
if (iMonth in ValMonList):
  pFirstLtr = iMonth[0].capitalize()
  p2nd3rdLtr = iMonth[1:3].lower()
  pKeyString = pFirstLtr + p2nd3rdLtr
  valid_day = valid_day_dict[pKeyString]
  if (iDay != 0) and (iDay <= valid_day):
#--------------------------------------------------------------  
    if pKeyString in SpringMon:
      print("Condition 1: The season is Spring")
    elif (pKeyString == "Mar" and iDay >= 20) or (pKeyString == "Jun" and iDay < 21):
      print("Condition 2: The season is Spring")
    elif (pKeyString == "Mar" and iDay < 20):
      print("Condition 3: The season is Winter")
    elif pKeyString == "Jun" and iDay >= 21:
      print("Condition 4: The season is Summer")
  #--------------------------------------------------------------  
    elif pKeyString in SummerMon:
      print("Condition 5: The season is Summer")
    elif (pKeyString == "Jun" and iDay >= 21) or (pKeyString == "Sep" and iDay < 22):
      print("Condition 6: The season is Summer")
    elif (pKeyString == "Jun" and iDay < 21):
      print("Condition 7: The season is Spring")
    elif pKeyString == "Sep" and iDay >= 22:
      print("Condition 8: The season is Fall")
  #--------------------------------------------------------------  
    elif pKeyString in FallMon:
      print("Condition 9: The season is Fall")
    elif (pKeyString == "Sep" and iDay >= 22) or (pKeyString == "Dec" and iDay < 21):
      print("Condition 10: The season is Fall")
    elif (pKeyString == "Sep" and iDay < 21):
      print("Condition 11: The season is Summer")
    elif pKeyString == "Dec" and iDay >= 22:
      print("Condition 12: The season is Winter")
  #--------------------------------------------------------------    
    elif pKeyString in WinterMon:
      print("Condition 13: The season is Winter")
    elif (pKeyString == "Dec" and iDay >= 21) or (pKeyString == "Mar" and iDay < 20):
      print("Condition 14: The season is Winter")
    elif (pKeyString == "Dec" and iDay < 21):
      print("Condition 15: The season is Fall")
    elif pKeyString == "Mar" and iDay >= 20:
      print("Condition 16: The season is Spring")
    else:
      print("Condition 17: Invalid Input Date")
  else:
    print("Invalid Input Data - Invalid Day.")
else:
    print("Invalid Input Data - Invalid Month.")
print("Thank you for using this app.")
#**************************************************************
# Open Items:
#
# CHistory:
# C0529231700
# - started coding for exercise 46 and finalize requirement
# C0531231700
# - completed coding for exercise 46 and ready for testing (refactor)