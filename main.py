#CarMD main page
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
label = tk.Label(
    text="CarMD by Sarah",
    fg="white",
    bg="#34A2FE",
    width=10,
    height=10,
    padx=10
    )
label.pack()

button = tk.Button(
    text="click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)


root.mainloop()