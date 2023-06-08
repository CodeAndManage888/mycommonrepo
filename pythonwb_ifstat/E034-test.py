#**************************************************************
# Date: 051123                                                *
# Title: Even or Odd                                          *
# Status: Testing (In Progress / Testing / Working)           *
# Write a program that reads an integer from the user. Then   * 
# your program should display a message indicating whether    * 
# the inter is even or odd.                                   *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
computed_value = 0
icheck = -1
iInteger, ciInteger = (0,0)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Integer input data only.")
#--------------------------------------------------------------    
iInteger = input("What number is in your mind (Integer Only)?==> ")
ciInteger = data_check(iInteger)
#--------------------------------------------------------------
if icheck == 0 and ciInteger != 0:
  computed_value = ciInteger % 2
  if computed_value == 1:
    print("Your number is an ODD number.")
  else:
    print("Your number is an EVEN number.")
  print("Thank you for using this app.")
else:
  print("Thank you for using this app.")
#**************************************************************