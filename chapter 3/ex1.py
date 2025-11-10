import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeting App")
root.geometry("400x250")
root.resizable(False, False)

def update_greeting():
    name = name_entry.get().strip()
    color = color_var.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!", fg=color)
    else:
        greeting_label.config(text="Please enter your name.", fg="black")

input_frame = tk.Frame(root, bg="#e3f2fd", bd=5, relief="ridge")
input_frame.pack(fill="x", padx=10, pady=10)

tk.Label(input_frame, text="Greeting App", fg="blue", bg="#e3f2fd", font=("Helvetica", 14, "bold")).pack(pady=5)

tk.Label(input_frame, text="Enter your name:", bg="#e3f2fd").pack()
name_entry = tk.Entry(input_frame, width=30)
name_entry.pack(pady=5)

tk.Label(input_frame, text="Select a color:", bg="#e3f2fd").pack()
color_var = tk.StringVar(value="black")
color_menu = ttk.Combobox(input_frame, textvariable=color_var, values=["red", "green", "blue", "purple", "orange"], state="readonly")
color_menu.pack(pady=5)

tk.Button(input_frame, text="Update Greeting", bg="#1a1a40", fg="white", command=update_greeting).pack(pady=10)

display_frame = tk.Frame(root, bg="#f5f5f5", bd=5, relief="ridge")
display_frame.pack(expand=True, fill="both", padx=10, pady=5)

greeting_label = tk.Label(display_frame, text="", bg="#f5f5f5", font=("Helvetica", 14))
greeting_label.pack(expand=True)

root.mainloop()