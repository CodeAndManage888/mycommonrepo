#**************************************************************
# Date: 040321                                                *
# Title: Arithmetic                                           *
# Programmer: BoredManager                                    *
# Create a program that reads two integers, a and b, from the *
# user. Your program should compute and display:              *
# - The sum of a and b                                        *
# - The difference when b is subtracted from a                *
# - The product of a and b                                    *
# - The quotient when a is divided by b                       *
# - The remainder when a is divided by b                      *
# - The result of log10 a                                     *
# - The result of a exp b                                     *
#**************************************************************
import math
computed_value = 0
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    iUser_Number1 = input("Please enter the first number ==> ")
    try:
        ciUser_Number1 = int(iUser_Number1)
        icheck = 0
    except:
        print("Please enter a number only value.")
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    iUser_Number2 = input("Please enter the second number ==> ")
    try:
        ciUser_Number2 = int(iUser_Number2)
        icheck = 0
    except:
        print("Please enter a number only value.")
#--------------------------------------------------------------
computed_value = ciUser_Number1 + ciUser_Number2
print ("The sum of %.f and %.f is %.f." % (ciUser_Number1, ciUser_Number2, computed_value))
computed_value = ciUser_Number1 - ciUser_Number2
print ("The difference of %.f and %.f is %.f." % (ciUser_Number1, ciUser_Number2, computed_value))
computed_value = ciUser_Number1 * ciUser_Number2
print ("The product of %.f and %.f is %.f." % (ciUser_Number1, ciUser_Number2, computed_value))
computed_value = ciUser_Number1 / ciUser_Number2
print ("The quotient of %.f and %.f is %.f." % (ciUser_Number1, ciUser_Number2, computed_value))
computed_value = ciUser_Number1 % ciUser_Number2
print ("The remainder of %.f and %.f is %.f." % (ciUser_Number1, ciUser_Number2, computed_value))
computed_value = math.log10(ciUser_Number1)
print ("The result of log10(%.f) is %.f." % (ciUser_Number1, computed_value))
computed_value = ciUser_Number1 ** ciUser_Number2
print ("The result of %.f exp %.f is %.f." % (ciUser_Number1, ciUser_Number1, computed_value))
#--------------------------------------------------------------
print("Thank you for using this app.")

#**************************************************************
# Lessons Learned:
# - 
