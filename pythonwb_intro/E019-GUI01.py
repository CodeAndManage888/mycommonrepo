#**************************************************************
# Date: 101322                                                *
# Title: Free Fall                                            *
# Status: Working (In Progress / Testing / Working)           *
# Programmer: BoredManager                                    *
# Create a program that determines how quickly an object is   *
# traveling when it hits the ground. The user will enter the  *
# height from which the object is dropped in meters (m).      *
# Because the object is dropped its initial speed is 0 m/s.   *
# Assume that the acceleration due to gravity is 9.8 m/s^2.   *
# You can use the formula vf = (vi^2 + 2ad)^1/2 to compute    *
# the final speed, vf , when the initial speed, vi ,          *
# acceleration, a, and distance, d, are known.                *
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

w = Tk()
w.title("My Free Fall App")
w.configure(background="Light Yellow")

#-------------------------------------------------------------
Label (w, text="Drop Height(meters):", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

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
#       speaking the formula is correct.
