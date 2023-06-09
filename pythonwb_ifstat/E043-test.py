#**************************************************************
# Date: 052623   (Expected Solution with 31 Lines of Code)    *
# Title: Faces on Money                                       *
# Status: Testing (In Progress / Testing / Working)           *
# It is common for images of a country's previous leaders, or *
# other individual of historical significance, to appear on   *
# its money. The individuals that appear on banknotes in the  *
# United states are listed in the table below.                *
#                                                             *
# Individual                    Amount                        *
# George Washington             $1                            *
# Thomas Jefferson              $2                            *
# Abraham Lincoln               $5                            *
# Alexander Hamilton            $10                           *
# Andrew Jackson                $20                           *
# Ulysses S. Grant              $50                           *
# Benjamin Franklin             $100                          *
#                                                             *
# Write a program that begins by reading the denomination of  *
# a banknote from the user. Then your program should display  *
# the name of the individual that appears on the banknote of  *
# the entered amount. An appropriate error message should be  *
# displayed if no such note exits.                            *
# While two dollar banknotes are rarely seen in circulation   *
# in the United States, they are legal tender that can be     *
# spent just like any other denomination. The United States   *
# has also issued banknotes in denominations of $500, $1000,  *
# $5000 and $10000 for public use. However, high denomination *
# banknotes have not been printed since 1945 and were         *
# officially discontinued in 1969. As a result, we will not   *
# consider them in this exercise.                             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
face_money_dict = { 
     1: "George Washington",
     2: "Thomas Jefferson",
     5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
   100: "Benjamin Franklin",
}
fin_data, iMoneyValue, ciMoneyValue = (" ", " ", 0)
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
iMoneyValue = input("Enter the denomination(Numeric only): ")
ciMoneyValue = data_check(iMoneyValue)
if icheck == 0:
  fin_data = face_money_dict.get(ciMoneyValue,"Not Found")
  if fin_data != "Not Found":
    print("The individual in the note is %s." % fin_data)
  else:
    print("Invalid data! No equivalent note found.")
  print("Thank you for using this app.")
else:
  print("Thank you for using this app.")
#**************************************************************