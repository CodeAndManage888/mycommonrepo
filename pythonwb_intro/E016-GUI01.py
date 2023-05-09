#**************************************************************
# Date: 073122                                                *
# Title: Area and Volume                                      *
# Programmer: BoredManager                                    *
# Write a program that begins by reading a radius, r, from    * 
# the user. The program will continue by computing and        * 
# displaying the area of a circle with radius r and the       *
# volume of a sphere with radius r. Use the pi constant in    *
# the math module in your calculations.                       *
#                                                             *
# Hint: The area of a circle is computed using the formula    * 
# area = πr2. The volume of a sphere is computed using the    * 
# formula volume = 4/3πr3.                                    *
#                                                             *
#**************************************************************

from tkinter import *
import math

def click():
    UsrInputRaduis=inputentry1.get()
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(UsrInputRaduis)
        icheck = 0
        # computed_data1 = math.pi * (cUserInput1 ** 2)
        # computed_data2 = (4/3) * math.pi * (cUserInput1 ** 3)
        computed_data1, computed_data2 = math.pi * (cUserInput1 ** 2) , (4/3) * math.pi * (cUserInput1 ** 3)
    except:
        computed_data1, computed_data2 ='Input Error' , 'Input Error'

    outputdata1.insert(END,computed_data1)
    outputdata2.insert(END,computed_data2)

def close_app():
    w.destroy()
    exit()

def retain_app():
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    inputentry1.delete(0, END)

w = Tk()
w.title("My Area and Volume App")
w.configure(background="Light Yellow")
#-------------------------------------------------------------
Label (w, text="User Radius Input(Unit):", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="Area of a Circle(Square Units):", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label (w, text="Volume of a Sphere(Cubic Units):", bg="black", fg="white", font="none 12 bold") .grid(row=12, column=0, sticky=W)
outputdata2 = Text(w, width=15, height=1, bg="green", fg="white", font="none 12 bold")
outputdata2.grid(row=13, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=16, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=16, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=16, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
# - The exercise are now simple with me just reusing code 
#   template with the input processing being modified to 
#   satisfy the requirements. 
# - The following are the open questions regarding the GUI
#   window: