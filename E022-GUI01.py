#**************************************************************
# Date: 011823                                                *
# Title: Area of a Triangle 2                                 *
# Status: Working (In Progress / Testing / Working)           *
# Programmer: BoredManager                                    *
# In the previous exercise you created a program that computed*
# the area of a trianglewhen the length of its base and its   *
# height were known. It is also possible to computethe area of*
# a triangle when the lengths of all three sides are known.   *
# Let s1, s2 and s3 be the lengths of the sides. Let          *
# s = (s1+ s2+ s3)/2. Then the area of the trianglecan be     *
# calculated using the following formula:                     *
#        Area = sqrt(s * (s-s1) * (s-s2) * (s-S3))            *
# Develop a program that reads the lengths of the sides of a  * 
# triangle from the user anddisplays its area.                *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
from tkinter import *
import math

def click():
    UsrInputSide1 = inputentry1.get()
    UsrInputSide2 = inputentry2.get()
    UsrInputSide3 = inputentry3.get()
    outputdata1.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(UsrInputSide1)
        cUserInput2 = float(UsrInputSide2)
        cUserInput3 = float(UsrInputSide3)
        icheck = 0
        cTotalSide = (cUserInput1 + cUserInput2 + cUserInput3) / 2
        computed_data1 = math.sqrt(cTotalSide * (cTotalSide - cUserInput1) 
                                              * (cTotalSide - cUserInput2)
                                              * (cTotalSide - cUserInput3))
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
    inputentry3.delete(0, END)


w = Tk()
w.title("My Area of a Triangle 2 App")
w.configure(background="Light Yellow")

#-------------------------------------------------------------
Label(w, text="Side 1(units):", bg="black", fg="white",
      font="none 12 bold").grid(row=0, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=0, column=1, sticky=W)

Label(w, text="Side 2(units):", bg="black", fg="white",
      font="none 12 bold").grid(row=1, column=0, sticky=W)
inputentry2 = Entry(w, width=10, bg="white")
inputentry2.grid(row=1, column=1, sticky=W)

Label(w, text="Side 3(units):", bg="black", fg="white",
      font="none 12 bold").grid(row=2, column=0, sticky=W)
inputentry3 = Entry(w, width=10, bg="white")
inputentry3.grid(row=2, column=1, sticky=W)

Button(w, text="Submit", width=8, command=click).grid(row=0,
                                                      column=2,
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
outputdata1.grid(row=10, column=1, sticky=W)

Label(w,
      text="Close Application?",
      bg="black",
      fg="white",
      font="none 12 bold").grid(row=16, column=1, sticky=W)
Button(w, text="Yes", width=7, command=close_app).grid(row=16,
                                                       column=2,
                                                       sticky=W)
Button(w, text="No", width=7, command=retain_app).grid(row=16,
                                                       column=3,
                                                       sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
#
