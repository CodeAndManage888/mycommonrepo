#**************************************************************
# Date: 01312023                                                       *
# Title:                                                      *
# Status: In Progress (In Progress / Testing / Working)       *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
import math

computed_value = 0
icheck = -1
while icheck == -1:
  iLength = input("What is the length of the sides? ==> ")
  iSides = input("How many sides does the polygon have? ==> ")
  try:
    ciLength = float(iLength)
    ciSides = float(iSides)
    icheck = 0
  except:
    print("Please input number data only.")
#--------------------------------------------------------------
computed_value = (ciSides * ciLength**2) / (4 * math.tan(math.pi/ciSides))
fcomputed_value = format(computed_value, '2f')
final_value = str(fcomputed_value)
#--------------------------------------------------------------
print("The area of the polygon is", final_value, "sq. units.")
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
# 1.) Will this have the same result if used to compute the 
#     area of the triangle?
