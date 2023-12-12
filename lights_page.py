import tkinter as tk

from fonts import *

from symptoms_page import *

class LightsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="purple")

        label = tk.Label(
            master=self,
            text="Warning Lights",
            fg="navy",
            bg="purple",
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

# icons
        #<a href="https://www.flaticon.com/free-icons/automotive" title="automotive icons">Automotive icons created by LAFS - Flaticon</a>