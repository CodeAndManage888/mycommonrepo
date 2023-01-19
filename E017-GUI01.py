#**************************************************************
# Date: 080122                                                *
# Title: Heat Capacity                                        *
# Status: Working (In Progress / Testing / Working)           *
# Programmer: BoredManager                                    *
# The amount of energy required to increase the temperature   *
# of one gram of a material by one degree Celsius is the      *
# material’s specific heat capacity, C. The total amount of   *
# energy required to raise m grams of a material by ∆T        *
# degrees Celsius can be computed using the formula:          *
#                      q = mC∆T                               *
# Write a program that reads the mass of some water and the   * 
# temperature change from the user. Your program should       * 
# display the total amount of energy that must be added or    * 
# removed to achieve the desired temperature change.          *
#                                                             *
# Hint: The specific heat capacity of water is 4.186 J /g◦C.  *
# Because water has a density of 1.0 gram per millilitre, you * 
# can use grams and millilitres interchangeably in this       * 
# exercise.                                                   *
#                                                             *
# Extend your program so that it also computes the cost of    * 
# heating the water. Electricity is normally billed using     * 
# units of kilowatt hours rather than Joules. In this         * 
# exercise, you should assume that electricity costs 8.9      * 
# cents per kilowatt-hour. Use your program to compute the    * 
# cost of boiling water for a cup of coffee.                  *
#                                                             *
# Hint: You will need to look up the factor for converting    * 
# between Joules and kilowatt hours to complete the last part * 
# of this exercise.                                           *
#                                                             *
# Computed Result Validated:                                  *
# https://www.omnicalculator.com/physics/specific-heat        *
#**************************************************************

from tkinter import *
import math

def click():
    SpHtCapH2O = 4.186
    kWhperOneJoule = 3.6**6
    CostperKwH = 8.9
    UsrInputMass=inputentry1.get()
    UsrInputTempChg=inputentry2.get()
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    outputdata3.delete(0.0, END)
    icheck = -1
    try:
        cUserInput1 = float(UsrInputMass)
        cUserInput2 = float(UsrInputTempChg)
        icheck = 0
        computed_data1 = cUserInput1 * SpHtCapH2O * cUserInput2
        computed_data2 = computed_data1 / kWhperOneJoule
        computed_data3 = (computed_data2 * CostperKwH) / 100
    except:
        computed_data1, computed_data2, computed_data3 ='Input Error' , 'Input Error', 'Input Error'

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
    inputentry2.delete(0, END)

w = Tk()
w.title("My Heat Capacity App")
w.configure(background="Light Green")
#-------------------------------------------------------------
Label (w, text="User Input Water Mass(Grams):", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry1 = Entry(w, width=10, bg="white")
inputentry1.grid(row=1, column=18, sticky=W)

Label (w, text="User Input Temp Change(Celsius):", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)
inputentry2 = Entry(w, width=10, bg="white")
inputentry2.grid(row=2, column=18, sticky=W)

Button(w, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (w, text="Total Amount of Energy(Joules):", bg="black", fg="white", font="none 12 bold") .grid(row=10, column=0, sticky=W)
outputdata1 = Text(w, width=15, height=1, bg="blue", fg="white", font="none 12 bold")
outputdata1.grid(row=11, column=0, sticky=W)

Label (w, text="Total Amount of Energy(kWh)::", bg="black", fg="white", font="none 12 bold") .grid(row=12, column=0, sticky=W)
outputdata2 = Text(w, width=15, height=1, bg="blue", fg="white", font="none 12 bold")
outputdata2.grid(row=13, column=0, sticky=W)

Label (w, text="Total Energy Cost($)::", bg="black", fg="white", font="none 12 bold") .grid(row=14, column=0, sticky=W)
outputdata3 = Text(w, width=15, height=1, bg="blue", fg="white", font="none 12 bold")
outputdata3.grid(row=15, column=0, sticky=W)

Label (w, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=16, column=0, sticky=W)
Button(w, text="Yes", width=7, command=close_app) .grid(row=16, column=18, sticky=W)
Button(w, text="No", width=7, command=retain_app) .grid(row=16, column=25, sticky=W)
#-------------------------------------------------------------

w.mainloop()
#**************************************************************
# Lessons Learned:
# 
