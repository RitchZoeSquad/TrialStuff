#!/usr/bin/env python3
import os
import tkinter


import tkinter as tk
import time

root = tk.Tk()

def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")

    # Update the timeText Label box with the current time
    timeText.configure(text=current)

    # Call the update_timeText() function after 1 second
    root.after(1000, update_timeText)

# Create a timeText Label (a text box)
timeText = tk.Label(root, text="", font=("Helvetica", 150))
timeText.pack()

# Update the timeText Label after 1 second (1000 milliseconds)
root.after(1000, update_timeText)

root.mainloop()
##add shebang to the top of the file for scripting to
##run the file in the terminal




