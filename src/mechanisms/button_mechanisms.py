from tkinter import messagebox
import tkinter as tk
import webbrowser as web
import customtkinter as ctk
from src.miscellaneous.fonts import font2
from src.miscellaneous.time import year


# Driver selector
def create_driver_dropdown(self, xl, x_position, y_position):
    ctk.CTkLabel(self.master, text="Driver:", fg_color="black",
                 bg_color="black", font=font2, padx=20).place(x=xl, y=y_position)
    self.drivers = ["Select ODBC Driver", "{ODBC Driver 17 for SQL Server}", "{ODBC Driver 18 for SQL Server}"]
    self.selected_driver.set(self.drivers[0])

    driver_dropdown = ctk.CTkComboBox(self.master, variable=self.selected_driver, values=self.drivers, width=200)
    driver_dropdown.configure(fg_color="#b3b3b3", bg_color="#333333", text_color="black", button_hover_color="white",
                              state="readonly", dropdown_fg_color="white", dropdown_text_color="black",
                              dropdown_hover_color="#0080ff")
    driver_dropdown.place(x=x_position, y=y_position)


# reset:
def reset_button_click(self):
    for entry_name in ["server_entry", "database_entry", "username_entry", "password_entry"]:
        entry = getattr(self, entry_name)
        entry.delete(0, tk.END)

        self.selected_driver.set(self.drivers[0])


# help info:
def help_button_click(self):
    text = "To use this program, fill in all the blank fields and select an appropriate ODBC driver installed in your system.\n\nUsage Guidelines:\n\n1. Server: The URL or IP of your Azure SQL Database server.\n2. Database: The name of the target database.\n3. Username: Your database username.\n4. Password: Your database password.\n5. Driver: Select the appropriate ODBC Driver installed in your       system.\n6. After this, click on 'Test Connection' to test whether or not       your connection credentials are correct.\n7. To clear the fields, click the 'RESET' button.\n8. To see the License, click the 'LICENSE' button\n9. To quit the program, click the 'EXIT' button."
    text2 = "IMPORTANT NOTES:\nThis program expects that you have a stable internet connection and already have an ODBC driver installed in your system. If not, please install the driver from the official Microsoft Website by clicking on the 'Install Driver' Button."
    text3 = "In case of a successful connection, a message box with success status will pop up.\n\nIn case of a failed or unstable connection, a message box detailing error reasons will popup."
    messagebox.showinfo("Help", f"{text}\n\n{text2}\n\n{text3}")


# Install Driver:
def install_driver_button_click(self):
    text = "Upon clicking 'Ok,' you will be redirected to the official website of Microsoft Corporation, where you can proceed to download the ODBC Driver.\n\nLink:\nhttps://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16"
    messagebox.showinfo("Install ODBC Driver", f"{text}")
    web.open("https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16")


# About:
def about_button_click(self):
    text = "Presenting the SQLlet INSPECTION SUITE: AZURE SQL, a tool designed to assist developers in verifying the correctness of their Azure SQL database credentials.\n\nIt is designed to be a streamlined and comprehensive tool crafted to assist developers in confirming the correctness of their Azure SQL database credentials, verifying its external accessibility.\n\nThis application is portable, eliminating the need for installation, and places a premium on security by abstaining from logging or storing any received or inputted information.\n\nDevelopers can employ this tool to ascertain the external accessibility of the intended database for their ongoing system development."
    mail_text = "For any issues, bugs or queries, contact us at: pandoradynamics@gmail.com"
    cp_text = f"© {year()} PANDORA DYNAMICS & RYANCANTRELL321.\nAll Rights Reserved for the source code.\n\n© {year()} SHAD0WW0RRI0R.\nAll Rights Reserved for system identity: 'SQLlet'\n\nLicensed under Creative Commons Attribution-NoDerivs 4.0 International (CC BY-ND 4.0).\n\nTo view a copy of this license, visit http://creativecommons.org/licenses/by-nd/4.0/"
    messagebox.showinfo("About", f"{text}\n\n{mail_text}\n\n{cp_text}")
    web.open("https://internal-sqllet.rf.gd/readmeazure.html")
    web.open("https://creativecommons.org/licenses/by-nd/4.0/")


# Exit:
def exit_button_click(self):
    self.master.destroy()
    exit(0)
