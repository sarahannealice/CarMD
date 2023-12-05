import tkinter as tk
import requests
from bs4 import BeautifulSoup

from fonts import *
from symptoms_page import *

class DetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="light goldenrod yellow")

        # if statement to check which url to send

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
            #command=lambda: controller.show_toplevel(title="Heater Repair Costs", url=heater)
            command=lambda: self.repair_cost(self.lbl_title.cget("text"), heater)
        )
        btn.grid(row=3, column=0, columnspan=2)
        
        # return to previous page
        from symptoms_page import SymptomsPage
        btn_home = tk.Button(
            master=self,
            text="return",
            bg="light grey",
            fg="black",
            command=lambda: controller.show_frame(SymptomsPage)
        )
        btn_home.grid(row=3, column=2, columnspan=2)

    # updates title and content of page
    def update_content(self, title, details):
        self.lbl_title.config(text=title)

        self.txt_details.config(state="normal")
        self.txt_details.delete("1.0", tk.END)
        self.txt_details.insert(tk.END, details)
        self.txt_details.config(state="disabled")

# -----------display repair cost as toplevel-------------- #
    # from toplevel_page import DisplayToplevel
    def repair_cost(self, title, url):
        tl_win = tk.Toplevel()
        tl_win.geometry("500x300")
        tl_win.configure(bg="light sea green")
        tl_win.wm_title(title)

        tl_win.grid_rowconfigure(1, weight=1)
        tl_win.grid_columnconfigure(0, weight=1)
        tl_win.grid_columnconfigure(1, weight=1)

        self.lbl_ptitle = tk.Label(
            master=tl_win,
            text=""
        )
        self.lbl_ptitle.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        self.lbl_ctitle = tk.Label(
            master=tl_win,
            text=""
        )
        self.lbl_ctitle.grid(row=0, column=1, sticky='ew', padx=10, pady=10)

        # details
        self.lbl_problem = tk.Label(
            master=tl_win,
            text=""
        )
        self.lbl_problem.grid(row=1, column=0)

        self.lbl_costs = tk.Label(
            master=tl_win,
            text=""
        )
        self.lbl_costs.grid(row=1, column=1)

        self.web_scraping(url)

    # popup for warning lights
    def warning_lights(self, title, img):
        placeholder = ""


    #-------web scraping-------#
    def web_scraping(self, url):
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="wp-block-table is-style-stripes")

        txt_problem = ""
        txt_cost = ""

        repairs = results.find_all("tr")
        for repair in repairs:
            td_tags = repair.find_all("td")
            problem = td_tags[0].text.strip()
            cost = td_tags[1].text.strip()

            # bolds the titles
            # https://stackoverflow.com/a/17303428
            if (problem == 'Car Heater Problem'):
                self.lbl_ptitle.config(text=problem, font='bold')
                self.lbl_ctitle.config(text=cost, font='bold')
            else:
                txt_problem += f"{problem}\n"
                txt_cost += f"{cost}\n"
            
        self.lbl_problem.config(text=txt_problem)
        self.lbl_costs.config(text=txt_cost)


    def testing(self, title, url):
    tl_win = tk.Toplevel()
    tl_win.geometry("500x300")
    tl_win.configure(bg="light sea green")
    tl_win.wm_title(title)

    tl_win.grid_rowconfigure(1, weight=1)
    tl_win.grid_columnconfigure(0, weight=1)
    tl_win.grid_columnconfigure(1, weight=1)

# -----------URLS--------- #
heater = "https://vehiclechef.com/how-much-does-it-cost-to-fix-a-car-heater/"