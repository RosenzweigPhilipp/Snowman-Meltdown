# 🎮 Snowman Meltdown

A fun and interactive word-guessing game where you race against time to save a snowman from melting! Each wrong guess brings the snowman closer to complete meltdown. Can you guess the secret word before it's too late?

## 📖 Game Description

**Snowman Meltdown** is a twist on the classic Hangman game. Instead of drawing a gallows, watch as a perfectly built snowman gradually melts away with each incorrect guess. The game features beautiful ASCII art showing 7 different stages of snowman melting, from a perfect winter creation to a sad puddle.

### 🎯 How to Play

1. **Start the Game**: Run the program and you'll be greeted with a welcome screen
2. **Guess Letters**: Try to guess the secret word one letter at a time
3. **Save the Snowman**: Guess all letters correctly before the snowman melts completely
4. **Avoid Mistakes**: You have 6 wrong guesses before the snowman is completely melted
5. **Play Again**: After each game, choose whether to play another round

### ❄️ Snowman Melting Stages

The game features 7 beautifully crafted ASCII art stages showing the snowman's condition:

- **Stage 0**: Perfect snowman with hat, face, and full body
- **Stage 1**: Bottom base starts melting  
- **Stage 2**: Bottom section melting more
- **Stage 3**: Middle section starts melting
- **Stage 4**: Only head with hat remains
- **Stage 5**: Head melting, hat falls
- **Stage 6**: Complete meltdown - only a puddle remains

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No additional libraries required (uses only Python standard library)

### Installation & Running

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RosenzweigPhilipp/Snowman-Meltdown.git
   cd Snowman-Meltdown
   ```

2. **Run the game**:
   ```bash
   python snowman.py
   ```

3. **Start playing**:
   - Follow the on-screen prompts
   - Enter single letters when prompted
   - Try to guess the word before the snowman melts!

## 🎮 Game Features

### 🎨 Visual Experience
- **Beautiful ASCII Art**: 7 detailed snowman melting stages
- **Colorful Interface**: Emojis and visual separators for better UX
- **Clear Progress Tracking**: Health bar showing snowman condition
- **Organized Display**: Separate sections for correct/wrong guesses

### 🛡️ Robust Input Validation
- **Smart Error Handling**: Prevents empty inputs, numbers, and symbols
- **Duplicate Prevention**: Won't accept letters already guessed
- **User-Friendly Messages**: Clear feedback for invalid inputs
- **Continuous Prompting**: Game continues smoothly despite input errors

### 📊 Game Statistics
- **Multi-Game Sessions**: Play multiple rounds in one session
- **Win Rate Tracking**: See your success percentage
- **Game Counter**: Track how many games you've played
- **Performance Feedback**: Celebration messages and encouragement

### 🎯 Enhanced Gameplay
- **Bonus Detection**: Special messages for letters appearing multiple times
- **Progress Indicators**: Visual feedback after each guess
- **Strategic Information**: Word length hints at game start
- **Replay System**: Easy option to play again or quit

## 🏗️ Project Structure

```
Snowman-Meltdown/
├── snowman.py          # Main entry point
├── game_logic.py       # Core game functionality
├── ascii_art.py        # Snowman ASCII art stages
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

### 📁 File Descriptions

- **`snowman.py`**: Main entry point with professional structure and documentation
- **`game_logic.py`**: Contains all game logic including word selection, input validation, game state management, and user interaction
- **`ascii_art.py`**: Stores the 7-stage snowman ASCII art progression
- **`.gitignore`**: Excludes Python cache files and IDE artifacts

## 🛠️ Code Quality

This project demonstrates professional Python development practices:

### 📝 Documentation
- **Google-Style Docstrings**: Comprehensive function documentation
- **Type Annotations**: Full type hint coverage using `typing` module
- **Module Documentation**: Detailed descriptions for each file
- **Usage Examples**: Code examples in docstrings

### 🎯 Code Standards
- **PEP 8 Compliance**: Follows Python style guidelines
- **Type Safety**: Complete type annotation coverage
- **Error Handling**: Robust input validation and error management
- **Modular Design**: Clean separation of concerns

### 🧪 Quality Assurance
- **Tested Functionality**: All features thoroughly tested
- **Input Validation**: Comprehensive edge case handling
- **Code Organization**: Professional project structure
- **Version Control**: Clean Git history with descriptive commits

## 🎲 Game Mechanics

### 🔤 Word Selection
- **Curated Word List**: Programming and technology-themed words
- **Random Selection**: Each game uses a different secret word
- **Balanced Difficulty**: Words range from 3-8 letters

### 🎯 Scoring System
- **Mistake Tracking**: Up to 6 wrong guesses allowed
- **Health Display**: Visual snowman health indicator
- **Guess Counter**: Track total guesses made
- **Win Rate**: Calculate success percentage across sessions

## 🎨 User Experience

### 🌟 Visual Design
- **Emoji Integration**: Engaging visual elements throughout
- **Color Coding**: Different symbols for correct/wrong guesses
- **Clear Separators**: Visual organization with decorative lines
- **Progress Feedback**: Real-time game state updates

### 🎮 Game Flow
- **Smooth Transitions**: "Press Enter to continue" pacing
- **Clear Instructions**: Helpful guidance throughout gameplay
- **Error Recovery**: Graceful handling of invalid inputs
- **Session Management**: Easy replay and quit options

## 🔧 Technical Implementation

### 🐍 Python Features Used
- **Type Hints**: `typing.List` and function annotations
- **String Methods**: `.lower()`, `.strip()`, `.isalpha()`
- **List Comprehensions**: Efficient filtering of guesses
- **Random Module**: Word selection functionality
- **Input Validation**: Comprehensive user input checking

### 📋 Functions Overview

| Function | Purpose | Type Signature |
|----------|---------|----------------|
| `get_random_word()` | Select random word | `() -> str` |
| `display_game_state()` | Show game status | `(int, str, List[str]) -> None` |
| `is_word_complete()` | Check win condition | `(str, List[str]) -> bool` |
| `get_valid_guess()` | Validate user input | `(List[str]) -> str` |
| `play_single_game()` | Single game round | `() -> bool` |
| `play_game()` | Main game loop | `() -> None` |

## 🎓 Educational Value

This project demonstrates key programming concepts:

- **Object-Oriented Thinking**: Modular code organization
- **Input Validation**: Robust user input handling
- **Game State Management**: Tracking and updating game progress  
- **User Experience Design**: Creating engaging interactions
- **Code Documentation**: Professional documentation practices
- **Version Control**: Git workflow and commit practices

## 🤝 Contributing

While this is a learning project, suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is created for educational purposes. Feel free to use and modify for learning!

## 🎮 Have Fun!

Enjoy playing Snowman Meltdown and may you save many snowmen from their melting fate! ❄️

---

*Created as part of a Git and GitHub learning exercise - demonstrating version control, code organization, and Python best practices.*