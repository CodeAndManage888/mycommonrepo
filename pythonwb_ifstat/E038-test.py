#**************************************************************
# Date: 052123  (Expected Solution with 18 Lines of Code)     *
# Title: Month Name to Number of Days                         *
# Status: Testing (In Progress / Testing / Working)           *
# The length of a month varies from 28 to 31 days. In this    *
# exercise you will create a program that reads the name of a *
# month from the user as a string. Then your program should   *
# display the number of days in that month. Display "28 or 29 *
# days" for February so that leap years are addressed.        *
#                                                             *
# Coder Additional Features:                                  *
# The code can recognize 5 month name variations which are    *
# following:                                                  *
# a.) Full with capital letter e.g. January                   *
# b.) Full with small letter e.g. january                     *
# c.) 3 byte shortened with capital letter e.g. Jan           *
# d.) 3 byte shortened with small letter e.g. jan             *
# e.) All 4 variations but all caps e.g. JAN or JANUARY       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
data_side_dict = { 
   "Jan": "31",
   "Feb": "28 or 29",
   "Mar": "31",
   "Apr": "30",
   "May": "31",
   "Jun": "30",
   "Jul": "31",
   "Aug": "31",
   "Sep": "30",
   "Oct": "31",
   "Nov": "30",
   "Dec": "31"
}
MonList = ["January", "Jan", "january", "jan", "JANUARY", 
           "February", "Feb", "february", "feb", "FEBRUARY", 
           "March", "Mar", "march", "mar", "MARCH", "April", 
           "Apr", "april", "apr", "APRIL", "May", "may", "MAY", 
           "June", "Jun", "june", "jun", "JUNE", "July", "Jul", 
           "july", "jul", "JULY", "August", "Aug", "august", 
           "aug", "AUGUST", "September", "Sep", "september", 
           "sep", "SEPTEMBER", "October", "Oct", "october", 
           "oct", "OCTOBER", "November", "Nov", "november", 
           "nov", "NOVEMBER", "December", "Dec", "december", 
           "dec", "DECEMBER"]
iMonNameOnly = " "
p2nd3rdLtr = " "
pFirstLtr = " "
pKeyString = " "
fin_data = " "
icheck = -1
#--------------------------------------------------------------    
iMonNameOnly = input("Enter the name of the month: ")
if iMonNameOnly in MonList:
  pFirstLtr = iMonNameOnly[0].capitalize()
  p2nd3rdLtr = iMonNameOnly[1:3].lower()
  pKeyString = pFirstLtr + p2nd3rdLtr
  fin_data = data_side_dict[pKeyString]
  print("The input month have " + fin_data + " days.")
  print("Thank you for using this app.")
else:
  print("Invalid input data! Not a valid month name.")
  print("Thank you for using this app.")
#**************************************************************