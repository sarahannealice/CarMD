#CarMD main page
import tkinter as tk
import tkinter.ttk as ttk

import warning_lights
import functions

root = tk.Tk()
root.title("CarMD")
root.geometry("400x400")
root.resizable(width=False, height=False)

frame = tk.Frame(
    master=root,
    bg="pink")
frame.pack()

label = tk.Label(
    master=frame,
    text="CarMD by Sarah",
    fg="white",
    bg="#34A2FE",
    width=10,
    height=10,
    padx=10
    )
label.pack()

button = tk.Button(
    master=frame,
    text="click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=functions.root_title(root,"car problems")
)
button.pack()

root.mainloop()