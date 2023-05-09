#**************************************************************
# Date: 073122                                                *
# Title: Distance Units                                       *
# Programmer: BoredManager                                    *
# In this exercise, you will create a program that begins by  *
# reading a measurement in feet from the user. Then your      * 
# program should display the equivalent distance in inches,   * 
# yards and miles. Use the Internet to look up the necessary  * 
# conversion factors if you don’t have them memorized.        * 
#                                                             *
# Google Research:                                            *
# Feet to Inches: 1 Ft = 12 Inches                            *
# Feet to Yards: 1 Ft = 1/3 Yards                             *
# Feet to Miles: 1 Ft = 1/5280 Miles                          *
#**************************************************************

from tkinter import *

def click():
    DinFeet=inputentry1.get()
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    outputdata3.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(DinFeet)
        icheck = 0
        computed_data1 = cUserInput1 * 12
        computed_data2 = cUserInput1 / 3
        computed_data3 = cUserInput1 / 5280
    except:
        computed_data1='Input Error'
        computed_data2='Input Error'
        computed_data3='Input Error'

    outputdata1.insert(END,computed_data1)
    outputdata2.insert(END,computed_data2)
    outputdata3.insert(END,computed_data3)

def close_app():
    w.destroy()
    exit()

def retain_app():
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    outputdata3.delete(0.0, END)
    inputentry1.delete(0, END)

w = Tk()
w.title("My Distance Units App")
w.configure(background="Light Blue")
#-------------------------------------------------------------
Label (w, text="User Distance Input(Feet): ", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="User Distance in Inches: ", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label (w, text="User Distance in Yards: ", bg="black", fg="white", font="none 12 bold") .grid(row=12, column=0, sticky=W)
outputdata2 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata2.grid(row=13, column=0, sticky=W)

Label (w, text="User Distance in Miles: ", bg="black", fg="white", font="none 12 bold") .grid(row=14, column=0, sticky=W)
outputdata3 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata3.grid(row=15, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=16, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=16, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=16, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
# - The following are the open questions regarding the GUI
#   window:
#  