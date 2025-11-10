import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x300")
root.config(bg="#f5f5f5")
root.resizable(False, False)

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        elif op == "%":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 % num2
        lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    lbl_result.config(text="Result:")

title = tk.Label(root, text="Basic Arithmetic Calculator", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#1a1a40")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

tk.Label(frame, text="Enter first number:", bg="#f5f5f5").grid(row=0, column=0, sticky="w", pady=5)
entry1 = tk.Entry(frame, width=25, bg="#e6e6e6")
entry1.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Enter second number:", bg="#f5f5f5").grid(row=1, column=0, sticky="w", pady=5)
entry2 = tk.Entry(frame, width=25, bg="#e6e6e6")
entry2.grid(row=1, column=1, pady=5)

btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

operations = [("+", "Add"), ("-", "Subtract"), ("*", "Multiply"), ("/", "Divide"), ("%", "Modulo")]
for symbol, name in operations:
    tk.Button(btn_frame, text=name, width=10, bg="#1a1a40", fg="white", command=lambda s=symbol: calculate(s)).pack(side="left", padx=5)

lbl_result = tk.Label(root, text="Result:", font=("Helvetica", 12, "bold"), bg="#f5f5f5", fg="#1a1a40")
lbl_result.pack(pady=15)

tk.Button(root, text="Clear", width=15, bg="#1a1a40", fg="white", command=clear_fields).pack()

root.mainloop()