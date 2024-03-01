# Created on Monday, October 16, 2023:
# @author: RYANCANTRELL321
# Organization: Pandora Dynamics
# @email: pandoradynamics@gmail.com
# Program Name: PANDORA DATABASE CONNECTION TESTER (AZURE SQL)


from src.gui_initialization import *
from src.mechanisms.button_placements import checkbox
from src.mechanisms.instance_lock_mechanism import acquire_lock, release_lock

# instance lock
lock_fd = acquire_lock()


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
        configure_bg_image(self.master, "img/bg.jpg", 500, 500)
        create_widgets(self)
        checkbox(self, 390, 180, 25, 15)


release_lock(lock_fd)
