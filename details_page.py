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
        self.url = ""

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
            width=80,
            height=13,
            bd=0,
            bg="light yellow2",
            padx=5
        )
        self.txt_details.grid(row=1, column=0, columnspan=4, padx=20, pady=5)

        scrollb = tk.Scrollbar(
            master=self,
            command=self.txt_details.yview
        )
        scrollb.grid(row=1, column=4, sticky='nsew')
        self.txt_details['yscrollcommand'] = scrollb.set

        print(self.lbl_title.cget("text"))

        # displays repair costs
        btn = tk.Button(
            master=self,
            text="Repair Costs",
            font=BTNS,
            command=lambda: self.repair_cost(self.lbl_title.cget("text"))
        )
        btn.grid(row=3, column=0, columnspan=2)
        
        # return to previous page
        from symptoms_page import SymptomsPage
        btn_home = tk.Button(
            master=self,
            text="return",
            bg="light grey",
            fg="black",
            font=BTNS,
            command=lambda: controller.show_frame(SymptomsPage)
        )
        btn_home.grid(row=3, column=2, columnspan=2)

# -----------updates title and content of page-------------- #

    def update_content(self, title, details):
        self.lbl_title.config(text=title)   

        self.txt_details.config(state="normal") # enables text edit
        self.txt_details.delete("1.0", tk.END) # clears text widget
        self.txt_details.config(font=DETAILS)

        for word in details:
            start_index = self.txt_details.index(tk.END)

            # skip images
            if word.split(' ')[-2] == "Image":
                continue
            elif word.split(' ', 1)[0] == "*h2":
                text = word.split(' ', 1)[1]
                self.txt_details.tag_add('h2', start_index, self.txt_details.index(tk.END))
                self.txt_details.insert(tk.END, '\n'+text+'\n')
            elif word.split(' ', 1)[0] == "*p":
                text = word.split(' ', 1)[1]
                self.txt_details.tag_add('p', start_index, self.txt_details.index(tk.END))
                self.txt_details.insert(tk.END, text+'\n')
            elif word.split(' ', 1)[0] == "*li":
                text = word.split(' ', 1)[1]
                self.txt_details.tag_add('li', start_index, self.txt_details.index(tk.END))
                self.txt_details.insert(tk.END, '\t*'+text+'\n')

        # applying styles
        self.txt_details.tag_config('h2', font=SUBTITLE)
        self.txt_details.tag_config('p', font=DETAILS)
        self.txt_details.tag_config('li', font=DETAILS)

        self.txt_details.config(state="disabled") # disables text edit


# -----------display repair cost as toplevel-------------- #
    # from toplevel_page import DisplayToplevel
    def repair_cost(self, title):
        tl_win = tk.Toplevel()
        tl_win.geometry("500x300")
        tl_win.configure(bg="light sea green")
        tl_win.wm_title(title)

        tl_win.grid_rowconfigure(1, weight=1)
        tl_win.grid_columnconfigure(0, weight=1)
        tl_win.grid_columnconfigure(1, weight=1)

        self.lbl_title = tk.Label(
            master=tl_win,
            text="Information Unavailable",
            font=SUBTITLE
        )
        self.lbl_title.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        # self.lbl_cost = tk.Label(
        #     master=tl_win,
        #     text="Cost to Replace",
        #     font=TITLE
        # )
        # self.lbl_cost.grid(row=1, column=0, sticky='ew', padx=10, pady=10)

        # self.lbl_breakdown = tk.Label(
        #     master=tl_win,
        #     text="Cost Breakdown",
        #     font=SUBTITLE
        # )
        # self.lbl_breakdown.grid(row=2, column=0, sticky="ew")
    

# -----------URLS--------- #
heater = "https://vehiclechef.com/how-much-does-it-cost-to-fix-a-car-heater/"
break_pads ="https://repairpal.com/estimator/estimate-results"
        
    
#-------generic web scraping with selenium-------#
'''
* @brief practiced webscraping with beautiful soup but later found selenia was needed in interact with the webpage
* desired website prevents this and i resulted to inputting the information manually
* the resources used are:
* https://scrapfly.io/blog/web-scraping-with-selenium-and-python/#navigating-waiting-and-retrieving-in-selenium
* https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python
'''

# # configure webdriver
# options = Options()
# options.add_argument("headless")
# options.headless = True # hides gui
# options.add_argument('--blink-settings=imagesEnabled=false') # prevents imgs/js from loading

# driver = webdriver.Edge(options=options)
# driver.get("https://repairpal.com/estimator")

# # wait for page to load
# element = WebDriverWait(driver=driver, timeout=5).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-target=zipCode]')()
# )
# # prints webpage elements
# print(driver.page_source)