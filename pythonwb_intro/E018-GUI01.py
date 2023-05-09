#**************************************************************
# Date: 080222                                                *
# Title: Volume of a Cylinder                                 *
# Status: Working (In Progress / Testing / Working)           *
# Programmer: BoredManager                                    *
# The volume of a cylinder can be computed by multiplying the *
# area of its circular base by its height. Write a program    *
# that reads the radius of the cylinder, along with its       *
# height, from the user and computes its volume. Display the  *
# result rounded to one decimal place.                        *
#                                                             *
# Computed Result Validated:                                  *
# https://www.google.com/                                     *
#**************************************************************

from tkinter import *
import math

def click():
    UsrInputRadius=inputentry1.get()
    UsrInputHeight=inputentry2.get()
    outputdata1.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(UsrInputRadius)
        cUserInput2 = float(UsrInputHeight)
        icheck = 0
        computed_data1 = (math.pi * (cUserInput1 ** 2)) * cUserInput2 
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
w.title("My Cylinder Volume App")
w.configure(background="Light Yellow")

#-------------------------------------------------------------
Label (w, text="User Input Radius(Unit):", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

Label (w, text="User Input Height(Unit):", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)
inputentry2 = Entry(w, width=10, bg="white")
inputentry2.grid(row=2, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="Volume of the Cylinder(Cubic Units):", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=16, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=16, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=16, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
