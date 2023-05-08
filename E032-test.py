#**************************************************************
# Date: 050823                                                *
# Title: Sort 3 Integers                                      *
# Status: Testing (In Progress / Testing / Working)           *
# Create a program that read three integers from the user and *
# displays them in sorted order (from smallest to largest).   *
# Use the min and max functions to find the smalles and       *
# largest values. The middle value can be found by computing  *
# the sum of all three values, and then subtracting the       *
# minimum value and the miximum value.                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
tot_sum = 0
num_list = []
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
  print("Please provide a three-digit integer only.")
  i3Integer = input("What is the three-digit integer? ==> ")
  if len(i3Integer) == 3:
    i3Integer = data_check(i3Integer)
    if icheck == -1:
      break
    for i in range(len(i3Integer)):
      tot_sum = tot_sum + int(i3Integer[i])
    for char in i3Integer:
      num_list.append(char)
    min_value = min(num_list)
    max_value = max(num_list)
    mid_value = str(tot_sum - (int(min_value) + int(max_value)))
    print("The sorted value of " + i3Integer + " is " + min_value + 
          mid_value + max_value + " .")
  else:
    print("Please input three-digit integer only!")
    icheck = 0
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# Open Items:
#
# CHistory:
# C0508231900:
# - complete the initial draft of the exercise 32
# - updated status of the completed programs