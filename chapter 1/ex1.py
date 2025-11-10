user_name = input("Please enter your name: ")
formatted_name = user_name.title()


while True:
    try:
        user_age_input = input("Please enter your age: ")
        user_age = int(user_age_input)
        break
    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")


name_length = len(formatted_name.replace(" ", "")) 


age_next_year = user_age + 1


print("\n--- User Details ---")
print(f"Name: {formatted_name}")
print(f"Age: {user_age}")
print(f"Name Length: {name_length}")
print(f"Age Next Year: {age_next_year}")
