import random
import sys

# --- Constants ---
# The prompt phrase to start the joke telling
JOKE_PROMPT = "alexa tell me a joke" 

def load_jokes(joke_content: str) -> list[tuple[str, str]]:
    """
    Parses the raw joke content into a list of (setup, punchline) tuples.
    Args:
        joke_content (str): The raw text content of the jokes file.
    Returns:
        list[tuple[str, str]]: A list where each element is a (setup, punchline).
    """
    jokes = []
    # Split the content by line to process each joke
    lines = joke_content.strip().split('\n')
    for line in lines:
        # Check if the line contains the expected separator '?'
        if '?' in line:
            # Use rsplit to split only on the first '?' from the right, 
            # ensuring all question marks in the setup are preserved.
            parts = line.rsplit('?', 1) 
            if len(parts) == 2:
                setup = parts[0].strip() + '?'
                punchline = parts[1].strip()
                jokes.append((setup, punchline))
    return jokes

def tell_random_joke(jokes: list[tuple[str, str]]):
    """
    Selects a random joke, presents the setup, waits for input, 
    and then reveals the punchline.
    Args:
        jokes (list[tuple[str, str]]): The list of (setup, punchline) tuples.
    """
    if not jokes:
        print("I don't have any jokes right now! My joke database is empty. 😔")
        return
    
    # Randomly select one joke
    setup, punchline = random.choice(jokes)
    
    print(f"\n🗣️ {setup}")
    input("Press ENTER for the punchline...")
    print(f"🎤 {punchline}")

def main(joke_data: str):
    """
    The main program loop that handles the user prompt.
    Args:
        joke_data (str): The raw text content of the jokes file.
    """
    jokes_list = load_jokes(joke_data)
    
    if not jokes_list:
        print("Error: Could not load jokes. Exiting.")
        sys.exit()

    print("🤖 Joke Bot is ready. Say 'Alexa tell me a Joke' to begin, or 'quit' to exit.")
    
    while True:
        try:
            # Get user input and convert to lowercase for easy matching
            user_input = input("\nYou say: ").strip().lower()

            if user_input == 'quit' or user_input == 'exit':
                print("👋 Goodbye! Hope you got a laugh.")
                break
            
            if user_input == JOKE_PROMPT:
                tell_random_joke(jokes_list)
            else:
                print("🤔 I didn't catch that. Please say 'Alexa tell me a Joke' or 'quit'.")
                
        except EOFError:
            # Handle Ctrl+D or end-of-file signal
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            # Handle other unexpected errors gracefully
            print(f"An error occurred: {e}")
            break


JOKES_TXT_CONTENT = """
Why did the zombies get divorced?Their marriage was dead!
Why did the lion go to therapy?He found out his wife was a cheetah!
Did you hear about the couple of bed bugs?They got married in the spring!
Which one of your kids will never grow up and move out?Your husband!
Why is being married worse than going to work?At least at work, you might get a new boss!
How are boys similar to wine?They take years and years and years to mature!
Why is a good doctor able to stay calm?He has a lot of patients!
What the best way to criticize your boss?Very quietly, so she can’t hear you!
Why did the marketer dump her boyfriend?Lack of engagement!
What’s a pirate’s favorite meeting style?A webinarrrrr!
What does Nemo have in common with my dad?Neither can be found!
What did the cow say to the leather chair?“Hi Mom!”
When does a joke become a dad joke?When it leaves and never comes back!
Who makes the most money off of Father’s Day?Therapists!
Why don’t cannibals eat clowns?Because they taste funny!
Why don’t graveyards ever get overcrowded?Because people are dying to get in!
Why don’t orphans get their driver’s license?Because they don’t know where home is!
What’s the best part about dead batteries?Free of charge!
Why did the old man fall into the well?Because he couldn’t see that well!
Why don’t we play hide and seek in cemeteries?Because good luck finding someone who hasn’t already won!
Why do blind people hate skydiving?It scares the heck out of their dog!
What’s red and bad for your teeth?A brick!
"""

if __name__ == "__main__":
    main(JOKES_TXT_CONTENT)