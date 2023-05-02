import tkinter as tk
import time
#---------------------------------------------------------------------
def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1

window = tk.Tk()
window.title("System Message")
#---------------------------------------------------------------------
frame_box1 = tk.Frame(
	master=window, 
	width=350,
	height = 50,
	bg="red"
	)
frame_box1.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
label_01 = tk.Label(
	master=frame_box1,
	text = "This machine will reboot in 5 mins.",
	font="none 12 bold",
	fg="white",
	bg="red"
	)
label_01.place(x=0, y=0)
label_02 = tk.Label(
	master=frame_box1,
	text = "Please save your work ASAP!",
	font="none 12 bold",
	fg="white",
	bg="red"
	)
label_02.place(x=0, y=20)
#frame_box2 = tk.Frame(
#	master=window, 
#	bg="red",
#	relief=tk.RAISED,
#	borderwidth=1
#	)
#frame_box2.grid(row=0, column=0)
#label_02 = tk.Label(
#	master=frame_box2,
#	text = "Please save your work ASAP!",
#	bg="red"
#	)
#label_01.pack()
#entry_01 = tk.Entry(
#	master=frame_box2,
#	width = 10
#	)
#entry_01.grid(row=0, column=0)
#entry_02 = tk.Entry(
#	master=frame_box2,
#	width = 10
#	)
#entry_02.grid(row=0, column=1)
#---------------------------------------------------------------------
window.mainloop()
#countdown(int(300))
#---------------------------------------------------------------------
