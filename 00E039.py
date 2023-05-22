#**************************************************************
# Date: 052223   (Expected Solution with 30 Lines of Code)    *
# Title: Sound Levels                                         *
# Status: In Progress (In Progress / Testing / Working)       *
# The following table lists the sound level in decibels for   *
# several common noises.                                      *
#                                                             *
# Noise                Decibel Level (dB)                     *
# Jackhammer           130                                    *
# Gas lawnmower        106                                    *
# Alarm clock          70                                     *
# Quiet room           40                                     *
#                                                             *
# Write a program that reads a sound level in decibel from    *
# the user. If the user enters a decibel level that matches   *
# one of the noises in the table then your program should     *
# display a message containing only that noise. If the user   *
# enters a number of decibels between the noises listed then  *
# your program should display a message indicating which      *
# noises the level in between. Ensure that your program also  *
# generates reasonable output for a value smaller than the    *
# quietest noise in the table, and for a value larger than    *
# the loudest noise in the table.                             *
#                                                             *
# Coder Additional Features:                                  *
# Added the following on top of the initial requirements      *
# a.) The message for the input that is beyond the quietest   *
# and loudest noise will be in percentage format.             *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
iSoundLvl = " "
ciSoundLvl = 0
pDiffDec = 
pFinalPercent = 0
pFinalValue = " "
noise_dict = {
  130: "Jackhammer",
  106: "Gas lawnmower",
   70: "Alarm clock",
   40: "Quiet room"
}
noise_list = [130, 106, 70, 40]
#--------------------------------------------------------------
def data_check(UserIn1, cUserIn1):
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return UserIn1, cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------    
iSoundLvl = input("What is the sound level in decibel? ==> ")
iSoundLvl, ciSoundLvl = data_check(iSoundLvl, ciSoundLvl)
if ciSoundLvl in noise_list:
  pFinalValue = noise_dict[ciSoundLvl]
  print("Sound level is equivalent to a " + pFinalValue + " noise level.")
  print("Thank you for using this app.")
else:
  if (130 > ciSoundLvl > 106):
    print("Sound level is between Jackhammer and Gas Lawnmower noise." )
  if (106 > ciSoundLvl > 70):
    print("Sound level is between Gas Lawnmower and Alarm Clock noise." )
  if (70 > ciSoundLvl > 40):
    print("Sound level is between Alarm Clock and Quiet Room noise." )
  if ciSoundLvl > 130:
    pDiffDec = ciSoundLvl - 130
    pFinalPercent = pDiffDec%130



if ciDogAgeMYrs == 2:
  print("The total equivalent dog years is", TwoYearsOld)
else:
  if ciDogAgeMYrs < 2:
    tot_years = (ciDogAgeMYrs / 2) * TwoYearsOld
    print("The total equivalent dog years is ", tot_years)
  else:
    tot_years = (ciDogAgeMYrs - 2)*4 + TwoYearsOld
    print("The total equivalent dog years is ", tot_years)
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# Open Items:
#
# CHistory:
# C0522230900
# - started the draft of the code for exercise 39
# C0522232300
# - continue coding for exercise 39