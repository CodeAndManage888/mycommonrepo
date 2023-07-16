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
def data_check(UserIn1, cUserIn1):
  try:
    cUserIn1=float(UserIn1)
    icheck = 0
    return UserIn1, cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
    icheck = 0
#--------------------------------------------------------------    
while icheck == -1:
  iDogAgeMYrs = input("What is the age of the dog in human years? ==> ")
  iDogAgeMYrs, ciDogAgeMYrs = data_check(iDogAgeMYrs, ciDogAgeMYrs)
  if ciDogAgeMYrs == 2:
    print("The total equivalent dog years is", TwoYearsOld)
  else:
    if ciDogAgeMYrs < 2:
      tot_years = (ciDogAgeMYrs / 2) * TwoYearsOld
      print("The total equivalent dog years is", tot_years)
    else:
      tot_years = (ciDogAgeMYrs - 2)*4 + TwoYearsOld
      print("The total equivalent dog years is", tot_years)
  icheck = 0
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************