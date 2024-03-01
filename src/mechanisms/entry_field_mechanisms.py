from cryptography.fernet import Fernet
import base64

code = b"""

import customtkinter as ctk
import tkinter as tk
from src.miscellaneous.fonts import *
from src.mechanisms.context_menu import make_menu, show_menu


def entry_var_getter():
    entry_var = tk.StringVar()
    return entry_var


def create_entry(self, label_text, xl, x_position, y_position, max_length=50):

    ctk.CTkLabel(self.master, text=label_text, fg_color="black",
                 bg_color="black", font=font2, padx=20).place(x=xl, y=y_position)

    entry = ctk.CTkEntry(self.master, width=200, textvariable=entry_var_getter())
    vcmd = (self.master.register(on_validate), "%S", "%P", max_length)

    make_menu(entry)
    entry.bind("<Button-3>", lambda event: show_menu(event, entry))

    entry.configure(fg_color="#b3b3b3", bg_color="black", text_color="black", validate="key", validatecommand=vcmd)
    entry.place(x=x_position, y=y_position)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

    setattr(self, f"{label_text.lower().replace(':', '')}_entry", entry)


def pwd_entry(self, label_text, xl, x_position, y_position, show_var=None, max_length=30):

    ctk.CTkLabel(self.master, text=label_text, fg_color="black", bg_color="black",
                 font=font2, padx=20).place(x=xl, y=y_position)

    pwd = ctk.CTkEntry(self.master, textvariable=entry_var_getter(), width=200, show="*" if show_var is None or not show_var.get() else "")
    vcmd = (self.master.register(on_validate), "%S", "%P", max_length)

    pwd.configure(fg_color="#b3b3b3", bg_color="black", text_color="black", validate="key", validatecommand=vcmd)
    pwd.place(x=x_position, y=y_position)

    make_menu(pwd)
    pwd.bind("<Button-3>", lambda event: show_menu(event, pwd))

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


def on_validate(char, entry_value, max_length):
    return len(str(entry_value)) <= int(max_length)


"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)
