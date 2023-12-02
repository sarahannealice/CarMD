import tkinter as tk
from tkinter import font as tkfont

        
from title_page import TitlePage
from page import Page
from symptoms_page import SymptomsPage
from details_page import DetailsPage

class MainApplication(tk.Tk):
    """
    frame object holding the different pages
    controller to maneuver pages

    **note**
    simply moves the desired frame to the top rather than destroying/forgetting
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("CarMD")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty arry
        self.frames = {}

        title = ""
        # iterating through a tuple consisting of different page layouts
        for F in (TitlePage, SymptomsPage, DetailsPage):
            frame = F(container, self, title)

            #initializing frame of that object
            self.frames[F] = frame 
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(TitlePage, "carmd")

    #displays current frame
    def show_frame(self, cont, title):
        frame = self.frames[cont]
        frame.tkraise()

        if title is not None and isinstance(frame, DetailsPage):
            frame.update_content(title)



# initializing application and displaying it
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()