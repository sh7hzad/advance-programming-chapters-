from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def order_coffee():
    coffee_type = coffee_var.get()
    sugar = "with sugar" if sugar_var.get() else "no sugar"
    milk = "with milk" if milk_var.get() else "no milk"
    message = f"You ordered a {coffee_type} ({sugar}, {milk}). Enjoy your drink!"
    messagebox.showinfo("Order Confirmed", message)

root = Tk()
root.title("Coffee Vending Machine")
root.geometry("400x400")
root.config(bg="#f8f3e7")

# Load an image (replace 'coffee.png' with your own image file)
try:
    img = Image.open("coffee.jpeg")
    img = img.resize((120, 120))
    coffee_img = ImageTk.PhotoImage(img)
    img_label = Label(root, image=coffee_img, bg="#f8f3e7")
    img_label.pack(pady=10)
except:
    Label(root, text="☕", font=("Arial", 60), bg="#f8f3e7").pack(pady=10)

Label(root, text="Select your coffee type:", font=("Arial", 14), bg="#f8f3e7").pack()

coffee_var = StringVar(value="Espresso")
Radiobutton(root, text="Espresso", variable=coffee_var, value="Espresso", bg="#f8f3e7").pack()
Radiobutton(root, text="Cappuccino", variable=coffee_var, value="Cappuccino", bg="#f8f3e7").pack()
Radiobutton(root, text="Latte", variable=coffee_var, value="Latte", bg="#f8f3e7").pack()

Label(root, text="Options:", font=("Arial", 14), bg="#f8f3e7").pack(pady=5)

sugar_var = BooleanVar()
milk_var = BooleanVar()

Checkbutton(root, text="Add Sugar", variable=sugar_var, bg="#f8f3e7").pack()
Checkbutton(root, text="Add Milk", variable=milk_var, bg="#f8f3e7").pack()

Button(root, text="Place Order", command=order_coffee, bg="#d1a679", fg="white", font=("Arial", 12)).pack(pady=15)

root.mainloop()
