from tkinter import *
class App:
    def __init__(self, master):
    
        frame = Frame(master)
        frame.pack()
    
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
    
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
    
    def say_hi(self):
        print ("hi there, everyone!")

root = Tk()
app = App(root)
root.mainloop()














#from tkinter import *
#
#ws = Tk()
#ws.title('PythonGuides')
#ws.geometry('400x400')
#ws.config(bg='#31403C')
#
#Spinbox(
#    ws,
#    from_=1,
#    to=10,
#    font=('sans-serif', 14), 
#
#).pack(pady=20)

#ws.mainloop()



#print ("Hello World")
#text00 = input("Write Something : ")
#print (text00)
#writeout = format(9999999999*999999999,'.0f')
#print (writeout)
#writeout00 = 999999999999*999999999999
#writeout01 = int(writeout00)
#print (writeout01)