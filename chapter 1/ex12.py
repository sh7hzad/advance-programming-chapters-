import math

def area_square():
    side = float(input("Enter the length of the side of the square: "))
    area = side ** 2
    print(f"The area of the square is {area:.2f}")

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is {area:.2f}")

def area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:.2f}")

def main():
    print("Choose an option:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        area_square()
    elif choice == "2":
        area_circle()
    elif choice == "3":
        area_triangle()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

main()
