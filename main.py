#CarMD main page
import tkinter as tk
import tkinter.ttk as ttk
import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("CarMD")
# root.geometry("600x400")
root.resizable(width=False, height=False)
root.configure(bg="pink")

frame = tk.Frame(
    master=root,
    padx=10,
    pady=10
)
frame.pack()

label = tk.Label(
    master=frame,
    text="CarMD by Sarah",
    fg="navy",
    bg="pink",
    font=("Ariel", 18),
    width=10,
    height=3,
    padx=20
    )
label.grid(row=0, column=0, columnspan=2)

btn_left = tk.Button(
    master=frame,
    text="common symptoms",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    font=16
)
btn_left.grid(row=1, column=0)

btn_right = tk.Button(
    master=frame,
    text="warning lights",
    width=25,
    height=5,
    bg="orange",
    fg="black",
    font=16
)
btn_right.grid(row=1, column=1)

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print("\n")


# print(results.prettify())

root.mainloop()