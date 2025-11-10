import random
import sys

# --- Constants ---
NUM_QUESTIONS = 10
MAX_SCORE = NUM_QUESTIONS * 10
DIFFICULTY_LEVELS = {
    1: {"name": "Easy", "min": 0, "max": 9},       # Single digit
    2: {"name": "Moderate", "min": 10, "max": 99},  # Double digit
    3: {"name": "Advanced", "min": 1000, "max": 9999} # Four digit
}
SCORE_FIRST_ATTEMPT = 10
SCORE_SECOND_ATTEMPT = 5

# --- Core Functions ---

def displayMenu():
    """
    Displays the difficulty level menu and validates user input.
    Returns:
        int: The validated difficulty level choice (1, 2, or 3).
    """
    print("\n--- DIFFICULTY LEVEL ---")
    for key, val in DIFFICULTY_LEVELS.items():
        print(f" {key}. {val['name']}")
    print("------------------------")
    
    while True:
        try:
            choice = int(input("Select your difficulty (1, 2, or 3): "))
            if choice in DIFFICULTY_LEVELS:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def randomInt(min_val: int, max_val: int) -> int:
    """
    Generates a random integer within a specified range.
    Args:
        min_val (int): The minimum value (inclusive).
        max_val (int): The maximum value (inclusive).
    Returns:
        int: A random integer.
    """
    return random.randint(min_val, max_val)

def decideOperation() -> str:
    """
    Randomly decides between addition (+) or subtraction (-).
    Returns:
        str: The operator ('+' or '-').
    """
    return random.choice(['+', '-'])

def displayProblem(num1: int, num2: int, operation: str) -> tuple[int, int]:
    """
    Displays the question to the user and accepts their answer.
    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operation (str): The arithmetic operator.
    Returns:
        tuple[int, int]: (user_answer, correct_answer)
    """
    
    # Calculate the correct answer
    if operation == '+':
        correct_answer = num1 + num2
    else: # operation == '-'
        correct_answer = num1 - num2
        
    problem_str = f"\nWhat is {num1} {operation} {num2} = "
    
    while True:
        try:
            user_input = input(problem_str)
            user_answer = int(user_input)
            return user_answer, correct_answer
        except ValueError:
            print("Invalid input. Please enter an integer.")

def isCorrect(user_answer: int, correct_answer: int) -> bool:
    """
    Checks if the user's answer is correct and outputs a message.
    Args:
        user_answer (int): The answer provided by the user.
        correct_answer (int): The actual correct answer.
    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    if user_answer == correct_answer:
        print("🎉 Correct!")
        return True
    else:
        print("❌ Incorrect. Try again!")
        return False

def displayResults(score: int):
    """
    Outputs the user's final score and ranks them.
    Args:
        score (int): The user's final score.
    """
    percentage = (score / MAX_SCORE) * 100
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"
        
    print("\n" + "="*30)
    print("--- QUIZ RESULTS ---")
    print(f"Your final score is: {score} / {MAX_SCORE} ({percentage:.0f}%)")
    print(f"Your rank is: {grade}")
    print("="*30)

# --- Main Game Loop ---

def playQuiz():
    """
    The main function to run a single instance of the maths quiz.
    """
    # 1. Get Difficulty Level
    level_choice = displayMenu()
    difficulty = DIFFICULTY_LEVELS[level_choice]
    print(f"\nStarting {difficulty['name']} quiz with {NUM_QUESTIONS} questions...")
    
    min_val = difficulty['min']
    max_val = difficulty['max']
    current_score = 0
    
    # 2. Loop for 10 questions
    for i in range(1, NUM_QUESTIONS + 1):
        print(f"\n--- Question {i} of {NUM_QUESTIONS} ---")
        
        # Generate random numbers and operation
        num1 = randomInt(min_val, max_val)
        num2 = randomInt(min_val, max_val)
        op = decideOperation()
        
        # Ensure positive results for subtraction at 'Easy' level for simplicity
        # (Though not strictly required by the prompt, it improves game flow for beginners)
        if level_choice == 1 and op == '-' and num1 < num2:
            num1, num2 = num2, num1 # Swap to ensure non-negative result
            
        # First attempt
        user_ans, correct_ans = displayProblem(num1, num2, op)
        
        if isCorrect(user_ans, correct_ans):
            current_score += SCORE_FIRST_ATTEMPT
            print(f"Score awarded: {SCORE_FIRST_ATTEMPT} points.")
            continue # Move to the next question
        
        # Second attempt (only if the first was wrong)
        print("\nSecond attempt:")
        user_ans, _ = displayProblem(num1, num2, op) # Reuse the correct_ans
        
        if isCorrect(user_ans, correct_ans):
            current_score += SCORE_SECOND_ATTEMPT
            print(f"Score awarded: {SCORE_SECOND_ATTEMPT} points.")
        else:
            print(f"The correct answer was {correct_ans}.")
            print("No points awarded for this question.")
            
    # 3. Display Results
    displayResults(current_score)


# --- Program Entry Point ---

def main():
    """
    Handles the overall flow and 'play again' loop.
    """
    print("--- Welcome to the Maths Quiz! ---")
    
    play_again = 'y'
    while play_again.lower() == 'y':
        playQuiz()
        
        while True:
            try:
                play_again = input("\nWould you like to play again? (y/n): ").lower()
                if play_again in ['y', 'n']:
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            except Exception:
                # Handle unexpected input gracefully
                print("Invalid input.")
                
    print("\nThank you for playing! Goodbye.")
    sys.exit()

if __name__ == "__main__":
    main()