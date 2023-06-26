#**************************************************************
# Date: 061423   (Expected Solution with 22 Lines of Code)    *
# Title: Is it a Leap Year                                    *
# Status: Testing (In Progress / Testing / Working)           *
# Most years have 365 days. However, the time required for    *
# the Earth to orbit the Sun is actually slightly more than   *
# that. As a result, an extra day, February 29, is included   *
# in some years to correct for this difference. Such years    *
# are referred to as leap years. The rules for determiniing   *
# whether or not a year is a leap year follow:                *
#                                                             *
# a.) Any year that is divisible by 400 is a leap year.       *
# b.) Of the remaining years, any year that is divisible by   *
#     100 is not a leap year.                                 *
# c.) Of the remaining years, any year that is divisible by 4 *
#     is a leap year.                                         *
# d.) All other year are not leap years.                      *
#                                                             *
# Write a program that reads a year from the user and         *
# displays a message indicating whether or not it is a leap   *
# year.                                                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
iYearOnly, iCnvYear, pRemYrs1, pRemYrs2, pRemYrs3 = (" ", 0, 0, 0, 0)
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
  if icheck == 0:
    pRemYrs1 = iCnvYear % 400
    if pRemYrs1 != 0:
      pRemYrs2 = pRemYrs1 % 100
      if pRemYrs2 != 0:
        pRemYrs3 = pRemYrs2 % 4
        if pRemYrs3 != 0:
          print("The %s year is not a leap year." % iYearOnly)
        else:
          print("The %s year is a leap year." % iYearOnly)
      else:
        print("The %s year is a leap year." % iYearOnly)
    else:
      print("The %s year is a leap year." % iYearOnly)
else:
  print("Invalid Input Data. Invalid Input Data Length.")
print("Thank you for using this app.")
#**************************************************************