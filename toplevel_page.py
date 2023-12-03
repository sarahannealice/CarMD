import tkinter as tk
import requests
from bs4 import BeautifulSoup

#*****NEEDS FIXING*****#
class DisplayToplevel(tk.Toplevel):
    def __init__(self, parent, controller):
        tk.Toplevel.__init__(self, parent)
        self.controller = controller

        self.geometry("500x300")
        self.wm_title("")
        self.configure(bg="")
        
    # popup for repair costs
    def repair_cost(self, title, url):
        self.tl_win.wm_title(title)
        self.tl_win.configure(bg="light sea green")
            
        # titles
        self.lbl_ptitle = tk.Label(
            master=self.tl_win,
            text="title"
        )
        self.lbl_ptitle.grid(row=1, column=0, columnspan=2)

        self.lbl_ctitle = tk.Label(
            master=self.tl_win,
            text=""
        )
        self.lbl_ctitle.grid(row=1, column=2, columnspan=2)

        # details
        self.lbl_problem = tk.Label(
            master=self.tl_win,
            text=""
        )
        self.lbl_problem.grid(row=2, column=0, columnspan=2)

        self.lbl_costs = tk.Label(
            master=self.tl_win,
            text=""
        )
        self.lbl_costs.grid(row=2, column=2, columnspan=2)

        self.web_scraping(url)

    # popup for warning lights
    def warning_lights(self, title, img):
        placeholder = ""


    #-------web scraping-------#
    def web_scraping(self, url):
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="wp-block-table is-style-stripes")
        print(results.prettify())

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

            print(problem)
            print(cost)
            print()
            
        self.lbl_problem.config(text=txt_problem)
        self.lbl_costs.config(text=txt_cost)