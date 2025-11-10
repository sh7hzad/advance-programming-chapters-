import tkinter as tk
from tkinter import ttk

def draw_shape():
    canvas.delete("all")
    shape = shape_var.get()

    if shape == "Oval":
        canvas.create_oval(100, 50, 300, 200, fill="skyblue", outline="black")
    elif shape == "Rectangle":
        canvas.create_rectangle(100, 50, 300, 200, fill="lightgreen", outline="black")
    elif shape == "Square":
        canvas.create_rectangle(150, 50, 250, 150, fill="orange", outline="black")
    elif shape == "Triangle":
        canvas.create_polygon(200, 50, 100, 200, 300, 200, fill="pink", outline="black")

root = tk.Tk()
root.title("Shape Drawer")
root.geometry("450x400")
root.config(bg="#f2f2f2")

tk.Label(root, text="Select a Shape to Draw", font=("Arial", 14, "bold"), bg="#f2f2f2").pack(pady=10)

shape_var = tk.StringVar(value="Oval")
shapes = ["Oval", "Rectangle", "Square", "Triangle"]

for s in shapes:
    ttk.Radiobutton(root, text=s, variable=shape_var, value=s).pack(anchor="w", padx=100)

tk.Button(root, text="Draw Shape", command=draw_shape, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=15)

canvas = tk.Canvas(root, width=400, height=220, bg="white", relief="ridge", bd=2)
canvas.pack(pady=10)

root.mainloop()
