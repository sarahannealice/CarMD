import tkinter as tk

def symptoms(root, frame):
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
        text=("Common Symptoms"),
        fg="navy",
        font=("Arial", 18),
    )
    lbl_symptopms.grid(row=0, column=0, columnspan=2)

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
    frame.pack()
    root.title("CarMD")
    root.configure(bg="pink")