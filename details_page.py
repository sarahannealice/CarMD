import tkinter as tk
import requests
from bs4 import BeautifulSoup

from fonts import *

class DetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="light goldenrod yellow")
        self.url = ""


    #-------grid weights-------#
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.lbl_title = tk.Label(
            master=self,
            text="",
            font=TITLE,
            bg="light goldenrod yellow"
        )
        self.lbl_title.grid(row=0, column=0, columnspan=2)

        self.txt_details = tk.Text(
            master=self,
            wrap=tk.WORD,
            width=80,
            height=13,
            bd=0,
            bg="light yellow2",
            padx=5
        )
        self.txt_details.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

        scrollb = tk.Scrollbar(
            master=self,
            command=self.txt_details.yview
        )
        scrollb.grid(row=1, column=2, sticky='nsew')
        self.txt_details['yscrollcommand'] = scrollb.set

        print(self.lbl_title.cget("text"))

        # displays repair costs
        self.btn_costs = tk.Button(
            master=self,
            text="repair costs",
            font=BTNS,
            width=12,
            command=lambda: self.repair_cost(self.lbl_title.cget("text"))
        )
        self.btn_costs.grid(row=3, column=0)
        
        # return to previous page
        self.page = ""
        self.btn_return = tk.Button(
            master=self,
            text="return",
            bg="light grey",
            fg="black",
            font=BTNS,
            width=12,
            command=lambda: controller.show_frame(self.page)
        )
        self.btn_return.grid(row=3, column=1)

# -----------updates title and content of page-------------- #

    def update_content(self, title, details):
        self.lbl_title.config(text=title)   

        from lights_page import LightsPage
        from symptoms_page import SymptomsPage

        # checks if displaying dash light, removes repair cost button if so
        if (title == "Check Engine Light On" or title == "What to Do When Your\nBrake Warning Light Is On" or 
            title == "What Your Car's Battery Warning Light Means" or title == "Why Your Car's ABS Light Is On,\nand What It Means" or 
            title == "Why Is My Engine\nTemperature Warning Light On?" or title == "What Your Oil Warning Lights Mean,\nand What to Do"):
            
            self.btn_costs.grid_forget()
            self.btn_return.grid(row=3, column=0, columnspan=2)
            self.page = LightsPage
            
        else:
            # updates return btn
            self.page = SymptomsPage
            self.btn_costs.grid(row=3, column=0)
            self.btn_return.grid(row=3, column=1)


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
        tl_win.configure(bg="dark sea green2")
        tl_win.wm_title(title)

        self.lbl_cost = tk.Label(
            master=tl_win,
            text="Cost to Replace",
            bg="dark sea green2",
            font=TITLE
        )
        self.lbl_cost.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        lbl_title = tk.Label(
            master=tl_win,
            text="Information Unavailable",
            bg="dark sea green2",
            font=SUBTITLE
        )
        lbl_title.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        # self.lbl_breakdown = tk.Label(
        #     master=tl_win,
        #     text="Cost Breakdown",
        #     font=SUBTITLE
        # )
        # self.lbl_breakdown.grid(row=2, column=0, sticky="ew")
    
    
# -----------costs--------- #




# -----------URLS--------- #
heater = "https://vehiclechef.com/how-much-does-it-cost-to-fix-a-car-heater/"
break_pads ="https://repairpal.com/estimator/estimate-results"
        
    
#-------generic web scraping with selenium-------#
'''
* @brief practiced webscraping with beautiful soup but later found selenia was needed in interact with the webpage
* desired website (repairpal.com/estimator) prevents this and i resulted to inputting the information manually
* the resources used are:
* https://scrapfly.io/blog/web-scraping-with-selenium-and-python/#navigating-waiting-and-retrieving-in-selenium
* https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python
*
* america common cars:
* https://www.copilotsearch.com/posts/most-common-cars-in-america/#:~:text=What%20are%20the%20Most%20Common%20Cars%20in%20America%3F,Percentage%20of%20cars%20on%20the%20road%3A%202.48%25%20
*
* canada common cars:
* https://motorillustrated.com/most-popular-cars-in-canada-in-2022/109387/
*
*
* @params
* assumptions -- chicago, illinois (60601 zip)
* make -- honda
* year -- 2020
* model -- accord
* to mention -- 2nd most common car is the ford f-series (in america) and 1st most common (in canada)
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