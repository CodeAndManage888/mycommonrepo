#import tkinter as tk
#---------------------------------------------------------------------
#window = tk.Tk()
#window.title("System Message")
#window.geometry("350x50")
#---------------------------------------------------------------------
#frame_box1 = tk.Frame(
#	master=window, 
#	width=350,
#	height = 50,
#	bg="red"
#	)
#frame_box1.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
#label_01 = tk.Label(
#	master=frame_box1,
#	text = "This machine will reboot in 5 mins.",
#	font="none 12 bold",
#	fg="white",
#	bg="red"
#	)
#label_01.place(x=0, y=0)
#label_02 = tk.Label(
#	master=frame_box1,
#	text = "Please save your work ASAP!",
#	font="none 12 bold",
#	fg="white",
#	bg="red"
#	)
#label_02.place(x=0, y=20)
#---------------------------------------------------------------------
#window.mainloop()
#---------------------------------------------------------------------
import pyautogui
import os
os.environ['HOME']
#---------------------------------------------------------------------
pyautogui.alert(text='This machine will reboot in 5 mins. Please save your work ASAP!' , title='System Message')

