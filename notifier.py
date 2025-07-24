import tkinter as tk
from tkinter import messagebox

def show_update_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    result = messagebox.askyesno("Update Available", "A new update is available. Do you want to update now?")
    if result:
        print("User chose to update.")
    else:
        print("User skipped the update.")
    root.destroy()

