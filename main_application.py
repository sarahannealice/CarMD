import tkinter as tk

        
from title_page import TitlePage
from symptoms_page import SymptomsPage
from details_page import DetailsPage
from toplevel_page import DisplayToplevel
from lights_page import LightsPage

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
        self.geometry("800x600")
        self.resizable(width=False, height=False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty arry
        self.frames = {}

        title = ""
        # iterating through a tuple consisting of different page layouts
        for F in (TitlePage, SymptomsPage, DetailsPage, LightsPage):
            frame = F(container, self)

            #initializing frame of that object
            self.frames[F] = frame 
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(TitlePage)

    # displays current frame
    def show_frame(self, cont, title=None, details=None):
        frame = self.frames[cont]
        frame.tkraise()

        if title is not None and isinstance(frame, DetailsPage):
            frame.update_content(title, details)

    # displays popup window using toplevel()
    def show_toplevel(self, title=None, url=None):
        
        # popup for repair costs
        if title is not None:
            DisplayToplevel.repair_cost(DisplayToplevel, title, url)

        # popup for warning lights

# initializing application and displaying it
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()