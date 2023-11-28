import tkinter as tk
import requests
from bs4 import BeautifulSoup

def repairs(root, frame, title):
    frame.pack_forget()
    root.title(title)
    root.configure(bg="light sea green")

    frm_heater = tk.Frame(
        master=root,
        padx=10,
        pady=10,
    )
    frm_heater.pack()

    heater_window = tk.Toplevel(
        
    )
    
    # titles
    lbl_ptitle = tk.Label(
        master=frm_heater,
        text=""
    )
    lbl_ptitle.grid(row=1, column=0, columnspan=2)

    lbl_ctitle = tk.Label(
        master=frm_heater,
        text=""
    )
    lbl_ctitle.grid(row=1, column=2, columnspan=2)

    # details
    lbl_problem = tk.Label(
        master=frm_heater,
        text=""
    )
    lbl_problem.grid(row=2, column=0, columnspan=2)

    lbl_costs = tk.Label(
        master=frm_heater,
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