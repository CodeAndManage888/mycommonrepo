#**************************************************************
# Date: 052523   (Expected Solution with 40 Lines of Code)    *
# Title: Frequency to Note                                    *
# Status: Testing (In Progress / Testing / Working)           *
# In the previous question you converted from note name to    *
# frequency. In this question you will write a program that   *
# reverses that process. Begin by reading a frequency from    *
# the user. If the frequency is within one Hertz of a value   *
# listed in the table in the previous question then report    *
# the name of the note. Otherwise report that the frequency   *
# does not correspond to a known note. In this exercise you   *
# only need to consider the notes listed in the table. There  *
# is no need to consider notes from other octaves.            *

# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
iFreqValues, ciFreqValues = (" ", 0)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1=float(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Integer input data only.")
    print("Thank you for using this app.")
    cUserIn1 = 0
    return cUserIn1
#--------------------------------------------------------------
iFreqValues = input("Please input the frequency to know the note name?==> ")
ciFreqValues = data_check(iFreqValues)
if icheck == 0:
  if (260.63 <= ciFreqValues <= 262.63):
    print("The input frequency of %s Hz is a C4 note." % ciFreqValues)
  else:
    if (292.66 <= ciFreqValues <= 294.66):
      print("The input frequency of %s Hz is a D4 note." % ciFreqValues)
    else:
      if (328.63 <= ciFreqValues <= 330.63):
        print("The input frequency of %s Hz is a E4 note." % ciFreqValues)
      else:
        if (348.23 <= ciFreqValues <= 349.23):
          print("The input frequency of %s Hz is a F4 note." % ciFreqValues)
        else:
          if (391.00 <= ciFreqValues <= 393.00):
            print("The input frequency of %s Hz is a G4 note." % ciFreqValues)
          else:
            if (439.00 <= ciFreqValues <= 441.00):
              print("The input frequency of %s Hz is a A4 note." % ciFreqValues)
            else:
              if (492.88 <= ciFreqValues <= 494.88):
                print("The input frequency of %s Hz is a B4 note." % ciFreqValues)
              else:
                print("The input frequency does not correspond to any known note.")
  print("Thank you for using this app.")
#**************************************************************
# Open Items:
#
# CHistory:
# C0525231200
# - complete the code and ready for testing