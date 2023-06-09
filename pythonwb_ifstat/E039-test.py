#**************************************************************
# Date: 052223   (Expected Solution with 30 Lines of Code)    *
# Title: Sound Levels                                         *
# Status: Testing (In Progress / Testing / Working)           *
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
pDiffDec = 0
pFinalPercent = 0
pFinalValue = " "
noise_dict = {
  130: "Jackhammer",
  106: "Gas Lawnmower",
   70: "Alarm Clock",
   40: "Quiet Room"
}
noise_list = [130, 106, 70, 40]
#--------------------------------------------------------------
def data_check(UserIn1, cUserIn1):
  global icheck
  try:
    cUserIn1=int(UserIn1)
    icheck = 0
    return UserIn1, cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
    return UserIn1, cUserIn1
#--------------------------------------------------------------    
iSoundLvl = input("What is the sound level in decibel? ==> ")
iSoundLvl, ciSoundLvl = data_check(iSoundLvl, ciSoundLvl)
if (ciSoundLvl in noise_list) and (icheck == 0):
  pFinalValue = noise_dict[ciSoundLvl]
  print("Sound level is equivalent to a " + pFinalValue + " noise level.")
else:
  if (130 > ciSoundLvl > 106) and (icheck == 0):
    print("Sound level is between Jackhammer and Gas Lawnmower noise." )
  if (106 > ciSoundLvl > 70) and (icheck == 0):
    print("Sound level is between Gas Lawnmower and Alarm Clock noise." )
  if (70 > ciSoundLvl > 40) and (icheck == 0):
    print("Sound level is between Alarm Clock and Quiet Room noise." )
if (ciSoundLvl > 130) and (icheck == 0):
  pDiffDec = ciSoundLvl - 130
  pFinalPercent = (pDiffDec / 130) * 100
  fv_Percent = format(round(pFinalPercent, 2), '0.2f')
  print("Sound level is %s percent louder than a Jackhammer." % fv_Percent)
if (ciSoundLvl < 40) and (icheck == 0):
  if ciSoundLvl != 0:
    pDiffDec = 40 - ciSoundLvl
    pFinalPercent = (pDiffDec / 40) * 100
    print("Sound level is %s percent quieter than a Quiet Room." % pFinalPercent)
  else:
    print("Invalid input data! Please use a non zero data.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************