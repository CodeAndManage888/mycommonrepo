import tkinter as tk
#---------------------------------------------------------------------
window = tk.Tk()
window.title("Generic Dialogue Box [Place GM]")
#---------------------------------------------------------------------
frame_box1 = tk.Frame(
	master=window, 
	width=500,
	height = 250,
	bg="light blue"
	)
frame_box1.pack(fill=tk.BOTH, side=tk.TOP,expand=True)
label_01 = tk.Label(
	master=frame_box1,
	text = "User Entry: ",
	bg="light blue"
	)
label_01.place(x=0, y=0)
entry_01 = tk.Entry(
	master=frame_box1,
	width = 10
	)
entry_01.place(x=80, y=0)
click_button = tk.Button(
	master=frame_box1,
	text = "Submit",
	width = 6
	)
click_button.place(x=200, y=0)
label_02 = tk.Label(
	master=frame_box1,
	text = "Output: ",
	bg="light blue"
	)
label_02.place(x=0, y=20)
output_01 = tk.Entry(
	master=frame_box1,
	width = 10
	)
output_01.place(x=80, y=20)
#---------------------------------------------------------------------
window.mainloop()
#---------------------------------------------------------------------
#greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()
#---------------------------------------------------------------------
#label = tk.Label(
#	text = "Hello, Tkinter",
#	foreground ="white",
#	background = "black",
#	width = 10,
#	height = 10
#)
#---------------------------------------------------------------------
#button = tk.Button(
#	text = "Click Me!",
#	foreground ="yellow",
#	background = "blue",
#	width = 25,
#	height = 5
#)
#---------------------------------------------------------------------
#entry = tk.Entry(
#	fg = "yellow",
#	bg = "blue",
#	width = 50
#)
#---------------------------------------------------------------------
#label = tk.Label(text="Name")
#entry = tk.Entry()
#---------------------------------------------------------------------
#text_box = tk.Text()
#---------------------------------------------------------------------
#frame_a = tk.Frame()
#label_a = tk.Label(master=frame_a, text="I'm frame A")
#label_a.pack()

#frame_b = tk.Frame()
#label_b = tk.Label(master=frame_b, text="I'm frame B")
#label_b.pack()

#frame_b.pack()
#frame_a.pack()
#---------------------------------------------------------------------
#label.pack()
#button.pack()
#entry.pack()
#text_box.pack()
#frame.pack()
#---------------------------------------------------------------------

