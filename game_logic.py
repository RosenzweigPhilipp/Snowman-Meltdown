import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""
    print_separator()
    print(STAGES[mistakes])
    
    # Build a display version of the secret word with better formatting
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "_ "
    
    print(f"📝 Word: {display_word}")
    print(f"❄️  Snowman Health: {len(STAGES) - 1 - mistakes}/{len(STAGES) - 1}")
    
    # Show guessed letters if any with better formatting
    if guessed_letters:
        correct_guesses = [letter for letter in guessed_letters if letter in secret_word]
        wrong_guesses = [letter for letter in guessed_letters if letter not in secret_word]
        
        if correct_guesses:
            print(f"✅ Correct guesses: {', '.join(sorted(correct_guesses)).upper()}")
        if wrong_guesses:
            print(f"❌ Wrong guesses: {', '.join(sorted(wrong_guesses)).upper()}")
    
    print_separator()

def is_word_complete(secret_word, guessed_letters):
    """Check if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def get_valid_guess(guessed_letters):
    """Get a valid single letter guess from the user with comprehensive validation."""
    while True:
        guess = input("🎯 Guess a letter: ").strip()
        
        # Check for empty input
        if not guess:
            print("❌ Please enter something! Don't leave it blank.")
            continue
            
        # Check for multiple characters
        if len(guess) > 1:
            print("❌ Please enter only ONE letter at a time.")
            continue
            
        # Check if it's alphabetical
        if not guess.isalpha():
            print("❌ Please enter a LETTER (a-z), not numbers or symbols.")
            continue
            
        guess = guess.lower()
        
        # Check for duplicate guess
        if guess in guessed_letters:
            print(f"❌ You already guessed '{guess.upper()}'. Try a different letter!")
            continue
            
        return guess

def print_separator():
    """Print a decorative separator for better readability."""
    print("═" * 50)

def ask_play_again():
    """Ask the user if they want to play again."""
    while True:
        choice = input("\n🔄 Would you like to play again? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def play_single_game():
    """Play a single round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # Maximum mistakes before game over

    print("\n🎮 " + "="*20 + " NEW GAME " + "="*20 + " 🎮")
    print("🎯 Save the snowman by guessing the secret word!")
    print(f"⚠️  You have {max_mistakes} wrong guesses before the snowman melts!")
    print(f"💡 The word has {len(secret_word)} letters.")
    # Uncomment for testing: print("Secret word selected: " + secret_word)
    
    # Main game loop
    while mistakes < max_mistakes and not is_word_complete(secret_word, guessed_letters):
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Get validated user input
        guess = get_valid_guess(guessed_letters)
        
        # Add guess to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"\n✨ Excellent! '{guess.upper()}' is in the word! ✨")
            if secret_word.count(guess) > 1:
                print(f"🎉 Bonus! '{guess.upper()}' appears {secret_word.count(guess)} times!")
        else:
            mistakes += 1
            print(f"\n❌ Sorry, '{guess.upper()}' is not in the word.")
            if mistakes < max_mistakes:
                print(f"⚠️  Careful! {max_mistakes - mistakes} wrong guess(es) left before meltdown!")
        
        input("\n⏳ Press Enter to continue...")
    
    # Display final game state
    display_game_state(mistakes, secret_word, guessed_letters)
    
    # Check win/lose condition and display appropriate message
    if is_word_complete(secret_word, guessed_letters):
        print("\n" + "🎉" * 15)
        print("🏆 VICTORY! You saved the snowman! 🏆")
        print(f"The word was '{secret_word.upper()}' - you got it in {len(guessed_letters)} guesses!")
        print("🎉" * 15)
    else:
        print("\n" + "❄️" * 15)
        print("💔 GAME OVER! The snowman melted completely! 💔")
        print(f"The word was '{secret_word.upper()}'. Try again to save the next snowman!")
        print("❄️" * 15)

def play_game():
    """Main game function with replay functionality."""
    print("\n" + "🎭" * 20)
    print("  🎮 WELCOME TO SNOWMAN MELTDOWN! 🎮  ")
    print("🎭" * 20)
    
    games_played = 0
    games_won = 0
    
    while True:
        games_played += 1
        
        # Play a single game
        play_single_game()
        
        # Count wins (you'd need to modify play_single_game to return win/loss)
        # For now, we'll ask the user
        if ask_play_again():
            print("\n🔄 Starting a new game...")
            continue
        else:
            print("\n👋 Thanks for playing Snowman Meltdown!")
            print(f"📊 You played {games_played} game(s) today.")
            print("🎮 Come back soon to save more snowmen!")
            break