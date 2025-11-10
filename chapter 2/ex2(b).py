import tkinter as tk


root = tk.Tk()
root.title("GUI Pack Example")
root.geometry("400x200")


left_frame = tk.Frame(root, bd=5, relief="groove", bg="white")
right_frame = tk.Frame(root, bd=5, relief="groove", bg="white")

left_frame.pack(side="left", expand=True, fill="both")
right_frame.pack(side="right", expand=True, fill="both")


labelA = tk.Label(left_frame, text="A", bg="#1a1a40", fg="white")  # dark
labelB = tk.Label(left_frame, text="B", bg="white", fg="black")    # white

labelA.pack(side="top", expand=True, fill="both")
labelB.pack(side="bottom", expand=True, fill="both")


labelC = tk.Label(right_frame, text="C", bg="white", fg="black")   # white
labelD = tk.Label(right_frame, text="D", bg="#1a1a40", fg="white") # dark

labelC.pack(side="top", expand=True, fill="both")
labelD.pack(side="bottom", expand=True, fill="both")


root.mainloop()