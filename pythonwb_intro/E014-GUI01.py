#**************************************************************
# Date: 073122                                                *
# Title: Height Units                                         *
# Programmer: BoredManager                                    *
# Many people think about their height in feet and inches,    *
# even in some countries that primarily use the metric system.*
# Write a program that reads a number of feet from the user,  *
# followed by a number of inches. Once these values are read, *
# your program should compute and display the equivalent      *
# number of centimeters.                                      *
#                                                             *
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.  *
#**************************************************************

from tkinter import *

def click():
    HinFeet=inputentry1.get()
    HinInches=inputentry2.get()
    outputdata1.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(HinFeet)
        cUserInput2 = float(HinInches)
        icheck = 0
        # computed_data1 = (cUserInput1 * 12 * 2.54) + cUserInput2
        computed_data1 = (cUserInput1 * 30.48) + cUserInput2
    except:
        computed_data1='Input Error'

    outputdata1.insert(END,computed_data1)

def close_app():
    w.destroy()
    exit()

def retain_app():
    outputdata1.delete(0.0, END)
    inputentry1.delete(0, END)
    inputentry2.delete(0, END)

w = Tk()
w.title("My Height Units App")
w.configure(background="Violet")
#-------------------------------------------------------------
Label (w, text="User Height Input(Feet): ", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)
Label (w, text="User Height Input(Inches): ", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)
inputentry2 = Entry(w, width=10, bg="white")
inputentry2.grid(row=2, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="User Height in Centimeter: ", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=13, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=13, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=13, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
# - The following are the open questions regarding the GUI
#   window:
#   a.) What is the difference between "delete(0.0, END)" 
#       and "delete(0, END)"?
#   b.) Still not able to correctly formant the position of
#       the elements in the dialogue box.
#   c.) Current mapping element method is not clearly understood
# 
# 