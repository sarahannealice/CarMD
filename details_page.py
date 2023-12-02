import tkinter as tk

from fonts import *
from symptoms_page import *

class DetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="light goldenrod yellow")

        self.lbl_title = tk.Label(
            master=self,
            text="",
            font=TITLE,
            bg="light goldenrod yellow"
        )
        self.lbl_title.grid(row=0, column=0, columnspan=4)

        self.txt_details = tk.Text(
            master=self,
            wrap=tk.WORD,
            width=57,
            height=10,
            bd=0,
            bg="light yellow2",
            font=DETAILS
        )
        self.txt_details.grid(row=1, column=0, columnspan=4, padx=25, pady=5)

        scrollb = tk.Scrollbar(
            master=self,
            command=self.txt_details.yview
        )
        scrollb.grid(row=1, column=4, sticky='nsew')
        self.txt_details['yscrollcommand'] = scrollb.set

        # displays repair costs
        btn = tk.Button(
            master=self,
            text="Repair Costs",
            #command=repairs(root, frame, "Heater Repair Costs", "light sea green")
        )
        btn.grid(row=3, column=0, columnspan=2)
        
        # return to title page
        from title_page import TitlePage
        btn_home = tk.Button(
            master=self,
            text="return",
            bg="light grey",
            fg="black",
            command=lambda: controller.show_frame(TitlePage)
        )
        btn_home.grid(row=3, column=2, columnspan=2)

    # updates title and content of page
    def update_content(self, title, details):
        self.lbl_title.config(text=title)

        self.txt_details.config(state="normal")
        self.txt_details.delete("1.0", tk.END)
        self.txt_details.insert(tk.END, details)
        self.txt_details.config(state="disabled")