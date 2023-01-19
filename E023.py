#**************************************************************
# Date: 011823                                                *
# Title: Area of a Regular Polygon                            *
# Status: In Progress (In Progress / Testing / Working)       *
# Programmer: BoredManager                                    *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
computed_value = 0
icheck = -1
while icheck == -1:
    iWidth = input("What is the width of the room in meter/s? ==> ")
    iLength = input("What is the length of the room in meter/s? ==> ")
    try:
        ciWidth = float(iWidth)
        ciLength = float(iLength)
        icheck = 0
    except:
        print("Please input number data only.")
#--------------------------------------------------------------
computed_value = ciWidth * ciLength
fcomputed_value = format(computed_value,'2f')
final_value = str(fcomputed_value)
#--------------------------------------------------------------
print("The room area is",final_value,"sq. meter.")
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
#
