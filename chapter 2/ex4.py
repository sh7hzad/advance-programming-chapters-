import tkinter as tk
from tkinter import ttk, messagebox


root = tk.Tk()
root.title("Student Management System")
root.geometry("400x600")
root.config(bg="#f5f5f5")
root.resizable(False, False)


header_frame = tk.Frame(root, bg="#1a1a40", height=80)
header_frame.pack(fill="x")


lbl_bsu = tk.Label(header_frame, text="BATH SPA\nUNIVERSITY", bg="#1a1a40", fg="white", font=("Helvetica", 10, "bold"))
lbl_bsu.pack(side="left", padx=20, pady=10)

lbl_rak = tk.Label(header_frame, text="RAK\nCAMPUS", bg="#1a1a40", fg="white", font=("Helvetica", 10, "bold"))
lbl_rak.pack(side="left", padx=30)


title = tk.Label(root, text="Student Management System", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#1a1a40")
title.pack(pady=(15, 0))

subtitle = tk.Label(root, text="New Student Registration", font=("Helvetica", 10, "bold"), bg="#f5f5f5")
subtitle.pack(pady=(0, 10))


form = tk.Frame(root, bg="#f5f5f5")
form.pack(padx=20, pady=10, fill="x")


labels = ["Student Name", "Mobile Number", "Email Id", "Home Address", "Gender"]
entries = {}

for i, label in enumerate(labels[:-1]):  
    tk.Label(form, text=label, bg="#f5f5f5").grid(row=i, column=0, sticky="w", pady=4)
    ent = tk.Entry(form, width=30, bg="#e6e6e6")
    ent.grid(row=i, column=1, pady=4)
    entries[label] = ent


tk.Label(form, text="Gender", bg="#f5f5f5").grid(row=4, column=0, sticky="w", pady=4)
gender_var = tk.StringVar()
gender_menu = ttk.Combobox(form, textvariable=gender_var, values=["Male", "Female", "Other"], state="readonly", width=27)
gender_menu.grid(row=4, column=1, pady=4)


tk.Label(form, text="Course Enrolled", bg="#f5f5f5").grid(row=5, column=0, sticky="w", pady=(10, 2))
course_var = tk.StringVar()
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
for i, course in enumerate(courses):
    tk.Radiobutton(form, text=course, variable=course_var, value=course, bg="#f5f5f5").grid(row=6+i, column=0, columnspan=2, sticky="w")


tk.Label(form, text="Languages known", bg="#f5f5f5").grid(row=10, column=0, sticky="w", pady=(10, 2))
lang_vars = {"English": tk.IntVar(), "Tagalog": tk.IntVar(), "Hindi/Urdu": tk.IntVar()}
row = 11
tk.Checkbutton(form, text="English", variable=lang_vars["English"], bg="#f5f5f5").grid(row=row, column=0, sticky="w")
tk.Checkbutton(form, text="Tagalog", variable=lang_vars["Tagalog"], bg="#f5f5f5").grid(row=row, column=1, sticky="w")
tk.Checkbutton(form, text="Hindi/Urdu", variable=lang_vars["Hindi/Urdu"], bg="#f5f5f5").grid(row=row+1, column=0, sticky="w")


tk.Label(form, text="Rate your English communication skills", bg="#f5f5f5").grid(row=row+2, column=0, columnspan=2, sticky="w", pady=(10, 2))
scale = tk.Scale(form, from_=0, to=10, orient="horizontal", bg="#f5f5f5", highlightthickness=0, troughcolor="#e6e6e6")
scale.grid(row=row+3, column=0, columnspan=2, sticky="ew")


def submit():
    name = entries["Student Name"].get()
    if not name:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return
    messagebox.showinfo("Success", f"Student '{name}' registered successfully!")

def clear():
    for ent in entries.values():
        ent.delete(0, tk.END)
    gender_var.set("")
    course_var.set("")
    for v in lang_vars.values():
        v.set(0)
    scale.set(0)

btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=15)

btn_submit = tk.Button(btn_frame, text="Submit", width=12, bg="#1a1a40", fg="white", command=submit)
btn_submit.pack(side="left", padx=10)

btn_clear = tk.Button(btn_frame, text="Clear", width=12, bg="#1a1a40", fg="white", command=clear)
btn_clear.pack(side="left", padx=10)

root.mainloop()