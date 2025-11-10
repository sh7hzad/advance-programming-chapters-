def get_int_input(prompt):
    while True:
        try:
            value_input = input(prompt)
            value = int(value_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number (integer).")

print("--- Largest Number Finder ---")

num1 = get_int_input("Enter the first number: ")
num2 = get_int_input("Enter the second number: ")
num3 = get_int_input("Enter the third number: ")

largest = num1 

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

print("\n--- Result ---")
print(f"Numbers entered: {num1}, {num2}, {num3}")
print(f"The largest number is: {largest}")