import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Login Page")
root.geometry("350x200")
root.resizable(False, False)
root.config(bg="#e6e6e6")  


def login():
    user = entry_username.get()
    pwd = entry_password.get()
    if user == "admin" and pwd == "1234":
        messagebox.showinfo("Login Success", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


title = tk.Label(
    root,
    text="User Login",
    font=("Helvetica", 16, "bold"),
    bg="#e6e6e6",
    fg="#1a1a40"
)
title.grid(row=0, column=0, columnspan=2, pady=10)


lbl_username = tk.Label(root, text="Username:", bg="#e6e6e6")
lbl_username.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(root, width=25)
entry_username.grid(row=1, column=1, padx=10, pady=5)


lbl_password = tk.Label(root, text="Password:", bg="#e6e6e6")
lbl_password.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, width=25, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)


btn_login = tk.Button(root, text="Login", width=15, bg="#1a1a40", fg="white", command=login)
btn_login.grid(row=3, column=0, columnspan=2, pady=15)


root.mainloop()