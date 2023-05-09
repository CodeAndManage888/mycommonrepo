#**************************************************************
# Date: 040121                                                *
# Room Area                                                   *
# Programmer: BoredManager                                    *
# Write a program that asks the user to enter the width and   * 
# length of a room. Once the values have been read, your      *
# program should compute and display the area of the room.    *
# The length and the width will be entered as floating point  *
# numbers. Include units in your prompt and output message;   *
# either feet or meters, depending on which unit you are more *
# comfortable working with the user.                          *
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
# what have I learned from this challenge?                    
# - when getting data from a user input its format is "str"
#   i have to figure out how to change the data format the
#   moment it was received (A1).
# 091821
# - I'm not sure if this is possible, from what i found out the 
#   input function will always convert any data to "str" format.
#
# - the 1st version of the code is assuming that the user will
#   only input number with decimal point. added a validation
#   codes to prevent user from entering non numeric data. 
# - the program can accept interger however in processing big
#   number instead of displaying the entire string of numbers
#   it is using and exponential equivalent. how do you convert
#   it to a whole string instead? (A2).
# 091821
# - Using the format function can eliminate the automatic 
#   exponential convertion of the computed value. I still need 
#   to understand how to use the options to use the exact format 
#   needed (A2a)