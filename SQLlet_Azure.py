import tkinter as tk
from splash_screen import SplashScreen
from config import AzureSQLConnectionTester
from src.mechanisms.instance_lock_mechanism import acquire_lock, release_lock

# instance lock
lock_fd = acquire_lock()

if __name__ == "__main__":
    splash_root = tk.Tk()
    splash = SplashScreen(splash_root)
    splash_root.mainloop()
    splash_root.update()

    window = tk.Tk()
    app = AzureSQLConnectionTester(window)
    window.mainloop()

release_lock(lock_fd)
