#**************************************************************
# Date: 040121                                                *
# Field Area                                                  *
# Programmer: BoredManager                                    *
# Create a program that reads the length and width of a       *
# farmer’s field from the user in feet. Display the area of   *
# the field in acres.                                         *
# Hint:There are 43,560 square feet in an acre.               *  
#**************************************************************
computed_value = 0
icheck = -1
while icheck == -1:
    iWidth = input("What is the width of the field in feet? ==> ")
    iLength = input("What is the length of the field in feet? ==> ")
    try:
        ciWidth = float(iWidth)
        ciLength = float(iLength)
        icheck = 0
    except:
        print("Please input number data only.")
#--------------------------------------------------------------
one_acre = 43560
computed_value = (ciWidth * ciLength) / one_acre
computed_value = round(computed_value,6)
final_value = str(computed_value)
#--------------------------------------------------------------
print("The field area is "+final_value+" acre/s.")
print("Thank you for using this app.")
#**************************************************************
# what have I learned from this challenge?                    
# - the python is displaying up to 9 decimal places. Is that
#   the limit before using exponential form? (A1)
# - the program is a copy of the previous exercise except the
#   the addition of the conversion from sq. feet to acre.
# - still need to brush up with the use of different operation 
#   and its effect in different scenarios. (A2)
# - will it change to exponential form if the 4th decimal place
#   is zero? (A3)
# - [040221] added a process of rounding the number to 6 decimal
#   places. however it does not prevent it from formating it to 
#   exponential form if the decimal value is too small. can this
#   be prevented? (A4)