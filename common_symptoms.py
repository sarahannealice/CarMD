import tkinter as tk

def symptoms_layout(root, frame):
    frame.pack_forget()
    root.title("Common Symptoms")
    root.configure(bg="light blue")

    frm_symptoms = tk.Frame(
        master=root,
        padx=10,
        pady=10,
    )
    frm_symptoms.pack()

    lbl_symptopms = tk.Label(
        master=frm_symptoms,
        text="Common Symptoms",
        fg="navy",
        font=("Arial", 18)
    )
    lbl_symptopms.grid(row=0, column=0, columnspan=3)

    btn_heater = tk.Button(
        master=frm_symptoms,
        text="Heater not working",
        fg="white",
        bg="navy",
        font=14,
        command=heater_broken
    )

    btn_ac = tk.Button(
        master=frm_symptoms,
        text="A/C not working",
        fg="white",
        bg="navy",
        font=14
    )
    
    btn_oil_leak = tk.Button(
        master=frm_symptoms,
        text="Car leaking oil",
        fg="white",
        bg="navy",
        font=14
    )
    btn_heater.grid(row=1, column=0, padx=5, pady=5)
    btn_ac.grid(row=1, column=1, padx=5, pady=5)
    btn_oil_leak.grid(row=1, column=2, padx=5, pady=5)

    btn_menu = tk.Button(
        master=frm_symptoms,
        text="return",
        bg="light grey",
        fg="black",
        command=lambda: menu(root, frame,frm_symptoms)
    )
    btn_menu.grid(row=2, column=0, columnspan=2)



def menu(root, frame, frm_symptoms):
    frm_symptoms.pack_forget()
    frame.pack(side=tk.TOP)
    root.title("CarMD")
    root.configure(bg="pink")


def heater_broken():
    win = tk.Toplevel()
    win.geometry("500x300")
    win.configure(bg="light yellow")
    win.wm_title("Heater not Working")

    lbl_title = tk.Label(
        master=win,
        text="How a heating system works")
    lbl_title.grid(row=0, column=0, columnspan=4)

    # insert canvas with scrollbar here for info
    lbl_info = tk.Label(
        master=win,
        text="A vehicle's heating system is also part of its cooling system.\n"
    + "The coolant is circulated through the engine in which it absorb heat,\n "
    + "is sent to the radiator where it dissipates. This heated coolant can be expelled through the dashboard\n "
    + "if the heater is turned on."
    )
    lbl_info.grid(row=1, column=1, columnspan=2)

    # insert beautiful soup web scraping here for cost to repair
    # this is a test