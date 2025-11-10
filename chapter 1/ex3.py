def get_positive_float_input(prompt):
    while True:
        try:
            value_input = input(prompt)
            value = float(value_input)
            
            if value <= 0:
                print("Side length must be a positive number (greater than 0).")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

print("--- Triangle Checker ---")

side_a = get_positive_float_input("Enter the length of Side A: ")
side_b = get_positive_float_input("Enter the length of Side B: ")
side_c = get_positive_float_input("Enter the length of Side C: ")

is_triangle = (side_a + side_b > side_c) and \
              (side_a + side_c > side_b) and \
              (side_b + side_c > side_a)

print("\n--- Result ---")
print(f"Side A: {side_a}, Side B: {side_b}, Side C: {side_c}")

if is_triangle:
    print("These lengths CAN form a triangle.")
else:
    print("These lengths CANNOT form a triangle.")