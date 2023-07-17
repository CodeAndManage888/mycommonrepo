#**************************************************************
# Date: 051123                                                *
# Title: Dog Years                                            *
# Status: Working (In Progress / Testing / Working)           *
# It is commonly said that one human year is equivalent to 7  * 
# dog years. However this simple conversion fails to          *
# recognize that dogs reach adulthood in approximately two    * 
# years. As a result, some people believe that it is better   *
# to count each of the first two human years as 10.5 dog      * 
# years, and then count each additional human year as 4 dog   * 
# years.                                                      *
# Write a program that implements the conversion from human   *
# years to dog years described in the previous paragraph.     *
# ensure that your program works correctly for conversions of *
# less than two human years and for conversions of two or     *
# more human years. Your program should display an            *
# appropriate error message if the user enters a negative     *
# number.                                                     *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
tot_years, ciDogAgeMYrs = (0, 0)
TwoYearsOld = 10.5
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=float(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
    icheck = -1
#--------------------------------------------------------------  
iDogAgeMYrs = input("What is the age of the dog in human years? ==> ")
ciDogAgeMYrs = data_check(iDogAgeMYrs)
if icheck == 0:
  if ciDogAgeMYrs < 0:
    print("Please enter positive number only!")
  elif ciDogAgeMYrs == 2:
    print("The total equivalent dog years is 21.0.")
  elif ciDogAgeMYrs < 2:
    tot_years = TwoYearsOld * ciDogAgeMYrs
    print("The total equivalent dog years is %s." % tot_years)
  else:
    tot_years = ((ciDogAgeMYrs - 2) * 4) + 21
    print("The total equivalent dog years is %s." % tot_years)
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# C0717231800 - Addressed issue 81 & 82