#**************************************************************
# Date: 020323                                                *
# Title: Current Time                                         *
# Status: Working     (In Progress / Testing / Working)       *
# Python includes library of functions for working with time, *
# including a function called asctime in the time module. It  *
# reads the current time from the computer's internal clock   *
# returns it in a human-readable format. Write a program that *
# displays the current time and date Your program will not    *
# require any input from the user                             *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
import time
#--------------------------------------------------------------
current_time = time.localtime()
print("Not formatted date and time data ", time.localtime())
print("<=====================================================>")
#--------------------------------------------------------------
print("The current date and time is ", time.asctime(current_time))
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************
# Lessons Learned:
# 1.) What other function does time module have?
