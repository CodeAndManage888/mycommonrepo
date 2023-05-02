import tkinter as tk
import math

def calculate():
    # get the user input
    radius = float(entry_radius.get())
    height = float(entry_height.get())

    # calculate the volume
    volume = math.pi * radius**2 * height

    # round the volume to one decimal place
    volume = round(volume, 1)

    # display the volume in the label
    label_result.config(text=f'Volume: {volume}')

# create the main window
window = tk.Tk()
window.title('Cylinder Volume')

# create the widgets
label_radius = tk.Label(text='Radius:')
entry_radius = tk.Entry()
label_height = tk.Label(text='Height:')
entry_height = tk.Entry()
button_calculate = tk.Button(text='Calculate', command=calculate)
label_result = tk.Label(text='Volume:')

# layout the widgets
label_radius.grid(row=0, column=0, sticky='e')
entry_radius.grid(row=0, column=1)
label_height.grid(row=1, column=0, sticky='e')
entry_height.grid(row=1, column=1)
button_calculate.grid(row=2, column=0, columnspan=2, pady=5)
label_result.grid(row=3, column=0, columnspan=2, pady=5)

# run the main loop
window.mainloop()

# This program creates a simple GUI with four widgets: two Entry widgets for the user to input the radius and height, a Button widget to trigger the calculation, and a Label widget to display
