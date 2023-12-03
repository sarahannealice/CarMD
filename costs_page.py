import tkinter as tk

from fonts import *

class RepairCosts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent):
        self.controller = controller
        
        self.configure(bg="light sea green")

        self.lbl_title = tk.Label(
            master=self,
            text="",
            font=TITLE,
            bg="light sea green"
        )
        self.lbl_title.grid(row=0, column=0, columnspan=4)