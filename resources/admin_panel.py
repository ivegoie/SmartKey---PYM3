import tkinter as tk
from tkinter import messagebox

from resources.smartdatabase import SmartKeyDatabase
import sqlite3


class AdminPanel:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.smart_key_db = SmartKeyDatabase()

        welcome_label = tk.Label(
            main_frame, text="Dobrodosao admin!", font=("System", 25)
        )
        welcome_label.pack()

        # RIGHT FRAME
        right_frame = tk.Frame(main_frame)

        username_label = tk.Label(right_frame, text="Nadimak")
        self.username_entry = tk.Entry(right_frame)

        password_label = tk.Label(right_frame, text="PIN (4 broja)")
        self.password_entry = tk.Entry(right_frame)

        name_label = tk.Label(right_frame, text="Ime i prezime")
        self.name_entry = tk.Entry(right_frame, text='')

        status_label = tk.Label(right_frame, text="Status")
        self.status_entry = tk.Entry(right_frame)

        role_label = tk.Label(right_frame, text="Uloga")
        self.role_entry = tk.Entry(right_frame)

        buttons_frame = tk.Frame(right_frame)
        save_button = tk.Button(
                buttons_frame,
                text="Spremi",
                command=lambda: self.smart_key_db.add_user(
                    self.username_entry.get(),
                    self.password_entry.get(),
                    self.name_entry.get(),
                    self.status_entry.get(),
                    self.role_entry.get(),
                )
            )

        
        abort_button = tk.Button(buttons_frame, text="Odustani", command=lambda: self.reset_entries())
        delete_button = tk.Button(buttons_frame, text="Izbrisi", command=lambda: self.delete_selected_user())

        # GRID MANAGMENT

        username_label.grid(row=0, column=0, sticky="e")
        self.username_entry.grid(row=0, column=1, sticky="e")

        password_label.grid(row=1, column=0, sticky="e")
        self.password_entry.grid(row=1, column=1, sticky="e")

        name_label.grid(row=2, column=0, sticky="e")
        self.name_entry.grid(row=2, column=1, sticky="e")

        status_label.grid(row=3, column=0, sticky="e")
        self.status_entry.grid(row=3, column=1, sticky="e")

        role_label.grid(row=4, column=0, sticky="e")
        self.role_entry.grid(row=4, column=1, sticky="e")

        save_button.grid(row=0, column=0)
        abort_button.grid(row=0, column=1)
        delete_button.grid(row=0, column=2)

        buttons_frame.grid(row=5, column=0, columnspan=4, pady=25, padx=25)
        buttons_frame.columnconfigure("all", pad=15, weight=1)

        right_frame.pack(expand=True, fill="y", side="right", padx=25, pady=25)
        
        # LEFT FRAME
        left_frame = tk.Frame(main_frame)

        name_label = tk.Label(
            left_frame,
            text="Lista Korisnika sa aktivnim kljucem",
            font=("System", 16),
            pady=10,
        )
        name_label.pack()
        self.smart_key_db.show_users(left_frame, self.username_entry, self.password_entry, self.name_entry, self.status_entry, self.role_entry)
        left_frame.pack(expand=True, fill="y", side="left", padx=25, pady=25)

    def reset_entries(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END)

    def delete_selected_user(self):
        username = self.username_entry.get()
        if username == '':
            messagebox.showerror("SmartKey", "Molimo Vas da popunite sva polja!")
        else:
            answer = messagebox.askyesno(
                title="SmartKey",
                message="Da li ste sigurni da želite izbrisati korisnika?",
            )
            if answer:
                try:
                    self.smart_key_db.delete_user(username)
                except sqlite3.Error:
                    messagebox.showerror("SmartKey", "Greška u brisanju korisnika!")
                else:
                    messagebox.showinfo("SmartKey", "Korisnik je uspješno izbrisan!")

            

