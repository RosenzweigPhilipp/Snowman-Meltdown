import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    
    # Show guessed letters if any
    if guessed_letters:
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print("\n")

def is_word_complete(secret_word, guessed_letters):
    """Check if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def play_game():
    """Main game loop for Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # Maximum mistakes before game over

    print("Welcome to Snowman Meltdown!")
    print("Save the snowman by guessing the secret word!")
    print(f"You have {max_mistakes} wrong guesses before the snowman melts completely!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    
    # Main game loop
    while mistakes < max_mistakes and not is_word_complete(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Get user input
        guess = input("Guess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter!")
            continue
        
        # Add guess to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"Great guess! '{guess}' is in the word!")
        else:
            mistakes += 1
            print(f"Sorry, '{guess}' is not in the word.")
            if mistakes < max_mistakes:
                print(f"You have {max_mistakes - mistakes} wrong guesses left.")
        
        print()  # Add spacing
    
    # Display final game state
    display_game_state(mistakes, secret_word, guessed_letters)
    
    # Check win/lose condition and display appropriate message
    if is_word_complete(secret_word, guessed_letters):
        print("🎉 Congratulations! You saved the snowman!")
        print(f"The word was '{secret_word}' and you guessed it correctly!")
    else:
        print("❄️ Oh no! The snowman has melted completely!")
        print(f"The word was '{secret_word}'. Better luck next time!")