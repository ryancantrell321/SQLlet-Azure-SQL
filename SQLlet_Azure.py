"""
Created on TUE Dec 19 2023:
@author: RYANCANTRELL321
Organization: Pandora Dynamics
@email: pandoradynamics@gmail.com
Program Name: PANDORA DATABASE CONNECTION TESTER (AZURE SQL)

"""
from src.gui_initialization import *
from src.mechanisms.button_placements import checkbox
from splash_screen import SplashScreen
import tkinter as tk


# Configuration:
class AzureSQLConnectionTester:
    def __init__(self, master):
        self.drivers = None
        self.password_entry = None
        self.username_entry = None
        self.database_entry = None
        self.server_entry = None
        self.driver_entry = None
        self.selected_driver = tk.StringVar()
        self.master = master
        master.title("SQLlet Inspection Suite: Azure SQL ")
        master.geometry("500x500+400+100")
        master.resizable(False, False)

        configure_icon(self.master, "src/img/ico/icon.ico")
        configure_bg_image(self.master, "img/bg_abstract.jpg", 500, 500)
        create_widgets(self)
        checkbox(self, 390, 180, 25, 15)


if __name__ == "__main__":
    splash_root = tk.Tk()
    splash = SplashScreen(splash_root)
    splash_root.mainloop()
    splash_root.update()

    window = tk.Tk()
    app = AzureSQLConnectionTester(window)
    window.mainloop()
