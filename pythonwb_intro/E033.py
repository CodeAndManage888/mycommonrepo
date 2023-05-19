#**************************************************************
# Date: 050823 / 051023                                       *
# Title: Day Old Bread                                        *
# Status: Working (In Progress / Testing / Working)           *
# A bakery sells loaves of bread for $3.49 each. Day old      *
# bread is discounted by 60 percent. Write a program that     *
# begins by reading the number of loaves of day old bread     *
# being purchased from the user. Then your program should     *
# display the regular price for the bread, the discount       *
# because it is a day old, and the total price. All of the    *
# values should be displayed using two decimal places, and    *
# the decimal points in all of the numbers should be aligned  *
# when reasonable values are entered by the users.            *
# Computed Result Validated:                                  *
#**************************************************************
regPrice = 3.49
dayOldPrice = regPrice * .4
iNumBread, ciNumBread, UserIn1, cUserIn1 = (0, 0, 0, 0)
computed_value  = 0
icheck = -1
#--------------------------------------------------------------
def data_check(UserIn1, cUserIn1):
  global icheck
  try:
    cUserIn1=float(UserIn1)
    icheck = 0
    return UserIn1, cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
    icheck = 0
    return UserIn1, cUserIn1
#--------------------------------------------------------------    
while icheck == -1:
  iNumBread=input("Please enter the number of bread: ")
  iNumBread, ciNumBread = data_check(iNumBread, ciNumBread)
#--------------------------------------------------------------
  if icheck == 0 and ciNumBread != 0:
    computed_value = dayOldPrice * ciNumBread
    fv_regPrice = str(format(round(regPrice, 2), '0.2f'))
    fv_dayOldPrice = str(format(round(dayOldPrice, 2), '0.2f'))
    final_value = str(format(round(computed_value, 2), '0.2f'))
    print("Your computed prices are the following: ")
    print("Regular price for bread is " + fv_regPrice)
    print("Discounted price for a day old bread is " + fv_dayOldPrice)
    print("Total price for " + iNumBread + " bread(s) is " + final_value)
    print("<--------------------------------------------------->")
    print("Your computed prices are the following: ")   
    print(fv_regPrice.rjust(6, " "))
    print(fv_dayOldPrice.rjust(6, " "))
    print(final_value.rjust(6, " "))
    print("Thank you for using this app!")
  else:
    print("Thank you for using this app!")
    break
#**************************************************************
# Open Items:
#
# CHistory:
# C0508231900:
# - initial draft for exercise 33
# C0508231700:
# - need to move all intro code to another 
# folder 
# C0509232230:
# - started coding exercise 33.
# C0510232130:
# - completed the draft of exercise 33.
# C0519230800:
# - updated the code to fix the issue if the input is string
# - fully tested code for exercise 33
# - updated bash script input data and permission for the bash script