user_choice = 'Y'
execution_count = 0

print("--- Loop Controller (Enter 'Y' to continue) ---")

while user_choice.upper() == 'Y':
    execution_count += 1
    
    print(f"Loop executed {execution_count} time(s).")
    
    # Prompt user for input and convert to uppercase for robust checking
    user_choice = input("Do you want to continue the loop? (Y/N): ").strip().upper()

print("\n--- Loop Terminated ---")
print(f"The loop was executed a total of {execution_count} time(s).")