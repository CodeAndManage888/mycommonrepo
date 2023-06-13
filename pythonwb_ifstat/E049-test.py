#**************************************************************
# Date: 053023   (Expected Solution with 30 Lines of Code)    *
# Title: Richter Scale                                        *
# Status: Testing (In Progress / Testing / Working)           *
# The following table contains earthquake magnitude ranges on *
# the Richter scale and their descriptors:                    *
#                                                             *
# Magnitude                Descriptor                         *
# -----------------        ----------------                   *
# Less than 2.0            Micro                              *
# 2.0 to less than 3.0     Very minor                         *
# 3.0 to less than 4.0     Minor                              *
# 4.0 to less than 5.0     Light                              *
# 5.0 to less than 6.0     Moderate                           *
# 6.0 to less than 7.0     Strong                             *
# 7.0 to less than 8.0     Major                              *
# 8.0 to less than 10      Great                              *
# 10.0 or more             Meteoric                           *
#                                                             *
# Write a program that reads a magnitude from the user and    *
# displays the appropriate description as part of a           *
# meaningful message. For example, if the user enters 5.5     *
# then your program should indicate that a magnitude 5.5      *
# earthquake is considered to be a moderate earthquake.       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
iMagValue, ciMagValue = (" ", 0)
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
iMagValue = input("Enter the earthquake magnitude(Numeric only): ")
ciMagValue = data_check(iMagValue)
if icheck == 0:
  if 0 < ciMagValue < 2.0:
    print("The value %s in the Richter Scale is Micro" % ciMagValue)
  elif 2.0 <= ciMagValue < 3.0:
    print("The value %s in the Richter Scale is Very Minor" % ciMagValue)
  elif 3.0 <= ciMagValue < 4.0:
    print("The value %s in the Richter Scale is Minor" % ciMagValue)
  elif 4.0 <= ciMagValue < 5.0:
    print("The value %s in the Richter Scale is Light" % ciMagValue)
  elif 5.0 <= ciMagValue < 6.0: 
    print("The value %s in the Richter Scale is Moderate" % ciMagValue)
  elif 6.0 <= ciMagValue < 7.0:
    print("The value %s in the Richter Scale is Strong" % ciMagValue)
  elif 7.0 <= ciMagValue < 8.0:
    print("The value %s in the Richter Scale is Major" % ciMagValue)
  elif 8.0 <= ciMagValue < 10.0:
    print("The value %s in the Richter Scale is Great" % ciMagValue)
  elif ciMagValue >= 10.0:
    print("The value %s in the Richter Scale is Meteoric" % ciMagValue)
  else:
    print("Invalid Data! Out of range data")
  print("Thank you for using this app.")
else:
  print("Thank you for using this app.")
#**************************************************************