import tkinter as tk


root = tk.Tk()
root.title("GUI Pack Example")
root.geometry("400x200")


labelA = tk.Label(
    root,
    text="A",
    bg="red",
    fg="white",
    bd=5,
    relief="raised"
)
labelA.pack(side="top", fill="x")


labelB = tk.Label(
    root,
    text="B",
    bg="yellow",
    bd=5,
    relief="groove"
)
labelB.pack(side="bottom", anchor="sw")


labelC = tk.Label(
    root,
    text="C",
    bg="blue",
    fg="white",
    bd=5,
    relief="groove"
)
labelC.pack(side="left", anchor="w")


labelD = tk.Label(
    root,
    text="D",
    bg="white",
    bd=5,
    relief="ridge"
)
labelD.pack(side="right", anchor="e")


root.mainloop()