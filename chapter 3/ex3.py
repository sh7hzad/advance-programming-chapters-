import tkinter as tk
from tkinter import ttk, messagebox
import math

def area_circle():
    try:
        r = float(entry_radius.get())
        area = math.pi * r ** 2
        messagebox.showinfo("Result", f"Area of Circle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def area_square():
    try:
        side = float(entry_side.get())
        area = side ** 2
        messagebox.showinfo("Result", f"Area of Square: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def area_rectangle():
    try:
        width = float(entry_width.get())
        height = float(entry_height.get())
        area = width * height
        messagebox.showinfo("Result", f"Area of Rectangle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Area Calculator")
root.geometry("400x300")
root.config(bg="#f2f2f2")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", pady=10)

# -------- Circle Tab --------
tab_circle = ttk.Frame(notebook)
notebook.add(tab_circle, text="Circle")

tk.Label(tab_circle, text="Enter Radius:", font=("Arial", 12)).pack(pady=10)
entry_radius = tk.Entry(tab_circle)
entry_radius.pack()
tk.Button(tab_circle, text="Calculate Area", command=area_circle, bg="#4CAF50", fg="white").pack(pady=10)

# -------- Square Tab --------
tab_square = ttk.Frame(notebook)
notebook.add(tab_square, text="Square")

tk.Label(tab_square, text="Enter Side Length:", font=("Arial", 12)).pack(pady=10)
entry_side = tk.Entry(tab_square)
entry_side.pack()
tk.Button(tab_square, text="Calculate Area", command=area_square, bg="#4CAF50", fg="white").pack(pady=10)

# -------- Rectangle Tab --------
tab_rectangle = ttk.Frame(notebook)
notebook.add(tab_rectangle, text="Rectangle")

tk.Label(tab_rectangle, text="Enter Width:", font=("Arial", 12)).pack(pady=5)
entry_width = tk.Entry(tab_rectangle)
entry_width.pack()
tk.Label(tab_rectangle, text="Enter Height:", font=("Arial", 12)).pack(pady=5)
entry_height = tk.Entry(tab_rectangle)
entry_height.pack()
tk.Button(tab_rectangle, text="Calculate Area", command=area_rectangle, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
