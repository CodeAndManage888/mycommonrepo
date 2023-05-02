from tkinter import * 

def click():
    entered_data=inputentry.get()
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    icheck = -1
    try:
        cUserInput = int(entered_data)
        icheck = 0
        computed_data1 = cUserInput * 100
        computed_data2 = cUserInput * 10
    except:
        computed_data1='Input Error'
        computed_data2='Input Error'       
    
    outputdata1.insert(END,computed_data1)
    outputdata2.insert(END,computed_data2)

def close_app():
    window.destroy()
    exit()
    
def retain_app():
    outputdata1.delete(0.0, END)
    outputdata2.delete(0.0, END)
    inputentry.delete(0, END)

window = Tk()
window.title("My WindowName App")
window.configure(background="gray")

Label (window, text="Enter Input One: ", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
inputentry = Entry(window, width=10, bg="white")
inputentry.grid(row=1, column=18, sticky=W)

Button(window, text="Submit", width=8, command=click) .grid(row=1, column=28, sticky=W)

Label (window, text="Output Data 1: ", bg="black", fg="white", font="none 12 bold") .grid(row=5, column=0, sticky=W)
outputdata1 = Text(window, width=15, height=1, bg="white")
outputdata1.grid(row=6, column=0, sticky=W)

Label (window, text="Output Data 2: ", bg="black", fg="white", font="none 12 bold") .grid(row=9, column=0, sticky=W)
outputdata2 = Text(window, width=15, height=1, bg="white")
outputdata2.grid(row=10, column=0, sticky=W)

Label (window, text="Close Application?", bg="black", fg="white", font="none 12 bold") .grid(row=11, column=0, sticky=W)
Button(window, text="Yes", width=7, command=close_app) .grid(row=11, column=18, sticky=W)
Button(window, text="No", width=7, command=retain_app) .grid(row=11, column=25, sticky=W)

window.mainloop()
#  - There are still a lot of parts of the code that I don't fully understand. I somehow figured out how
#    to use it but I still need to know how it works. 
#  - The placing of the elements are very clanky and difficult to place. I need to read more about
#    this grid command.
#  - The label command is too long is ther a better way to code this? The program is very disorganized.
#-------------------------------------------------------------------
#