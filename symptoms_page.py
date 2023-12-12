import tkinter as tk
import requests
from bs4 import BeautifulSoup

from fonts import *

class SymptomsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="light blue")
        self.url = ""

    #-------grid weights-------#
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        lbl_symptopms = tk.Label(
            master=self,
            text="Common Symptoms",
            fg="midnight blue",
            bg="light blue",
            font=TITLE
        )
        lbl_symptopms.grid(row=0, column=0, columnspan=4)

    #-------buttons-------#
        #---row 1---#
        btn_heater = tk.Button(
            master=self,
            text="Heater Not Working",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Heater Blowing Cold Air?\nHere's Why and What to Do About It")
        )
        btn_heater.grid(row=1, column=0, pady=10)

        btn_ac = tk.Button(
            master=self,
            text="A/C Not Working",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Car AC Not Working? Weak airflow?\nTop 8 Things to Check")
        )
        btn_ac.grid(row=1, column=1, pady=10)
        
        btn_oil_leak = tk.Button(
            master=self,
            text="Car Leaking Oil",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Car Leaking Oil? Possible Causes\nand What to Do About It")
        )
        btn_oil_leak.grid(row=1, column=2, pady=10)
        
        btn_brk_pads = tk.Button(
            master=self,
            text="Key Won't Turn",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("What To Do If Your Ignition\nKey Won’t Turn")
        )
        btn_brk_pads.grid(row=1, column=3, pady=10)
        
        #---row 2---#
        btn_engine_hot = tk.Button(
            master=self,
            text="Engine Overheating",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Car Engine Overheating:\nWhy It’s Happening and How to Fix It")
        )
        btn_engine_hot.grid(row=2, column=0, pady=10)

        btn_rough_idle = tk.Button(
            master=self,
            text="Rough Idle",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Rough Idle Causes and How to Fix Them")
        )
        btn_rough_idle.grid(row=2, column=1, pady=10)
        
        btn_liquid_leak = tk.Button(
            master=self,
            text="Fluid Leaks",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("What Fluid Is Leaking From Your Car?\nA Color-Coded Guide")
        )
        btn_liquid_leak.grid(row=2, column=2, pady=10)
        
        btn_spongy_brk = tk.Button(
            master=self,
            text="Soft Brakes",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Soft, Spongy Brakes and What to Do")
        )
        btn_spongy_brk.grid(row=2, column=3, pady=10)
        
        #---row 3---#
        btn_car_pull = tk.Button(
            master=self,
            text="Pulling Left/Right",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Why is My Car Pulling to the Left or Right?")
        )
        btn_car_pull.grid(row=3, column=0, pady=10)

        btn_car_shake = tk.Button(
            master=self,
            text="Car Shaking",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Why Is Your Vehicle Shaking?\nSymptoms, Causes and Solutions")
        )
        btn_car_shake.grid(row=3, column=1, pady=10)
        
        btn_shake_brk = tk.Button(
            master=self,
            text="Battery Not Jumping",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("Jumpstart Not Working?\nHere Are The Possible Reasons")
        )
        btn_shake_brk.grid(row=3, column=2, pady=10)
        
        btn_bat_replace = tk.Button(
            master=self,
            text="Engine Stalling",
            fg="midnight blue",
            bg="lightsteelblue",
            font=BTNS,
            width=13,
            wraplength=110,
            command=lambda:self.show_details("How to Fix Stalling and Other Issues\nAfterReplacing the Battery")
        )
        btn_bat_replace.grid(row=3, column=3, pady=10)


        # return to previous page
        from title_page import TitlePage
        btn_home = tk.Button(
            master=self,
            text="return",
            bg="light grey",
            fg="navy",
            font=BTNS,
            width=10,
            command=lambda: controller.show_frame(TitlePage)
        )
        btn_home.grid(row=4, column=0, columnspan=4)

    # uses controller to display desired details
    def show_details(self, title):
        details = ""
        # if statement to check which url to send
        if title == "Heater Blowing Cold Air?\nHere's Why and What to Do About It":
            self.url = heater
            details = self.web_scraping()
        elif title == "Car AC Not Working? Weak airflow?\nTop 8 Things to Check":
            self.url = ac
            details = self.web_scraping()
        elif title == "Car Leaking Oil? Possible Causes\nand What to Do About It":
            self.url = oil_leak
            details = self.web_scraping()
        elif title == "What To Do If Your Ignition\nKey Won’t Turn":
            self.url = key_stuck
            details = self.web_scraping()
        elif title == "Car Engine Overheating:\nWhy It’s Happening and How to Fix It":
            self.url = engine_hot
            details = self.web_scraping()
        elif title == "Rough Idle Causes and How to Fix Them":
            self.url = rough_idle
            details = self.web_scraping()
        elif title == "What Fluid Is Leaking From Your Car?\nA Color-Coded Guide":
            self.url = liquid_leak
            details = self.web_scraping()
        elif title == "Soft, Spongy Brakes and What to Do":
            self.url = spongy_brake
            details = self.web_scraping()
        elif title == "Why is My Car Pulling to the Left or Right?":
            self.url = car_pulling
            details = self.web_scraping()
        elif title == "Why Is Your Vehicle Shaking?\nSymptoms, Causes and Solutions":
            self.url = car_shaking
            details = self.web_scraping()
        elif title == "Jumpstart Not Working?\nHere Are The Possible Reasons":
            self.url = jumpstart
            details = self.web_scraping()
        elif title == "How to Fix Stalling and Other Issues\nAfter Replacing the Battery":
            self.url = after_battery_replace
            details = self.web_scraping()

        
        from details_page import DetailsPage
        self.controller.show_frame(DetailsPage, title, details)



