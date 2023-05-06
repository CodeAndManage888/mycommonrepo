#**************************************************************
# Date: 050623                                                *
# Title: Units of Pressure                                    *
# Status: In Progress (In Progress / Testing / Working)       *
# In this exercise you will create a program that reads a     *
# pressure from the user in kilo-pascals. Once the pressure   *
# has been read your program should report the equivalent     *
# pressure in pounds per square inch, millimeters of mercury  *
# and atmospheres. Use your research skills to determine the  *
# conversion factors between these units:                     *
#    a.)  1 kPa = 0.1450377377 psi                            *
#    b.)  1 kPa = 7.50061683 mmHg                             *
#    c.)  1 kPa = 0.00986923267 atm                           *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
computed_value = 0
icheck = -1
iPressure, ciPressure = (0,0)
#--------------------------------------------------------------
def data_check(UserIn1,cUserIn1):
  global icheck
  try:
    cUserIn1=float(UserIn1)
    icheck = 0
    return UserIn1, cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
    icheck = 0
#--------------------------------------------------------------    
while icheck == -1:
  print("Please provide the pressure in kPa.")
  iPressure = input("What is the pressure in kPa? ==> ")
  iPressure, ciPressure = data_check(iPressure, ciPressure)
#--------------------------------------------------------------
comp_psi = 0.1450377377 * ciPressure
comp_mmhg = 7.50061683 * ciPressure
comp_atm = 0.00986923267 * ciPressure
#--------------------------------------------------------------
print("The pressure in pounds per square inch, millimeters " + 
      "of mercury and atmosphere are " + 
      str(format(comp_psi, '2f')) + " psi, " + 
      str(format(comp_mmhg, '2f')) + " mmHg, " + 
      " and " + str(format(comp_atm, '2f')) + " atm.")
print("Thank you for using this app.")
#**************************************************************
# Open Items:
# 1.) why does this syntax defaults the decimal point to 6 
#     places only?
# 2.) in VS Code the processing does not stop when non numeric
#     is used needs testing in replit.
# 
# CHistory:
# C0506231230:
# - initial draft for exercise 30.
# - cleans up the templates for the next exercises
