import tkinter as tk
from repair_costs import repairs
from repair_cost import RepairCost

# ----------broken heater---------- #
def heater_broken(root, frame, title, details):
    frame.pack_forget()
    root.title("Heater not Working")
    root.configure(bg="light yellow")

    frm_heater = tk.Frame(
        master=root,
        padx=10,
        pady=10,
    )
    frm_heater.pack()

    lbl_title = tk.Label(
        master=frm_heater,
        text=title
    )
    lbl_title.grid(row=0, column=0, columnspan=4)

    # insert canvas with scrollbar here for info
    lbl_info = tk.Label(
        master=frm_heater,
        text=details
    )
    lbl_info.grid(row=1, column=1, columnspan=2)

    btn = tk.Button(
        master=frm_heater,
        text="Repair Costs",
        #command=lambda:repairs(root, frame, "Heater Repair Costs")
        command=RepairCost(root, frame, "Heater Repair Costs", "light sea green")
    )
    btn.grid(row=0, column=1)

    # insert beautiful soup web scraping here for cost to repair

def ac_broken(root, frame, title, details):
    win_ac = tk.Toplevel()
    win_ac.geometry("500x300")
    win_ac.configure(bg="light yellow")
    win_ac.wm_title("Heater not Working")

    lbl_title = tk.Label(
        master=win_ac,
        text=title
    )
    lbl_title.grid(row=0, column=0, columnspan=4)

    # insert canvas with scrollbar here for info
    lbl_info = tk.Label(
        master=win_ac,
        text=details
    )
    lbl_info.grid(row=1, column=1, columnspan=2)

  