# ----------individual symptom details---------- #
    #-------generic web scraping-------#
    def web_scraping(self):
        page = requests.get(self.url)

        soup = BeautifulSoup(page.content, "html.parser")
        mb4_content = soup.find(class_="mb4")

        details = []

        if mb4_content:
            # extract h2 and p tags
            for tag in mb4_content.find_all(['h2', 'p', 'li']):
                if tag.name == 'h2':
                    details.append("*h2 "+tag.text.strip())
                elif tag.name == 'p':
                    details.append("*p "+tag.text.strip())
                elif tag.name == 'li':
                    details.append("*li "+tag.text.strip())

        return details


# -----------URLS--------- #
heater = "https://repairpal.com/symptoms/car-heater-not-working"
ac = "https://repairpal.com/symptoms/car-ac-not-working"
oil_leak = "https://repairpal.com/symptoms/car-oil-leaking"
key_stuck = "https://repairpal.com/symptoms/car-key-wont-turn"
"""---"""
engine_hot = "https://repairpal.com/symptoms/car-engine-overheating-why-it-s-happening-and-how-to-fix-it"
rough_idle = "https://repairpal.com/symptoms/car-rough-idle"
liquid_leak = "https://repairpal.com/symptoms/car-fluid-leaks-what-to-do"
spongy_brake = "https://repairpal.com/symptoms/soft-spongy-brakes-what-to-do"
"""---"""
car_pulling = "https://repairpal.com/symptoms/car-pulling-left-right"
car_shaking = "https://repairpal.com/symptoms/car-shaking-reasons"
jumpstart = "https://repairpal.com/symptoms/car-battery-wont-jumpstart"
after_battery_replace = "https://repairpal.com/symptoms/engine-stalling-after-battery-replacement"





# break_pads ="https://repairpal.com/estimator/estimate-results"


brkn_heater = ("A vehicle's heating system is also part of its cooling system. "
"The coolant is circulated through the engine in which it absorbs heat, "
"is sent to the radiator where it dissipates. This heated coolant can be expelled through the dashboard "
"if the heater is turned on."

"""\n\nSome reasons your heating system isn't working could include:
     * the cooling system
     * the heater core
     * the heater valves
     * the blower fan"""

"\n\n> Cooling system issues"
"\n     ->coolant level: if low, not enough warmed coolant may be passed to the heater core preventing "
"it from producing adequate heat."
        
"\n\n     solution: a fix would be to top up the coolant. If the levels are low due to a leak, it would "
"be best to ")

brkn_ac = """this is where the info for a broken ac would go"""

brk_pads = ("Worn brake pads can result in a loud squeaking or grinding noise while driving, especially"
"at low speeds. Replacing your brake pads early may prevent the brake rotors from being worn or damaged beyond repair.\n\n"
"The brake rotors should be inspected when the pads are replaced and depending on their condition and/or manufacturers "
"recommendations, they may require resurfacing or replacement."
"\nIt is recommended to brake gently for the first 40 to 50 miles when driving on new pads. This will allow them to adjust to the rotors and help prevent squeaking.\n\n"
"While it's a safe practice to use rotors worn or machined to the manufacturer's minimum specification, brake pedal "
"pulsation is more likely to occur with thinner rotors. If your vehicle is prone to brake pedal pulsation issues, "
"you may be better off replacing worn rotors instead of having them machined.")