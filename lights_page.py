import tkinter as tk
import requests
from bs4 import BeautifulSoup

from fonts import *

class LightsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="thistle")


    #-------grid weights-------#
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)


        label = tk.Label(
            master=self,
            text="Dashboard Warning Lights",
            fg="dark slate blue",
            bg="thistle",
            font=TITLE,
            )
        label.grid(row=0, column=0, columnspan=3)
        
    #-------load icones-------#
    # https://stackoverflow.com/a/3366046
        self.check = tk.PhotoImage(file='./icons/car_small.png') 
        self.brakes = tk.PhotoImage(file='./icons/parking_small.png') 
        self.battery = tk.PhotoImage(file='./icons/charging_sys_small.png') 
        self.abs = tk.PhotoImage(file='./icons/abs_small.png') 
        self.tires = tk.PhotoImage(file='./icons/tire_pressure_small.png') 
        self.oil = tk.PhotoImage(file='./icons/low_oil_small.png')



    #-------buttons-------#
        #---row 1---#
        btn_check = tk.Button(
            master=self,
            image=self.check,
            fg="dark slate blue",
            bg="lavender",
            height=150,
            width=150,
            font=BTNS,
            command=lambda:self.show_details("Check Engine Light On")
        )
        btn_check.grid(row=1, column=0, pady=10)

        btn_brks = tk.Button(
            master=self,
            image=self.brakes,
            fg="dark slate blue",
            bg="lavender",
            font=BTNS,
            height=150,
            width=150,
            command=lambda:self.show_details("What to Do When Your\nBrake Warning Light Is On")
        )
        btn_brks.grid(row=1, column=1, pady=10)
        
        btn_battery = tk.Button(
            master=self,
            image=self.battery,
            fg="dark slate blue",
            bg="lavender",
            font=BTNS,
            height=150,
            width=150,
            command=lambda:self.show_details("What Your Car's Battery Warning Light Means")
        )
        btn_battery.grid(row=1, column=2, pady=10)
        
        #---row 2---#
        btn_abs = tk.Button(
            master=self,
            image=self.abs,
            fg="dark slate blue",
            bg="lavender",
            font=BTNS,
            height=150,
            width=150,
            command=lambda:self.show_details("Why Your Car's ABS Light Is On,\nand What It Means")
        )
        btn_abs.grid(row=2, column=0, pady=10)

        btn_tires = tk.Button(
            master=self,
            image=self.tires,
            fg="dark slate blue",
            bg="lavender",
            font=BTNS,
            height=150,
            width=150,
            command=lambda:self.show_details("Tire Pressure Warning Light:\nWhat It Means, and What to Do About It")
        )
        btn_tires.grid(row=2, column=1, pady=10)
        
        btn_oil = tk.Button(
            master=self,
            image=self.oil,
            fg="dark slate blue",
            bg="lavender",
            font=BTNS,
            height=150,
            width=150,
            command=lambda:self.show_details("What Your Oil Warning Lights Mean,\nand What to Do")
        )
        btn_oil.grid(row=2, column=2, pady=10)


        # return to previous page
        from title_page import TitlePage
        btn_home = tk.Button(
            master=self,
            text="return",
            fg="dark slate blue",
            bg="light grey",
            font=BTNS,
            width=10,
            command=lambda: controller.show_frame(TitlePage)
        )
        btn_home.grid(row=4, column=0, columnspan=4)


# uses controller to display desired details
    def show_details(self, title):
        details = ""
        # if statement to check which url to send
        if title == "Check Engine Light On":
            self.url = check
            details = self.web_scraping()
        elif title == "What to Do When Your\nBrake Warning Light Is On":
            self.url = brakes
            details = self.web_scraping()
        elif title == "What Your Car's Battery Warning Light Means":
            self.url = battery
            details = self.web_scraping()
        elif title == "Why Your Car's ABS Light Is On,\nand What It Means":
            self.url = abs
            details = self.web_scraping()
        elif title == "Tire Pressure Warning Light:\nWhat It Means, and What to Do About It":
            self.url = tires
            details = self.web_scraping()
        elif title == "What Your Oil Warning Lights Mean,\nand What to Do":
            self.url = oil
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
    
# ----------URLS---------- #
check = "https://repairpal.com/symptoms/check-engine-light"
brakes = "https://repairpal.com/brake-hydraulic-system-red-warning-light"
battery = "https://repairpal.com/symptoms/charging-system-warning-light"
"""---"""
abs = "https://repairpal.com/symptoms/abs-warning-light"
tires = "https://repairpal.com/tire-pressure-warning-light"
oil = "https://repairpal.com/low-oil-pressure-warning-light"



# ----------icon resource---------- #
#<a href="https://www.flaticon.com/free-icons/automotive" title="automotive icons">Automotive icons created by LAFS - Flaticon</a>