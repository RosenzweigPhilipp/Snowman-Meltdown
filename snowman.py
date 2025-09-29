"""Snowman Meltdown Game - Main Entry Point.

A word guessing game where players try to save a snowman from melting by
correctly guessing letters in a secret word. Each wrong guess causes the
snowman to melt further until either the word is guessed or the snowman
completely melts.

Usage:
    python snowman.py

Author: Your Name
Date: 2025
"""

from game_logic import play_game


def main() -> None:
    """Main function to start the Snowman Meltdown game.
    
    Entry point for the application that initializes and starts the game.
    """
    play_game()


if __name__ == "__main__":
    main()