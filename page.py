import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)

class Page(tk.Frame):
    def __init__(self, parent, controller, title):
        tk.Frame.__init__(self, parent, title)
        self.title = title
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
        from title_page import TitlePage
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(TitlePage))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)