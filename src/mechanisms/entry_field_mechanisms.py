import customtkinter as ctk
from src.miscellaneous.fonts import *


def create_entry(self, label_text, xl, x_position, y_position):
    ctk.CTkLabel(self.master, text=label_text, fg_color="black",
                 bg_color="black", font=font2, padx=20).place(x=xl, y=y_position)
    entry = ctk.CTkEntry(self.master, width=200)

    entry.configure(fg_color="#b3b3b3", bg_color="black", text_color="black")
    entry.place(x=x_position, y=y_position)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

    setattr(self, f"{label_text.lower().replace(':', '')}_entry", entry)


def pwd_entry(self, label_text, xl, x_position, y_position, show_var=None):
    ctk.CTkLabel(self.master, text=label_text, fg_color="black", bg_color="black",
                 font=font2, padx=20).place(x=xl, y=y_position)

    pwd = ctk.CTkEntry(self.master, width=200, show="*" if show_var is None or not show_var.get() else "")
    pwd.configure(fg_color="#b3b3b3", bg_color="black", text_color="black")
    pwd.place(x=x_position, y=y_position)

    pwd.bind("<FocusIn>", on_focus_in)
    pwd.bind("<FocusOut>", on_focus_out)

    setattr(self, f"{label_text.lower().replace(':', '')}_entry", pwd)


# focus mechanism:
def on_focus_in(event):
    entry = event.widget
    entry.config(fg="black", bg="white")


def on_focus_out(event):
    entry = event.widget
    entry.config(fg="black", bg="#b3b3b3")


def toggle_password_visibility(self):
    show_password = self.show_password_var.get()
    pwd_entry = self.password_entry
    pwd_entry.configure(show="" if show_password else "*")
