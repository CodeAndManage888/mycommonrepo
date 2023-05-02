import tkinter as tk
#---------------------------------------------------------------------
window = tk.Tk()
window.title("Generic Dialogue Box [Grid GM]")
#---------------------------------------------------------------------
frame_box1 = tk.Frame(
	master=window, 
	bg="light green",
	relief=tk.RAISED,
	borderwidth=1
	)
frame_box1.grid(row=0, column=0)
label_01 = tk.Label(
	master=frame_box1,
	text = "Entry: ",
	bg="light green"
	)
label_01.pack()
frame_box2 = tk.Frame(
	master=window, 
	bg="light green",
	relief=tk.RAISED,
	borderwidth=1
	)
frame_box2.grid(row=0, column=1)
entry_01 = tk.Entry(
	master=frame_box2,
	width = 10
	)
entry_01.grid(row=0, column=0)
entry_02 = tk.Entry(
	master=frame_box2,
	width = 10
	)
entry_02.grid(row=0, column=1)
#---------------------------------------------------------------------
window.mainloop()
#---------------------------------------------------------------------
