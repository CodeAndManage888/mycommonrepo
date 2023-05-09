#**************************************************************
# Date: 072222                                                *
# Title: Making Change                                        *
# Programmer: BoredManager                                    *
# Consider the software that runs on a self-checkout machine. *
# One task that it must be able to perform is to determine    *
# how much change to provide when the shopper pays for a      *
# purchase with cash.                                         *
#                                                             *
# Write a program that begins by reading a number of cents    *
# from the user as an integer. Then your program should       *
# compute and display the denominations of the coins that     *
# should be used to give that amount of change to the shopper.*
# The change should be given using as few coins as possible.  *
# Assume that the machine is loaded with pennies, nickels,    *
# dimes, quarters, loonies and toonies.                       *
#                                                             *
# A one dollar coin was introduced in Canada in 1987. It is   *
# referred to as a loonie because one side of the coin has a  *
# loon (a type of bird) on it. The two dollar coin, referred  *
# to as a toonie, was introduced 9 years later. It’s name is  *
# derived from the combination of the number two and the name *
# of the loonie.                                              *
#                                                             *
# From Google:                                                *
# 100 pennies, 20 nickels, 10 dimes, or 4 quarters;           *
# each = 1 dollar.                                            *
#**************************************************************

from tkinter import *

def click():
    totalnumpenny=inputentry.get()
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    outputdata3.delete(0.0, END)
    outputdata4.delete(0.0, END)
    outputdata5.delete(0.0, END)
    outputdata6.delete(0.0, END)
    icheck = -1
    try:
        cUserInput = int(totalnumpenny)
        icheck = 0
        computed_data1 = cUserInput // 200
        remainder1 = cUserInput % 200

        computed_data2 = remainder1 // 100
        remainder2 = remainder1 % 100

        computed_data3 = remainder2 // 25
        remainder3 = remainder2 % 25

        computed_data4 = remainder3 // 10
        remainder4 = remainder3 % 10

        computed_data5 = remainder4 // 5
        computed_data6 = remainder4 % 5

    except:
        computed_data1='Input Error'
        computed_data2='Input Error'
        computed_data3='Input Error'
        computed_data4='Input Error'
        computed_data5='Input Error'
        computed_data6='Input Error'

    outputdata1.insert(END,computed_data1)
    outputdata2.insert(END,computed_data2)
    outputdata3.insert(END,computed_data3)
    outputdata4.insert(END,computed_data4)
    outputdata5.insert(END,computed_data5)
    outputdata6.insert(END,computed_data6)

def close_app():
    w.destroy()
    exit()

def retain_app():
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    outputdata3.delete(0.0, END)
    outputdata4.delete(0.0, END)
    outputdata5.delete(0.0, END)
    outputdata6.delete(0.0, END)
    inputentry.delete(0, END)

w = Tk()
w.title("My Change Maker App")
w.configure(background="Light Green")
#w.configure(background="Pink")
#-------------------------------------------------------------
Label (w, text="Total Number Of 1 Cents: ", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry = Entry(w, width=10, bg="white")
inputentry.grid(row=1, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="Total Number of Toonies: ", bg="black", fg="white", font="none 12 bold") .grid(row=5, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="white")
outputdata1.grid(row=6, column=0, sticky=W)

Label (w, text="Total Number of Loonies: ", bg="black", fg="white", font="none 12 bold") .grid(row=9, column=0, sticky=W)
outputdata2 = Text(w, width=15, height=1, bg="white")
outputdata2.grid(row=10, column=0, sticky=W)

Label (w, text="Total Number of Quarters: ", bg="black", fg="white", font="none 12 bold") .grid(row=13, column=0, sticky=W)
outputdata3 = Text(w, width=15, height=1, bg="white")
outputdata3.grid(row=14, column=0, sticky=W)

Label (w, text="Total Number of Dimes: ", bg="black", fg="white", font="none 12 bold") .grid(row=17, column=0, sticky=W)
outputdata4 = Text(w, width=15, height=1, bg="white")
outputdata4.grid(row=18, column=0, sticky=W)

Label (w, text="Total Number of Nickels: ", bg="black", fg="white", font="none 12 bold") .grid(row=21, column=0, sticky=W)
outputdata5 = Text(w, width=15, height=1, bg="white")
outputdata5.grid(row=22, column=0, sticky=W)

Label (w, text="Total Number of Pennies: ", bg="black", fg="white", font="none 12 bold") .grid(row=25, column=0, sticky=W)
outputdata6 = Text(w, width=15, height=1, bg="white")
outputdata6.grid(row=26, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=29, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=29, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=29, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()

#**************************************************************
# Lessons Learned:
# - The following are the open questions regarding the GUI
#   window:
#   a.) How do you center the data in the text box?
#   b.) How do you position the elements of windows?