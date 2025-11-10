numbers = [42, 15, 7, 99, 30, 7, 56, 18, 6, 82]
print(f"Original list: {numbers}")
print("-" * 30)

print("Outputting the list with a for loop:")
for number in numbers:
    print(number, end=" ")
print("\n" + "-" * 30)

print(f"Highest value: {max(numbers)}")
print(f"Lowest value: {min(numbers)}")
print("-" * 30)

numbers.sort()
print(f"Sorted ascending: {numbers}")
print("-" * 30)

numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}")
print("-" * 30)

numbers.append(100)
numbers.append(1)
print("Appended 100 and 1.")
print("-" * 30)

print(f"Final list: {numbers}")