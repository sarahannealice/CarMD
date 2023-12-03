import tkinter as tk
from tkinter import ttk

from fonts import *

from symptoms_page import *

class TitlePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="pink")

        label = tk.Label(
            master=self,
            text="CarMD by Sarah",
            fg="navy",
            bg="pink",
            font=TITLE,
            )
        label.grid(row=0, column=0, columnspan=2)

        btn_left = tk.Button(
            master=self,
            text="common symptoms",
            bg="blue",
            fg="yellow",
            font=16,
            command=lambda: controller.show_frame(SymptomsPage)
        )
        btn_left.grid(row=1, column=0)

        btn_right = tk.Button(
            master=self,
            text="warning lights",
            bg="orange",
            fg="black",
            font=16
        )
        btn_right.grid(row=1, column=1)