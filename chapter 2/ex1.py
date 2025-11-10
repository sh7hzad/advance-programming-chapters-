import tkinter as tk
from tkinter import font


root = tk.Tk()
root.title("Welcome Program")


root.geometry("400x200")


root.resizable(False, False)


root.config(bg="#cdeac0")  


welcome_label = tk.Label(
    root,
    text="Welcome to Python GUI!",
    font=("Helvetica", 20, "bold"),  
    bg="#cdeac0",  
    fg="#2b2d42"   
)
welcome_label.pack(expand=True)


root.mainloop()