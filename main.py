#CarMD main page
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
label = tk.Label(
    text="CarMD by Sarah",
    foreground="white",
    background="black"
    )

ttklabel = ttk.Label(text="CarMD by Sarah")
label.pack()
ttklabel.pack()

root.mainloop()