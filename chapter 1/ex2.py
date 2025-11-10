def get_int_input(prompt):
    
    while True: 
        try:
            
            value_input = input(prompt)
            
            value = int(value_input)

            return value
        except ValueError:

            print("❌ Oops! That wasn't a whole number. Please enter a valid integer.")

print("--- 🔢 Arithmetic Calculator ---")
print("This program will perform five basic math operations on two numbers you provide.")


number1 = get_int_input("Enter the first integer (Number 1): ")
number2 = get_int_input("Enter the second integer (Number 2): ")




sum_result = number1 + number2

diff_result = number1 - number2

product_result = number1 * number2


if number2 == 0:
    
    quotient_result = "ERROR: Cannot divide by zero (Undefined)"
    remainder_result = "ERROR: Cannot divide by zero (Undefined)"
else:
   
    quotient_result = number1 / number2
    
    remainder_result = number1 % number2



print("\n--- ✅ Calculation Results ---")
print(f"Input 1: {number1}")
print(f"Input 2: {number2}")
print("---------------------------------------")
print(f"Sum (+):       {number1} + {number2} = {sum_result}")
print(f"Difference (-): {number1} - {number2} = {diff_result}")
print(f"Product (x):   {number1} * {number2} = {product_result}")
print(f"Quotient (/):  {number1} / {number2} = {quotient_result}")
print(f"Remainder (%): {number1} % {number2} = {remainder_result} (The leftover after division)")