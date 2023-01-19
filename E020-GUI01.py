#**************************************************************
# Date: 101922                                                *
# Title: Ideal Gas Law                                        *
# Status: Working (In Progress / Testing / Working)           *
# Programmer: BoredManager                                    *
# The ideal gas law is a mathematical approximation of the    *
# behavior of gasses as pressure, volume and temperature      *
# change. It is usually stated as:                            *
#                        PV = nRT                             *
# where P is the pressure in Pascals, V is the volume in      * 
# liters, n is the amount of substance in moles, R is the     * 
# ideal gas constant, equal to 8.314 J / mol K , and T is the *
# temperature in degrees Kelvin.                              *
# Write a program that computes the amount of gas in moles    * 
# when the user supplies the pressure, volume and temperature.*
# Test your program by determining the number of moles of gas *
# in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas*
# at a pressure of 20,000,000 Pascals (approx 3,000 PSI). Room*
# temperature is approximately 20 degrees Celsius or 68       *
# degrees Fahrenheit.                                         *
# Hint: A temperature is converted from Celsius to Kelvin by  *
# adding 273.15 to it. To convert a temperature from          * 
# Fahrenheit to Kelvin, deduct 32 from it, multiply it by 59  *
# and then add 273.15 to it.                                  *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
from tkinter import *
import math

def click():
    fInitialVelocity = 0
    fAcceleration = 9.8
    UsrInputHeight=inputentry1.get()
    outputdata1.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(UsrInputHeight)
        icheck = 0
        computed_data1 = math.sqrt(fInitialVelocity**2 + (2*fAcceleration*cUserInput1))
#       computed_data1 = (fInitialVelocity**2 + (2*fAcceleration*cUserInput1)**(1/2)
    except:
        computed_data1 ='Input Error'

    outputdata1.insert(END,computed_data1)
    
def close_app():
    w.destroy()
    exit()

def retain_app():
    outputdata1.delete(0.0, END)
    inputentry1.delete(0, END)
    inputentry2.delete(0, END)

w = Tk()
w.title("My Ideal Gas Law App")
w.configure(background="Light Yellow")

#-------------------------------------------------------------
Label (w, text="Pressure(Pascals):", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

Label (w, text="Volume(Liters):", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)
inputentry2 = Entry(w, width=10, bg="white")
inputentry2.grid(row=2, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="Final Velocity(m/s^2):", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=16, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=16, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=16, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
# - The following are the open questions regarding the GUI
#   window:
#   a.) How do you get the square root without using math function?
#       The commented line is causing an issue when mathematically
#       speaking the formula should be correct.
