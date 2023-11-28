import tkinter as tk
from bs4 import BeautifulSoup
import requests

from frames import Frame

class RepairCost(Frame):
    def __init__(self, root, frame, title, colour):
        super().__init__(root, frame)
        self.window_title = title
        self.colour = colour

    def repairs_setup(self):
        self.frame.pack_forget()
        self.root.title(self.window_title)
        self.root.configure(bg=self.colour)

        frm = tk.Frame(
            master=self.root,
            padx=10,
            pady=10
        )
        frm.pack()
        
        # titles
        lbl_ptitle = tk.Label(
            master=frm,
            text=""
        )
        lbl_ptitle.grid(row=1, column=0, columnspan=2)

        lbl_ctitle = tk.Label(
            master=frm,
            text=""
        )
        lbl_ctitle.grid(row=1, column=2, columnspan=2)

        # details
        lbl_problem = tk.Label(
            master=frm,
            text=""
        )
        lbl_problem.grid(row=2, column=0, columnspan=2)

        lbl_costs = tk.Label(
            master=frm,
            text=""
        )
        lbl_costs.grid(row=2, column=2, columnspan=2)

    #-------web scraping-------#
        url = "https://vehiclechef.com/how-much-does-it-cost-to-fix-a-car-heater/"
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
                lbl_ptitle.config(text=problem, font='bold')
                lbl_ctitle.config(text=cost, font='bold')
            else:
                txt_problem += f"{problem}\n"
                txt_cost += f"{cost}\n"

            print(problem)
            print(cost)
            print()
            
        lbl_problem.config(text=txt_problem)
        lbl_costs.config(text=txt_cost)