#**************************************************************
# Date: 050723 / 050823                                       *
# Title: Sum of the Digits in an Integer                      *
# Status: Testing (In Progress / Testing / Working)           *
# Develop a program that reads a four-digit integer from the  *
# user and displays the sum of the digits in the number. For  *
# example, if the user enters 3141 then your program should   *
# display 3+1+4+1=9.                                          *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
icheck = -1
tot_sum = 0
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=float(UserIn1)
    icheck = 0
    return UserIn1
  except:
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------    
while icheck == -1:
  print("Please provide a four-digit integer only.")
  i4Integer = input("What is the four-digit integer? ==> ")
  if len(i4Integer) == 4:
    i4Integer = data_check(i4Integer)
    if icheck == -1:
      break
    for i in range(len(i4Integer)):
      tot_sum = tot_sum + int(i4Integer[i])
    print(i4Integer[0],"+",i4Integer[1],"+",i4Integer[2],"+",i4Integer[3],"=",tot_sum)
  else:
    print("Please input four-digit integer only!")
    icheck = 0
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# Open Items:
#
# CHistory:
# C05072200
# - test possible ways to break down a string
# C05072230
# - added process for sorting numbers in a 3 digit integer
# C0508231900:
# - complete the initial draft of the exercise 31
# - updated status of the completed programs
