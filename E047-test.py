#**************************************************************
# Date: 052923   (Expected Solution with 47 Lines of Code)    *
# Title: Birth Date to Astrological Sign                      *
# Status: Testing (In Progress / Testing / Working)           *
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
comp_sign_dict = {
   "Cap": "Capricorn",
   "Aqu": "Aquarius",
   "Pis": "Pisces",
   "Ari": "Aries",
   "Tau": "Taurus",
   "Gem": "Gemini",
   "Can": "Cancer",
   "Leo": "Leo",
   "Vir": "Virgo",
   "Lib": "Libra",
   "Sco": "Scorpio",
   "Sag": "Sagitarius"
}
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
valid_sign_dict = { 
   "Jan": ["Cap0119", "Aqu2031"],
   "Feb": ["Aqu0118", "Pis1929"],
   "Mar": ["Pis0120", "Ari2131"],
   "Apr": ["Ari0119", "Tau2030"],
   "May": ["Tau0120", "Gem2131"],
   "Jun": ["Gem0120", "Can2130"],
   "Jul": ["Can0122", "Leo2331"],
   "Aug": ["Leo0122", "Vir2331"],
   "Sep": ["Vir0122", "Lib2330"],
   "Oct": ["Lib0122", "Sco2331"],
   "Nov": ["Sco0121", "Sag2230"],
   "Dec": ["Sag0121", "Cap2231"]
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
sdata1, start1, end1, sdata2, start2, end2, final_sign = (" ", 0, 0, " ", 0, 0, " ")
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
    sign_duration_list = valid_sign_dict[pKeyString]
    sign_data1, sign_data2 = sign_duration_list[0],  sign_duration_list[1]
    sdata1, start1, end1 = sign_data1[0:3], int(sign_data1[3:5]), int(sign_data1[5:7])
    sdata2, start2, end2 = sign_data2[0:3], int(sign_data2[3:5]), int(sign_data2[5:7])
    if start1 <= iDay <= end1:
      final_sign = comp_sign_dict[sdata1]
      print("The Astrological Sign is", final_sign)
    elif start2 <= iDay <= end2:
      final_sign = comp_sign_dict[sdata2]
      print("The Astrological Sign isdec", final_sign)
    else:
      print("Invalid Data")
#--------------------------------------------------------------  
else:
    print("Invalid Input Data - Invalid Month.")
print("Thank you for using this app.")
#**************************************************************