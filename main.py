#**************************************************************
# Date: 060923   (Expected Solution with 31 Lines of Code)    *
# Title: Frequency to Name                                    *
# Status: Testing (In Progress / Testing / Working)           *
# Electromagnetic radiation can be classified into one of 7   *
# categories according to its frequency, as shown in the      *
# table below:                                                *
#                                                             *
# Name                  Frequency Range (Hz)                  *
# ---------------       --------------------------------      *
# Radio waves           Less than 3 x 10^9                    *
# Microwaves            3 x 10^9 to less than 3 x 10^12       *
# Infrared light        3 x 10^12 to less than 4.3 x 10^14    *
# Visible light         4.3 x 10^14 to less than 7.5 x 10^14  *
# Ultraviolet light     7.5 x 10^14 to less than 3 x 10^17    *
# X-rays                3 x 10^17 to less than 3 x 10^19      *
# Gamma rays            3 x 10^19 or more                     *
#                                                             *
# Write a program that reads the frequency of the radiation   *
# from the usr and displays the appropriate name.             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import math
#--------------------------------------------------------------
iFreqValue, ciFreqValue, fin_val_num = (" ", 0, 0)
icheck = -1
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=int(float(UserIn1))
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Integer input data only.")
    cUserIn1 = 0
    return cUserIn1
#--------------------------------------------------------------
iFreqValue = input("Enter the Frequency value in Hz(Numeric only): ")
ciFreqValue = data_check(iFreqValue)
fin_val_num = "{:.0e}".format(ciFreqValue)
if icheck == 0:
  if ciFreqValue < 3e9:
    print("The Frequency %s Hz is within the range of a Radio waves." % fin_val_num)
  elif 3e9 <= ciFreqValue < 3e12: #3 x 10^9 to less than 3 x 10^12
    print("The Frequency %s Hz is within the range of a Microwaves." % fin_val_num)
  elif 3e12 <= ciFreqValue < 4.3e14: #3 x 10^12 to less than 4.3 x 10^14
    print("The Frequency %s Hz is within the range of an Infrared light." % fin_val_num)
  elif 4.3e14 <= ciFreqValue < 7.5e14: #4.3 x 10^14 to less than 7.5 x 10^14
    print("The Frequency %s Hz is within the range of a Visible light." % fin_val_num)
  elif 7.5e14 <= ciFreqValue < 3e17: #7.5 x 10^14 to less than 3 x 10^17
    print("The Frequency %s Hz is within the range of an Ultraviolet light." % fin_val_num)
  elif 3e17 <= ciFreqValue <= 3e19: #3 x 10^17 to less than 3 x 10^19
    print("The Frequency %s Hz is within the range of an X-rays." % fin_val_num)
  elif 3e19 <= ciFreqValue: #3 x 10^19 or more
    print("The Frequency %s Hz is within the range of a Gamma rays." % fin_val_num)
  else:
    print("Invalid Data! Out of range data")
  print("Thank you for using this app.")
else:
  print("Thank you for using this app.")
#**************************************************************