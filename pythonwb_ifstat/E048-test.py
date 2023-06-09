#**************************************************************
# Date: 053023   (Expected Solution with 35 Lines of Code)    *
# Title: Chinese Zodiac                                       *
# Status: Testing (In Progress / Testing / Working)           *
# The Chinese zodiac assigns animals to years in a 12 year    *
# cycle. One 12 year cycle is show in the table below. The    *
# pattern repeats from the, and with 2012 being another year  *
# of teh dragon, and 1999 being another year of the hare.     *
#                                                             *
# Year            Animal                                      *
# -----           ------------                                *
# 2000            Dragon                                      *
# 2001            Snake                                       *
# 2002            Horse                                       *
# 2003            Sheep                                       *
# 2004            Monkey                                      *
# 2005            Rooster                                     *
# 2006            Dog                                         *
# 2007            Pig                                         *
# 2008            Rat                                         *
# 2009            Ox                                          *
# 2010            Tiger                                       *
# 2011            Hare                                        *
#                                                             *
# Write a program that reads a year from the user and         *
# displays the animal associated with the year. Your program  *
# should work correctly for any year greater than or equal to *
# zero, not just the one listed in the table.                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
chi_sign_list = ["Dragon", "Snake", "Horse", "Sheep", "Monkey",
                 "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger",
                 "Hare"]
rev_chi_sign_list = []
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
iYearOnly = input("Enter the input year e.g. 1999: ")
if len(iYearOnly) <= 4:
  iCnvYear = data_check(iYearOnly)
  if (iCnvYear <= 2000) and (icheck == 0):
    pRemYrs = (2000 - iCnvYear) % 12
    rev_chi_sign_list = chi_sign_list[::-1]
    print("The Chinese Zodiac for the year", iYearOnly, "is", rev_chi_sign_list[pRemYrs - 1]+".")
  elif (iCnvYear > 2000) and (icheck == 0):
    pRemYrs = (iCnvYear - 2000) % 12
    print("The Chinese Zodiac for the year", iYearOnly, "is", chi_sign_list[pRemYrs]+".")
else:
  print("Invalid Input Data. Invalid Input Data Length.")
print("Thank you for using this app.")
#**************************************************************