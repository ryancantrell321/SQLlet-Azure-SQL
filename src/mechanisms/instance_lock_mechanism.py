from tkinter import messagebox
import tkinter as tk
import os
import sys
import portalocker


def acquire_lock():
    lock_file = os.path.join(os.path.dirname(sys.argv[0]), "instance_lock.sqllet")

    try:
        lock_fd = open(lock_file, 'w')
        portalocker.lock(lock_fd, portalocker.LOCK_EX | portalocker.LOCK_NB)
        return lock_fd
    except portalocker.LockException:
        tk.messagebox.showerror("Error", "Another instance is already running. Exiting.")
        print("Another instance is already running. Exiting.")
        sys.exit(1)


def release_lock(lock_fd):
    portalocker.unlock(lock_fd)
    lock_fd.close()
    os.unlink(os.path.join(os.path.dirname(sys.argv[0]), "instance_lock.sqllet"))
