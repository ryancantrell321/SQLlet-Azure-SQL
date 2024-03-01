from cryptography.fernet import Fernet
import base64

code = b"""


import tkinter as tk
import customtkinter as ctk
from src.miscellaneous.fonts import font3


def make_menu(w):
    menu = tk.Menu(w, tearoff=0, relief="sunken", font=font3)
    commands = ["Cut", "Copy", "Paste", "Select all"]
    for command in commands:
        menu.add_command(label=command, command=lambda c=command, w=w: handle_menu_command(c, w))
    return menu


def cut(widget):
    widget.event_generate("<Control-x>")


def copy(widget):
    widget.event_generate("<Control-c>")


def paste(widget):
    widget.event_generate("<Control-v>")


def select_all(widget):
    widget.select_range(0, tk.END)


def handle_menu_command(command, widget):
    if command == "Cut":
        cut(widget)
    elif command == "Copy":
        copy(widget)
    elif command == "Paste":
        paste(widget)
    elif command == "Select all":
        select_all(widget)


def show_menu(event, widget):
    menu = make_menu(widget)
    menu.post(event.x_root, event.y_root)
    widget.focus_set()
    
"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)

