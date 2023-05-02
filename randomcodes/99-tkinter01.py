import tkinter as tk
window = tk.Tk()

#------------------------------------------------------
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
button = tk.Button(
    text="Click Me",
    fg="yellow",
    bg="blue",
    width=25,
    height=5
)
frame_a = tk.Frame()
label1 = tk.Label(
    master = frame_a,
    text="Input Space"
)
entry = tk.Entry(master = frame_a)
#label2 = tk.Label(
#    master = frame_a,
#    text="Input Text"
#)
#text_box = tk.Text()
#------------------------------------------------------
label.pack()
button.pack()
label1.pack()
entry.pack()
#label2.pack()
#ext_box.pack()
frame_a.pack()
#------------------------------------------------------
window.mainloop()
#------------------------------------------------------