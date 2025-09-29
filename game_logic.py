"""Main game logic for Snowman Meltdown.

This module contains all the core game functionality including word selection,
input validation, game state management, and user interaction.
"""

import random
from typing import List

from ascii_art import STAGES

# List of secret words used in the game
WORDS: List[str] = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word() -> str:
    """Selects a random word from the predefined word list.
    
    Returns:
        str: A randomly selected word from WORDS list.
        
    Examples:
        >>> word = get_random_word()
        >>> word in WORDS
        True
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes: int, secret_word: str, 
                       guessed_letters: List[str]) -> None:
    """Display the current game state including snowman, word progress, guesses.
    
    Args:
        mistakes: Number of incorrect guesses made so far.
        secret_word: The target word to be guessed.
        guessed_letters: List of all letters guessed by the player.
        
    Examples:
        >>> display_game_state(0, "python", ["p", "y"])
        # Displays stage 0 snowman and "P Y _ _ _ _"
    """
    print_separator()
    print(STAGES[mistakes])
    
    # Build a display version of the secret word with better formatting
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "_ "
    
    max_health = len(STAGES) - 1
    current_health = max_health - mistakes
    
    print(f"📝 Word: {display_word}")
    print(f"❄️  Snowman Health: {current_health}/{max_health}")
    
    # Show guessed letters if any with better formatting
    if guessed_letters:
        correct_guesses = [
            letter for letter in guessed_letters if letter in secret_word
        ]
        wrong_guesses = [
            letter for letter in guessed_letters if letter not in secret_word
        ]
        
        if correct_guesses:
            correct_display = ', '.join(sorted(correct_guesses)).upper()
            print(f"✅ Correct guesses: {correct_display}")
        if wrong_guesses:
            wrong_display = ', '.join(sorted(wrong_guesses)).upper()
            print(f"❌ Wrong guesses: {wrong_display}")
    
    print_separator()

def is_word_complete(secret_word: str, guessed_letters: List[str]) -> bool:
    """Check if all letters in the secret word have been guessed.
    
    Args:
        secret_word: The target word to check completion for.
        guessed_letters: List of letters that have been guessed.
        
    Returns:
        bool: True if all letters in secret_word are in guessed_letters,
              False otherwise.
              
    Examples:
        >>> is_word_complete("cat", ["c", "a", "t"])
        True
        >>> is_word_complete("cat", ["c", "a"])
        False
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def get_valid_guess(guessed_letters: List[str]) -> str:
    """Get a valid single letter guess from user with comprehensive validation.
    
    Validates input to ensure it's a single alphabetic character that hasn't
    been guessed before. Continues prompting until valid input is received.
    
    Args:
        guessed_letters: List of previously guessed letters to check against.
        
    Returns:
        str: A valid single lowercase letter that hasn't been guessed before.
        
    Examples:
        >>> # User enters 'a' (assuming 'a' not in guessed_letters)
        >>> guess = get_valid_guess(['b', 'c'])
        >>> guess
        'a'
    """
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
            print(f"❌ You already guessed '{guess.upper()}'. "
                  "Try a different letter!")
            continue
            
        return guess


def print_separator() -> None:
    """Print a decorative separator line for better visual formatting.
    
    Prints a line of 50 double horizontal line characters (═) to create
    visual separation between different sections of the game output.
    """
    print("═" * 50)


def ask_play_again() -> bool:
    """Ask the user if they want to play another game.
    
    Prompts the user for input and validates their response. Accepts
    'y', 'yes' (case insensitive) for yes, and 'n', 'no' for no.
    Continues prompting until valid input is received.
    
    Returns:
        bool: True if user wants to play again, False otherwise.
        
    Examples:
        >>> # User enters 'y'
        >>> ask_play_again()
        True
        >>> # User enters 'no'
        >>> ask_play_again()
        False
    """
    while True:
        choice = input("\n🔄 Would you like to play again? (y/n): ").strip()
        choice = choice.lower()
        
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def play_single_game() -> bool:
    """Play a single round of Snowman Meltdown.
    
    Manages the complete gameplay flow for one game including word selection,
    user input handling, game state updates, and win/lose determination.
    
    Returns:
        bool: True if player won (saved the snowman), False if they lost.
        
    Examples:
        >>> # Player successfully guesses the word
        >>> result = play_single_game()
        >>> result
        True
    """
    secret_word = get_random_word()
    guessed_letters: List[str] = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # Maximum mistakes before game over

    print("\n🎮 " + "="*20 + " NEW GAME " + "="*20 + " 🎮")
    print("🎯 Save the snowman by guessing the secret word!")
    print(f"⚠️  You have {max_mistakes} wrong guesses before the snowman "
          "melts!")
    print(f"💡 The word has {len(secret_word)} letters.")
    # Uncomment for testing: print("Secret word selected: " + secret_word)
    
    # Main game loop
    while (mistakes < max_mistakes and 
           not is_word_complete(secret_word, guessed_letters)):
        display_game_state(mistakes, secret_word, guessed_letters)
        
        # Get validated user input
        guess = get_valid_guess(guessed_letters)
        
        # Add guess to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"\n✨ Excellent! '{guess.upper()}' is in the word! ✨")
            letter_count = secret_word.count(guess)
            if letter_count > 1:
                print(f"🎉 Bonus! '{guess.upper()}' appears {letter_count} "
                      "times!")
        else:
            mistakes += 1
            print(f"\n❌ Sorry, '{guess.upper()}' is not in the word.")
            remaining_guesses = max_mistakes - mistakes
            if mistakes < max_mistakes:
                print(f"⚠️  Careful! {remaining_guesses} wrong guess(es) left "
                      "before meltdown!")
        
        input("\n⏳ Press Enter to continue...")
    
    # Display final game state
    display_game_state(mistakes, secret_word, guessed_letters)
    
    # Check win/lose condition and display appropriate message
    player_won = is_word_complete(secret_word, guessed_letters)
    
    if player_won:
        print("\n" + "🎉" * 15)
        print("🏆 VICTORY! You saved the snowman! 🏆")
        print(f"The word was '{secret_word.upper()}' - you got it in "
              f"{len(guessed_letters)} guesses!")
        print("🎉" * 15)
    else:
        print("\n" + "❄️" * 15)
        print("💔 GAME OVER! The snowman melted completely! 💔")
        print(f"The word was '{secret_word.upper()}'. Try again to save the "
              "next snowman!")
        print("❄️" * 15)
    
    return player_won

def play_game() -> None:
    """Main game function with replay functionality and statistics tracking.
    
    Manages the overall game session including welcome screen, multiple games,
    win/loss tracking, and final statistics display. Continues until the
    player chooses to quit.
    
    The function displays game statistics at the end showing total games
    played and games won.
    
    Examples:
        >>> play_game()
        # Starts the game session with welcome screen and game loop
    """
    print("\n" + "🎭" * 20)
    print("  🎮 WELCOME TO SNOWMAN MELTDOWN! 🎮  ")
    print("🎭" * 20)
    
    games_played = 0
    games_won = 0
    
    while True:
        games_played += 1
        
        # Play a single game and track the result
        player_won = play_single_game()
        if player_won:
            games_won += 1
        
        if ask_play_again():
            print("\n🔄 Starting a new game...")
            continue
        else:
            print("\n👋 Thanks for playing Snowman Meltdown!")
            print(f"📊 You played {games_played} game(s) today.")
            if games_played > 0:
                win_percentage = (games_won / games_played) * 100
                print(f"🏆 You saved {games_won} snowman(s) "
                      f"({win_percentage:.1f}% success rate)!")
            print("🎮 Come back soon to save more snowmen!")
            break