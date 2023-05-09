#**************************************************************
# Date: 072122                                                *
# Title: Distance Between Two Points on Earth                 *
# Programmer: BoredManager                                    *
# The surface of the Earth is curved, and the distance bet-   *
# ween degrees of longitudevaries with latitude. As a result, *
# finding the distance between two points on the surface of   *
# the Earth is more complicated than simply using the         * 
# Pythagorean theorem.                                        *
#                                                             *
# Let (t1, g1) and (t2, g2) be the latitude and longitude of  *
# two points on the Earth’s surface. The distance between     * 
# these points, following the surface of the Earth, in kilo-  *
# meters is:                                                  *
#                                                             *
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) x   × 
# cos(t2) × cos(g1 − g2))                                     * 
#                                                             * 
# The value 6371.01 in the previous equation wasn’t selected  *
# at random. It is the average radius of the Earth in kilo-   *
# meters.                                                     * 
#                                                             * 
# Create a program that allows the user to enter the latitude * 
# and longitude of two points on the Earth in degrees. Your   * 
# program should display the distance between the points,     *
# following the surface of the earth, in kilometers.          *
#**************************************************************
import math 
from cmath import acos, sin, cos
from matplotlib.pyplot import title
import pyautogui
computed_value = 0
m1out = 0
m2out = 0
m3out = 0
m4out = 0
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    LatUserInput1 = pyautogui.prompt(text='Latitude Data (Degree) of Point 1', title='Latitude Input')
    try:
        cLatUserInput1 = float(LatUserInput1)
        icheck = 0
    except:
        pyautogui.alert(text="Please Enter A Number Only Value.", title='Error Message')
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    LongUserInput1 = pyautogui.prompt(text='Longitude Data (Degree) of Point 1', title='Longitude Input')
    try:
        cLongUserInput1 = float(LongUserInput1)
        icheck = 0
    except:
        pyautogui.alert(text="Please Enter A Number Only Value.", title='Error Message')
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    LatUserInput2 = pyautogui.prompt(text='Latitude Data (Degree) of Point 2', title='Latitude Input')
    try:
        cLatUserInput2 = float(LatUserInput2)
        icheck = 0
    except:
        pyautogui.alert(text="Please Enter A Number Only Value.", title='Error Message')
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    LongUserInput2 = pyautogui.prompt(text='Longitude Data (Degree) of Point 2', title='Longitude Input')
    try:
        cLongUserInput2 = float(LongUserInput2)
        icheck = 0
    except:
        pyautogui.alert(text="Please Enter A Number Only Value.", title='Error Message')
#--------------------------------------------------------------
#computed_value = 6371.01 * acos(sin(cLatUserInput1) * sin(cLatUserInput2) + \
#                                cos(cLatUserInput1) * cos(cLatUserInput2) * \
#                                cos(cLongUserInput1 - cLongUserInput2))

m1out = sin(cLatUserInput1) * sin(cLatUserInput2) 
m2out = cos(cLatUserInput1) * cos(cLatUserInput2)
m3out = cos(cLongUserInput1 - cLongUserInput2)
m4out = acos(m1out + m2out * m3out)
computed_value = 6371.01 * m4out
pyautogui.alert(text=computed_value, title='Distance in Kilometers')
pyautogui.alert(text='Thank you for using the program!' , title='User Message')

#**************************************************************
# Lessons Learned:
# - As of 072122 1900, output is not the same as the result in
#   the following sites: 
#   a.) https://www.omnicalculator.com/other/latitude-longitude-distance
#   b.) https://www.nhc.noaa.gov/gccalc.shtml
#   c.) https://www.meridianoutpost.com/resources/etools/calculators/calculator-latitude-longitude-distance.php?
# - Test date used are the following:
#   a.) 50.5025 / 50.5025
#   b.) 25.5025 / 25.5025
# - How to use packages when to use import , from etc? (R1)
# - Does python follow the MDAS rule? (R2)
# - Still using pyautogui instead of other GUI pacakge. I still 
#   need to research documentation for PyQt or Tkinter
# - 072122 1100: The program can accept inputs with decimal point
#   but still able to validate if the input is numeric. The output
#   however is still showing parenthesis and the letter j.
