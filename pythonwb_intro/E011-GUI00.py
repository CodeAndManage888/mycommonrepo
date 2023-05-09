#**************************************************************
# Date: 072022                                                *
# Title: Fuel Efficiency                                      *
# Programmer: BoredManager                                    *
# In the United States, fuel efficiency for vehicles is nor-  *
# mally is expressed in miles-per-gallon (MPG). In Canada,    *
# fuel efficiency is normally expressed in liters-per-hundred *
# kilometers (L/100km). Use your research skills to determine *
# how to convert from MPG to L/100km. Then create a program   *
# that reads a value from the user in American units and dis- *
# plays the equivalent fuel efficiency in Canadian units.     *
#**************************************************************
import math
from matplotlib.pyplot import title
import pyautogui
computed_value = 0
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    UserInput = pyautogui.prompt(text='Please Enter US Fuel Efficiency Data (MPG)', title='Fuel Efficiency')
    try:
        cUserInput = int(UserInput)
        icheck = 0
    except:
        pyautogui.alert(text="Please Enter A Number Only Value.", title='Error Message')
#--------------------------------------------------------------
computed_value = 235.215 / cUserInput
pyautogui.alert(text=computed_value, title='Liters per 100 Kilometers')
pyautogui.alert(text='Thank you for using the program!' , title='User Message')

#**************************************************************
# Lessons Learned:
# - I still can't combine 2 message sources when displaying it 
#   via a dialoge box using pyautogui Python package (R1)
# - It would be good to also explore using other package for 
#   alternative GUI option e.g. TKinter, PyQt etc.
# - Simplify the application but just using one window. (R2)
