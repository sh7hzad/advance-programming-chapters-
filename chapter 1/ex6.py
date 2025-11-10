print("--- Exercise 6: FizzBuzz Generator (1 to 100) ---")

for number in range(1, 101):
    output = ""
    
    
    if number % 3 == 0:
        output += "Fizz"
    
    
    if number % 5 == 0:
        output += "Buzz"
        
    
        print(output)
    else:
        print(number)