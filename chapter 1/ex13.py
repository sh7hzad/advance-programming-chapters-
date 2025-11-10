def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def main():
    numbers = [2, 4, 6, 8]  
    result = product_of_list(numbers)
    print(f"The product of the list items is {result}")

main()
