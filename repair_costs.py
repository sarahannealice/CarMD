import tkinter as tk
import requests
from bs4 import BeautifulSoup

def repairs(root, frame):
    frame.pack_forget()
    root.title("Heater Repair Costs")
    root.configure(bg="light sea green")

    frm_heater = tk.Frame(
        master=root,
        padx=10,
        pady=10,
    )
    frm_heater.pack()

    lbl_title = tk.Label(
        master=frm_heater,
        text="How a heating system works")
    lbl_title.grid(row=0, column=0, columnspan=4)
    
    lbl_problem = tk.Label(
        master=frm_heater,
        text=""
    )
    lbl_problem.grid(row=1, column=0, columnspan=2)

    lbl_costs = tk.Label(
        master=frm_heater,
        text=""
    )
    lbl_costs.grid(row=1, column=2, columnspan=2)

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

        txt_problem += f"{problem}\n"
        txt_cost += f"{cost}\n"

        print(problem)
        print(cost)
        print()

    lbl_problem.config(text=txt_problem)
    lbl_costs.config(text=txt_cost)
