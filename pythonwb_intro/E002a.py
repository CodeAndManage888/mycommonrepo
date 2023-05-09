#**************************************************************
# 020222                                                      *
# Title: Hello with Date & Time                               *
# Status: Not Working                                         *
# This program will accept the name ahd reponse "Hello" to    *
# the user. It will show the current date and time at the     *
# start and in the date in the response.                      *
#                                                             *
#                                            - BoredManager   *
#**************************************************************
import datetime
now = datetime.datetime.now()
print(" ")
print("|----------------------------------------------------|")
print(" Current date and time : ")
print(now.strftime(" %Y-%m-%d %H:%M:%S"))
#sys_date = (now.strftime(" Feb %d %Y")
user_input = input(" What is your name?: ")
print(" Hello "+user_input+","" Have a good day.")
print("|----------------------------------------------------|")
print(" ")
#**************************************************************
# What have i learned from this challenge?                    *
#                                                             *
#**************************************************************
