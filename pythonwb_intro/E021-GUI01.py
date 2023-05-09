#**************************************************************
# Date: 110722 / 120122 / 011823                              *
# Title: Area of a Triangle                                   *
# Status: Working (In Progress / Testing / Working)           *
# Programmer: BoredManager                                    *
# The area of a triangle can be computed using the following  *
# formula, where b is the length of the base of the triangle, *
# and h is its height:                                        *
#                  Area = (b x h) / 2                         *
# Write a program that allows the user to enter values for b  *
# and h. The programshould then compute and display the area  *
# of a triangle with base length b and height h.              *
#                                                             *
# Computed Result Validated:                                  *
# Verified via google.com                                     *
#                                                             *
#**************************************************************
from tkinter import *
import math


def click():
    UsrInputHeight = inputentry1.get()
    UsrInputBase = inputentry2.get()
    outputdata1.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(UsrInputHeight)
        cUserInput2 = float(UsrInputBase)
        icheck = 0
        computed_data1 = (cUserInput1 * cUserInput2) / 2
    except:
        computed_data1 = 'Input Error'

    outputdata1.insert(END, computed_data1)


def close_app():
    w.destroy()
    exit()


def retain_app():
    outputdata1.delete(0.0, END)
    inputentry1.delete(0, END)
    inputentry2.delete(0, END)


w = Tk()
w.title("My Area of a Triangle App")
w.configure(background="Light Yellow")

#-------------------------------------------------------------
Label(w, text="Height(units):", bg="black", fg="white",
      font="none 12 bold").grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

Label(w,
      text="Base Length(units):",
      bg="black",
      fg="white",
      font="none 12 bold").grid(row=2, column=0, sticky=W)
inputentry2 = Entry(w, width=10, bg="white")
inputentry2.grid(row=2, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click).grid(row=1,
                                                      column=28,
                                                      sticky=W)

Label(w,
      text="Area of the Triangle:",
      bg="black",
      fg="white",
      font="none 12 bold").grid(row=10, column=0, sticky=W)
outputdata1 = Text(w,
                   width=15,
                   height=1,
                   bg="green",
                   fg="white",
                   font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label(w,
      text="Close Application?",
      bg="black",
      fg="white",
      font="none 12 bold").grid(row=16, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app).grid(row=16,
                                                       column=18,
                                                       sticky=W)
Button(w, text="No", width=7, command=retain_app).grid(row=16,
                                                       column=25,
                                                       sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
#
