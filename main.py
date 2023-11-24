#CarMD main page
import tkinter as tk
import tkinter.ttk as ttk

from common_symptoms import symptoms_layout
from repair_costs import repairs

root = tk.Tk()
root.title("CarMD")
root.geometry("600x400")
root.resizable(width=False, height=False)
root.configure(bg="pink")

frame = tk.Frame(
    master=root,
    padx=10,
    pady=10,
)
frame.pack(side="top")

btn = tk.Button(
    master=frame,
    text="bs4",
    command=lambda:repairs(root, frame, "Heater Repair Costs")
)
btn.grid(row=0, column=1)

label = tk.Label(
    master=frame,
    text="CarMD by Sarah",
    fg="navy",
    font=("Ariel", 18),
    )
label.grid(row=0, column=0)

btn_left = tk.Button(
    master=frame,
    text="common symptoms",
    bg="blue",
    fg="yellow",
    font=16,
    command=lambda: symptoms_layout(root, frame)
)
btn_left.grid(row=1, column=0)

btn_right = tk.Button(
    master=frame,
    text="warning lights",
    bg="orange",
    fg="black",
    font=16
)
btn_right.grid(row=1, column=1)

root.mainloop()