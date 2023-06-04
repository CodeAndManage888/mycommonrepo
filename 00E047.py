#**************************************************************
# Date: 052923   (Expected Solution with 47 Lines of Code)    *
# Title: Birth Date to Astrological Sign                      *
# Status: In Progress (In Progress / Testing / Working)       *
# The horoscopes commonly reported in newspapers use the      *
# position of the sund at the time of one's birth to try and  *
# predict the future. This system of astrology divides the    *
# year into twelve zodia signs, as outline in the table       *
# below:                                                      *
#                                                             *
# Zodiac Sign                  Date Range                     *
# -----------                  --------------------------     *
# Capricorn                    December 22 to January 19      *
# Aquarius                     January 20 to February 18      *
# Pisces                       February 19 to March 20        *
# Aries                        March 21 to April 19           *
# Taurus                       April 20 to May 20             *
# Gemini                       May 21 to June 20              *
# Cancer                       June 21 to July 22             *
# Leo                          July 23 to August 22           *
# Virgo                        August 23 to September 22      *
# Libra                        September 23 to October 22     *
# Scorpio                      October 23 to November 21      *
# Sagitarius                   November 22 to December 21     *
#                                                             *
# Write a program that asks the user to enter his or her      *
# month and day of birth. Then your program should report the *
# user's zodiac sign as part of an appropriate output message *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
valid_sign_dict = { 
   "Jan": "Cap0119", "Aqu2031",
   "Feb": "Aqu0118", "Pis1929",
   "Mar": "Pis0120", "Ari2131",
   "Apr": "Ari0119", "Tau2030",
   "May": "Tau0120", "Gem2131",
   "Jun": "Gem0120", "Can2130",
   "Jul": "Can0122", "Leo2331",
   "Aug": "Leo0122", "Vir2331",
   "Sep": "Vir0122", "Lib2330",
   "Oct": "Lib0122", "Sco2331",
   "Nov": "Sco0121", "Sag2230",
   "Dec": "Sag0121", "Cap2231"
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
iMonDayOnly = " "
input_list = []
sign_duration_list = []
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