#**************************************************************
# Date: 060923   (Expected Solution with 38 Lines of Code)    *
# Title: Wavelengths of Visible Light                         *
# Status: In Progress (In Progress / Testing / Working)       *
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
#--------------------------------------------------------------
#--------------------------------------------------------------
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