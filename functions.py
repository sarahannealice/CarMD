import tkinter as tk
import requests
from bs4 import BeautifulSoup

# updates scrollbar
def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    cnv_jobs.configure(scrollregion=cnv_jobs.bbox('all'))

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# https://stackoverflow.com/a/40539365 -- scrollbar work around
cnv_jobs = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, command=cnv_jobs.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')
cnv_jobs.configure(yscrollcommand = scrollbar.set)
cnv_jobs.bind('<Configure>', on_configure)
cnv_jobs.pack()

frm_jobs = tk.Frame(cnv_jobs)
cnv_jobs.create_window((0,0), window=frm_jobs, anchor='nw')

# cnv_companies = tk.Canvas(root)
# cnv_companies.configure(scrollregion=cnv_companies.bbox('all'))
# cnv_companies.pack(side=tk.RIGHT)

job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    lbl_job_title = tk.Label(
        master=frm_jobs,
        text=title_element.text.strip(),
        fg="white",
        bg="dark grey"
    )
    # lbl_job_title.pack()
    print(title_element.text.strip())

    # lbl_company = tk.Label(
    #     master=cnv_companies,
    #     text=company_element.text.strip(),
    #     fg="black",
    #     bg="white"
    # )
    # lbl_job_title.pack()
    print(company_element.text.strip())
    print(location_element.text.strip())
    print("\n")


# print(results.prettify())