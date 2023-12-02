import tkinter as tk

from fonts import *
from symptoms_page import *

class DetailsPage(tk.Frame):
    def __init__(self, parent, controller, title):
        tk.Frame.__init__(self, parent, title)
        self.controller = controller

        self.configure(bg="light yellow")

        self.lbl_title = tk.Label(
            master=self,
            text=""
        )
        self.lbl_title.grid(row=0, column=0, columnspan=4)

        btn = tk.Button(
            master=self,
            text="Repair Costs",
            #command=repairs(root, frame, "Heater Repair Costs", "light sea green")
        )
        btn.grid(row=0, column=1)

        self.txt_details = tk.Text(
            master=self,
            wrap=tk.WORD,
            width=50,
            height=10
        )
        self.txt_details.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        
        from title_page import TitlePage
        btn_home = tk.Button(
            master=self,
            text="return",
            bg="light grey",
            fg="black",
            command=lambda: controller.show_frame(TitlePage)
        )
        btn_home.grid(row=2, column=0, columnspan=4)

    def update_content(self, title, details):
        self.lbl_title.config(text=title)
        self.txt_details.delete("1.0", tk.END)
        self.txt_details.insert(tk.END, details)