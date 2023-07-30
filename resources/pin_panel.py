import tkinter as tk
from tkinter.messagebox import askyesno
import sqlite3

from resources.admin_panel import AdminPanel
from resources.smartdatabase import SmartKeyDatabase


class PinPanel:
    def __init__(self, main_frame, root):
        self.main_frame = main_frame
        self.root = root
        self.smart_key_database = SmartKeyDatabase()

        # PIN PANEL
        self.counter = 0
        self.PIN: str = ""
        self.label_pin = tk.StringVar()
        self.label_pin.set("")

        # LEFT FRAME
        self.left_frame = tk.Frame(self.main_frame, pady=5)

        self.create_buttons()

        self.left_frame.pack(expand=True, fill="y", pady=20, side="left")
        self.left_frame.rowconfigure("all", minsize=2, pad=10, weight=1)
        self.left_frame.columnconfigure("all", minsize=2, pad=10, weight=1)

        # RIGHT FRAME
        self.right_frame = tk.Frame(self.main_frame, padx=25, pady=25)
        self.status_label = tk.Label(
            self.main_frame, pady=15, text="Status i poruke", font=("System", 22)
        )
        self.status_text = tk.Label(
            self.right_frame,
            textvariable=self.label_pin,
            font=("System", 18),
        )
        self.welcome_label = tk.Label(self.right_frame, text='', font=('System', 18))

        self.status_label.pack(padx=22)
        self.status_text.pack()
        self.welcome_label.pack()

        self.button_frame = tk.Frame(self.main_frame, pady=25)

        self.b_confirm = tk.Button(
            self.button_frame, text="Potvrdi", command=lambda: self.confirm()
        )
        self.b_new_entry = tk.Button(
            self.button_frame, text="Novi unos", command=self.new_entry
        )

        self.b_confirm.grid(column=0, row=0, sticky="w")
        self.b_new_entry.grid(column=1, row=0, sticky="e")

        self.button_frame.pack(side="bottom")
        self.button_frame.columnconfigure("all", pad=25, weight=1)

        self.right_frame.pack(expand=True, fill="both", ipadx=80, pady=25, side="right")
        self.right_frame.rowconfigure("all", minsize=5, pad=5, weight=1)
        self.right_frame.columnconfigure("all", minsize=5, pad=5, weight=1)

    def open_admin_panel(self):
        # ADMIN PANEL
        answer = askyesno(
            title="Potvrda",
            message="Da li ste sigurni da zelite pokrenuti administraciju sustava?",
        )

        if answer:
            self.admin_panel = tk.LabelFrame(self.root, text="Admin Panel")
            self.bottom_frame = AdminPanel(self.admin_panel)
            self.bottom_frame.main_frame.pack(fill="both", expand=True)
            self.admin_panel.pack(expand=True, fill="both", side="top")
        else:
            self.label_pin.set("")
            self.PIN = ""

    def create_buttons(self):
        e_btn_1 = tk.Button(self.left_frame, height=2, width=2)
        e_btn_2 = tk.Button(self.left_frame, height=2, width=2)
        e_btn_3 = tk.Button(self.left_frame, height=2, width=2)
        e_btn_4 = tk.Button(self.left_frame, height=2, width=2)
        e_btn_5 = tk.Button(self.left_frame, height=2, width=2)

        b1 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="1",
            command=lambda text="1": self.show_message(text),
        )
        b2 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="2",
            command=lambda text="2": self.show_message(text),
        )
        b3 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="3",
            command=lambda text="3": self.show_message(text),
        )
        b4 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="4",
            command=lambda text="4": self.show_message(text),
        )
        b5 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="5",
            command=lambda text="5": self.show_message(text),
        )
        b6 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="6",
            command=lambda text="6": self.show_message(text),
        )
        b7 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="7",
            command=lambda text="7": self.show_message(text),
        )
        b8 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="8",
            command=lambda text="8": self.show_message(text),
        )
        b9 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="9",
            command=lambda text="9": self.show_message(text),
        )
        b0 = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="0",
            command=lambda text="0": self.show_message(text),
        )

        c_btn = tk.Button(
            self.left_frame,
            height=2,
            width=2,
            text="C",
            command=lambda text="C": self.show_message(text),
        )

        e_btn_1.grid(column=0, row=0)
        e_btn_2.grid(column=1, row=0)
        e_btn_3.grid(column=2, row=0)
        e_btn_4.grid(column=3, row=0)
        e_btn_5.grid(column=0, row=4)

        b1.grid(column=0, row=1)
        b2.grid(column=1, row=1)
        b3.grid(column=2, row=1)
        b4.grid(column=0, row=2)
        b5.grid(column=1, row=2)
        b6.grid(column=2, row=2)
        b7.grid(column=0, row=3)
        b8.grid(column=1, row=3)
        b9.grid(column=2, row=3)
        b0.grid(column=1, row=4)

        c_btn.grid(column=2, row=4)

    def confirm(self):
        if self.PIN == "1234":
            self.open_admin_panel()
        else:
            self.smart_key_database.login_user(self.PIN, self.welcome_label)
    def new_entry(self):
        try:
            self.label_pin.set("")
            self.status_text = ''
            self.counter = 0
            self.PIN = ""
            self.welcome_label.config(text='')
            self.admin_panel.forget()
        except AttributeError as err:
            print(err)

    def show_message(self, text):
        self.PIN += text
        self.counter += 1
        self.label_pin.set(self.PIN)

        if text == "C":
            self.label_pin.set("")
            self.counter = 0
            self.PIN = ""
