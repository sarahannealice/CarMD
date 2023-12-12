import tkinter as tk
from fonts import *

from symptoms_page import *
from lights_page import *

class TitlePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="pink")

    #-------grid weights-------#
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        label = tk.Label(
            master=self,
            text="CarMD by sarah",
            fg="navy",
            bg="pink",
            font=TITLE,
            )
        label.grid(row=1, column=0, columnspan=2)

        btn_left = tk.Button(
            master=self,
            text="common symptoms",
            bg="light blue",
            fg="navy",
            font=BTNS,
            command=lambda: controller.show_frame(SymptomsPage)
        )
        btn_left.grid(row=2, column=0)

        btn_right = tk.Button(
            master=self,
            text="warning lights",
            bg="thistle",
            fg="dark slate blue",
            font=BTNS,
            command=lambda: controller.show_frame(LightsPage)
        )
        btn_right.grid(row=2, column=1)