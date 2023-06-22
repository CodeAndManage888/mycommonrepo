#**************************************************************
# Date: 060923   (Expected Solution with 38 Lines of Code)    *
# Title: Wavelengths of Visible Light                         *
# Status: Testing (In Progress / Testing / Working)           *
# The wavelength of visible light ranges from 380 to 750      *
# nanometers (nm). While the spectrum is continuous, it is    *
# often divided into 6 colors as shown below:                 *
#                                                             *
# Color               Wavelength (nm)                         *
# ----------          ----------------------                  *
# Violet              380 to less than 450                    *
# Blue                450 to less than 495                    *
# Green               495 to less than 570                    *
# Yellow              570 to less than 590                    *
# Orange              590 to less than 620                    *
# Red                 620 to 750                              *
#                                                             *
# Write a program that reads a wavelength from the user and   *
# reports its color. Display an appropriate error message if  *
# the wavelength entered by the user is outside of the        *
# visible spectrum.                                           *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
iWaveLenValue, ciWaveLenValue = (" ", 0)
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
iWaveLenValue = input("Enter the Wavelength value(Numeric only): ")
ciWaveLenValue = data_check(iWaveLenValue)
if icheck == 0:
  if 280 <= ciWaveLenValue < 450:
    print("The Wavelength %snm is Color Violet." % ciWaveLenValue)
  elif 450 <= ciWaveLenValue < 495:
    print("The Wavelength %s nm is Color Blue." % ciWaveLenValue)
  elif 495 <= ciWaveLenValue < 570:
    print("The Wavelength %s nm is Color Green." % ciWaveLenValue)
  elif 570 <= ciWaveLenValue < 590:
    print("The Wavelength %s nm is Color Yellow." % ciWaveLenValue)
  elif 590 <= ciWaveLenValue < 620: 
    print("The Wavelength %s nm is Color Orange." % ciWaveLenValue)
  elif 620 <= ciWaveLenValue <= 750:
    print("The Wavelength %s nm is Color Red." % ciWaveLenValue)
  else:
    print("Invalid Data! Out of range data")
  print("Thank you for using this app.")
else:
  print("Thank you for using this app.")
#**************************************************************