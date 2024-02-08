from tkinter import messagebox
import pyodbc
from src.mechanisms.ping_mechanism import check_ping


# Algorithm to test connection:
def test_azure_sql_connection(self):
    server = self.server_entry.get()
    database = self.database_entry.get()
    username = self.username_entry.get()
    password = self.password_entry.get()
    driver = self.selected_driver.get()

    ping_value = check_ping(server)

    if not all([server, database, username, password]):
        messagebox.showerror("Error!", "Please fill in all the fields to proceed!")
        return None

    elif driver == "Select ODBC Driver":
        messagebox.showerror("Error!", "Please select a driver!")
        return None

    connection_string = (
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};PWD={password};")

    connection = None

    try:
        connection = pyodbc.connect(connection_string)
        messagebox.showinfo("Success!",
                            f"Connected to Azure SQL Database:\nServer: {server}\nDatabase: {database}\nPing Time: {ping_value}ms")

    except pyodbc.Error as e:
        messagebox.showerror("Error!", f"Connection Error: {e}")

    finally:
        if connection:
            connection.close()
