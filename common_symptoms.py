import tkinter as tk
from symptoms import *

# ----------layout of symptoms---------- #
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
        command=lambda:heater_broken(root, frm_symptoms, "How a heating system works", brkn_heater)
    )

    btn_ac = tk.Button(
        master=frm_symptoms,
        text="A/C not working",
        fg="white",
        bg="navy",
        font=14,
        command=lambda:ac_broken(root, frm_symptoms, "How a heating system works", brkn_ac)
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
        command=lambda: menu(root, frame, frm_symptoms)
    )
    btn_menu.grid(row=2, column=0, columnspan=2)


def menu(root, frame, frm_symptoms):
    frm_symptoms.pack_forget()
    frame.pack(side=tk.TOP)
    root.title("CarMD")
    root.configure(bg="pink")


# ----------individual symptom details---------- #
brkn_heater = """A vehicle's heating system is also part of its cooling system.
The coolant is circulated through the engine in which it absorb heat,
is sent to the radiator where it dissipates. This heated coolant can be expelled through the dashboard
if the heater is turned on.

Some reasons your heating system isn't working could include:
* the cooling system
* the heater core
* the heater valves
* the blower fan

> Cooling system issues
    ->coolant level: if low, not enough warmed coolant may be passed to the heater core preventing
        it from producing adequate heat.
        
      solution: a fix would be to top up the coolant. If the levels are low due to a leak, it would
        be best to """

brkn_ac = """this is where the info for a broken ac would go"""