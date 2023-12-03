import tkinter as tk

from fonts import *
from details_page import DetailsPage

class SymptomsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="light blue")

        lbl_symptopms = tk.Label(
            master=self,
            text="symptoms",
            fg="navy",
            font=("Arial", 18)
        )
        lbl_symptopms.grid(row=0, column=0, columnspan=3)

        # button details
        btn_heater = tk.Button(
            master=self,
            text="Heater not working",
            fg="white",
            bg="navy",
            font=14,
            command=lambda:self.show_details("Heater not working", brkn_heater)
        )

        btn_ac = tk.Button(
            master=self,
            text="A/C not working",
            fg="white",
            bg="navy",
            font=14,
            command=lambda:self.show_details("How a heating system works", brkn_ac)
        )
        
        btn_oil_leak = tk.Button(
            master=self,
            text="Car leaking oil",
            fg="white",
            bg="navy",
            font=14,
            command=lambda:self.show_details("Oil Leak", brkn_ac)
        )

        # adding buttons to frame
        btn_heater.grid(row=1, column=0, padx=5, pady=5)
        btn_ac.grid(row=1, column=1, padx=5, pady=5)
        btn_oil_leak.grid(row=1, column=2, padx=5, pady=5)

        # return to previous page
        from title_page import TitlePage
        btn_home = tk.Button(
            master=self,
            text="return",
            bg="light grey",
            fg="black",
            command=lambda: controller.show_frame(TitlePage)
        )
        btn_home.grid(row=2, column=0, columnspan=2)

    # uses controller to display desired details
    def show_details(self, title, details):
        self.controller.show_frame(DetailsPage, title, details)



# ----------individual symptom details---------- #
brkn_heater = """A vehicle's heating system is also part of its cooling system.
The coolant is circulated through the engine in which it absorbs heat,
is sent to the radiator where it dissipates. This heated coolant can be expelled through the dashboard
if the heater is turned on.

Some reasons your heating system isn't working could include:
* the cooling system
* the heater core
* the heater valves
* the blower fan

> Cooling system issues
    ->coolant level: if low, not enough warmed coolant may be passed to the heater core preventing
        it from producing adequate heat.
        
      solution: a fix would be to top up the coolant. If the levels are low due to a leak, it would
        be best to """

brkn_ac = """this is where the info for a broken ac would go"""