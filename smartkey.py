import tkinter as tk

from resources.button_panel import ButtonPanel
from resources.smartdatabase import SmartKeyDatabase


class App:
    def __init__(
        self,
    ):
        self.root = tk.Tk()
        self.root.title("SmartKey")
        self.root.minsize(750, 600)

        # DATABASE

        smart_key_db = SmartKeyDatabase()
        smart_key_db.create_table()

        try:
            smart_key_db.add_admin_user()
        except Exception:
            error_label = tk.Label(
                self.root,
                text="Dogodila se greska sa databazom".upper(),
                fg="red",
                font=("System", 20),
            )
            error_label.pack()
        else:
            # BUTTONS PANEL
            self.buttons_panel = tk.LabelFrame(self.root, text="Buttons Panel")

            self.button_frame = ButtonPanel(self.buttons_panel, self.root)
            self.button_frame.frame.pack(fill="both", expand=True)

            self.buttons_panel.pack(expand=True, fill="x", side="top")


if __name__ == "__main__":
    app = App()
    app.root.mainloop()
