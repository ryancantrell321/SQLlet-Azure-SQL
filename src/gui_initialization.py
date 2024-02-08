import os
from PIL import ImageTk, Image
from src.mechanisms.azure_tester import test_azure_sql_connection
from src.mechanisms.entry_field_mechanisms import *
from src.mechanisms.button_placements import *
import sys


# UI:
def create_widgets(self):
    create_entry(self, "Server:", 35, 175, 25)
    create_entry(self, "Database:", 35, 175, 75)
    create_entry(self, "Username:",35, 175, 125)
    pwd_entry(self, "Password:", 35, 175, 175)
    create_driver_dropdown(self, 35, 175, 225)

    # buttons:
    test_button(self, 75, 275, 160, test_azure_sql_connection)

    reset_button(self, 270, 275, 160, reset_button_click)

    help_button(self, 75, 325, 160, help_button_click)
    license_button(self, 270, 325, 160, license_button_click)
    install_button(self, 75, 375, 160, install_driver_button_click)
    about_button(self, 270, 375, 160, about_button_click)
    exit_button(self, 175, 425, 160, exit_button_click)

    footer(self, 0, 475, 500)


def configure_icon(master, icon_path):
    ico = getattr(sys, '_MEIPASS', '.') + f"/{icon_path}"
    image = Image.open(ico)
    icon = ImageTk.PhotoImage(image)
    master.tk.call('wm', 'iconphoto', master._w, icon)


def configure_bg_image(master, bg_image_path, bw, bh):

    script_dir = os.path.dirname(__file__)
    bg_image_path = os.path.join(script_dir, bg_image_path)

    bg = Image.open(bg_image_path)
    bg = bg.resize((bw, bh))
    bg_image = ImageTk.PhotoImage(bg)
    bg_label = ctk.CTkLabel(master=master, image=bg_image, text="")
    bg_label.pack()
