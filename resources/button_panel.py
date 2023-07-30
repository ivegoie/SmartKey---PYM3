import tkinter as tk
from tkinter import messagebox

from resources.pin_panel import PinPanel


class ButtonPanel:
    def __init__(self, button_panel, root):
        self.button_panel = button_panel
        self.root = root

        self.frame = tk.Frame(self.button_panel, padx=25, pady=5)

        self.ring_button = tk.Button(
            self.frame,
            text="POZVONI",
            width=15,
            height=2,
            padx=20,
            pady=5,
            command=self.ring_door,
        )

        self.unlock_button = tk.Button(
            self.frame,
            text="OTKLJUCAJ",
            width=15,
            height=2,
            padx=20,
            pady=5,
            command=self.unlock_door,
        )

        self.frame.pack(side="top")
        self.ring_button.grid(column=0, padx=20, pady=20, row=0, sticky="w")
        self.unlock_button.grid(column=1, padx=20, pady=20, row=0, sticky="e")

        # GRID CONFIGURATION
        self.frame.columnconfigure("all", minsize=10, pad=25, weight=1)

    def ring_door(self):
        messagebox.showinfo(
            "SmartKey", "Pozvonili ste, netko ce uskoro otvoriti vrata."
        )

    def unlock_door(self):
        # PIN PANEL
        self.pin_panel = tk.LabelFrame(self.root, text="Pin Panel")
        self.pin_frame = PinPanel(self.pin_panel, self.root)
        self.pin_frame.main_frame.pack(fill="both", expand=True)
        self.pin_panel.pack(expand=True, fill="both", side="top")
        self.unlock_button["state"] = "disabled"
