import sqlite3
import tkinter as tk
from tkinter import messagebox


class SmartKeyDatabase:
    def __init__(self):
        self.database = "smartkey.db"
        self.admin_user = ("admin", "1234", "Admin", "active", "admin")

        self.create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            role TEXT NOT NULL
            )
            """

        self.select_table_query_login = """
            SELECT * FROM users WHERE username=? AND password=?
            """

        self.select_table_query = """
            SELECT name FROM users WHERE role != 'Admin' AND status == 'Active'
            """
            
        self.select_user_table_query = """
            SELECT * From users WHERE name = ?
            """

        self.insert_into_table_query = """
            INSERT INTO users (username, password, name, status, role)
            VALUES (?, ?, ?, ?, ?)
            """

        self.update_query = """
            UPDATE users
            SET password=?, name=?, status=?, role=?
            WHERE username=?
            """

        self.delete_table_query = """
            DELETE FROM users WHERE username=?
            """

        self.login_user_query = """
            SELECT name, status 
            FROM users 
            WHERE password = ?
        """

    def create_table(self):
        sc = sqlite3.connect(self.database)
        cursor = sc.cursor()
        cursor.execute(self.create_table_query)
        sc.commit()
        cursor.close()
        if sc:
            sc.close()

    def add_admin_user(self):
        sc = sqlite3.connect(self.database)
        cursor = sc.cursor()
        cursor.execute(
            self.select_table_query_login, (self.admin_user[0], self.admin_user[1])
        )
        records = cursor.fetchone()
        cursor.close()
        if records is None:
            cursor = sc.cursor()
            cursor.execute(self.insert_into_table_query, self.admin_user)
            sc.commit()
            cursor.close()
        sc.close()

    def update_user(self, password, name, status, role, username):
        sc = sqlite3.connect(self.database)
        cursor = sc.cursor()
        cursor.execute(
            self.update_query, (password, name, status, role, username)
        )
        sc.commit()
        cursor.close()
        if sc:
            sc.close()

    def add_user(self, username, password, name, status, role):
        if username or password or name or status or role == '':
            messagebox.showerror('SmartKey', 'Nemozete spremiti prazna polja.\nMolimo Vas da ih popunite.')
        else:
            answer = messagebox.askyesno(
                title="SmartKey",
                message="Da li ste sigurni da zelite kreirati ili ažurirati korisnika?",
            )
            
            if answer:
                try:
                    new_user = (username, password, name, status, role)
                    sc = sqlite3.connect(self.database)
                    cursor = sc.cursor()
                    cursor.execute(self.insert_into_table_query, new_user)
                    sc.commit()
                    cursor.close()
                    messagebox.showinfo('SmartKey', f'Korisnik {username} je uspjesno dodan u bazu podataka!')
                
                except sqlite3.IntegrityError:
                    self.update_user(password, name, status, role, username)
                
                except sqlite3.Error as err:
                    messagebox.showerror("SmartKey", err)
                
                finally:
                    if sc:
                        sc.close()

    def update_user(self, password, name, status, role, username):
        try:
            update_data = (password, name, status, role, username)
            sc = sqlite3.connect(self.database)
            cursor = sc.cursor()
            cursor.execute(self.update_query, update_data)
            sc.commit()
            cursor.close()
        except sqlite3.Error as err:
            messagebox.showerror("SmartKey", err)
        else:
            messagebox.showinfo("SmartKey", f'Korisnik {username} je uspjesno azuriran.')

    def show_users(self, root, username_entry, password_entry, name_entry, status_entry, role_entry):
        sc = sqlite3.connect(self.database)
        cursor = sc.cursor()
        cursor.execute(self.select_table_query)
        records = cursor.fetchall()
        cursor.close()

        for record in records:
            name = record[0]
            self.button = tk.Button(root, text=name, command=lambda name=name: self.populate_information(name, username_entry, password_entry, name_entry, status_entry, role_entry))
            self.button.pack(pady=2)
            
        if sc:
            sc.close()
            

    def login_user(self, password, label):
        sc = sqlite3.connect(self.database)
        cursor = sc.cursor()
        cursor.execute(self.login_user_query, (password,))
        user_data = cursor.fetchone()
        name = user_data[0]
        status = user_data[1]
        
        if status == 'Active':
            label.configure(text=f'Dobrodosao {name}!')
        elif status == 'Disabled':
            label.configure(text='Nemate pristup za ulazak!')
        elif status == 'Vacation':
            label.configure(text=f'Na godisnjem odmoru ste!')
            
            
            

    def populate_information(self, selected_username, username_entry, password_entry, name_entry, status_entry, role_entry):
        try:
            sc = sqlite3.connect(self.database)
            cursor = sc.cursor()
            cursor.execute(self.select_user_table_query, (selected_username,))
            user_data = cursor.fetchone()
            cursor.close()
            
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            status_entry.delete(0, tk.END)
            role_entry.delete(0, tk.END)

            username_entry.insert(0, user_data[1])
            password_entry.insert(0, user_data[2])
            name_entry.insert(0, user_data[3])
            status_entry.insert(0, user_data[4])
            role_entry.insert(0, user_data[5])
        except:
            messagebox.showerror("SmartKey", f"Korisnike '{selected_username}' nije pronaden!")
        else:
            if sc:
                sc.close()

    def delete_user(self, username):    
        sc = sqlite3.connect(self.database)
        cursor = sc.cursor()
        cursor.execute(self.delete_table_query, (username,))
        sc.commit()
        cursor.close()
        if sc:
            sc.close()
    
