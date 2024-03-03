# Flash App Game

Welcome to the Flash App Game! This simple app helps you learn Japanese vocabulary in an interactive way. It presents you with Japanese words and their English translations on flashcards, allowing you to test and improve your vocabulary skills.

## Features

- **Flashcards**: View Japanese words and their English translations on flashcards.
- **Interactive Learning**: Flip the flashcards to reveal the English translations.
- **Correct/Wrong Buttons**: Mark whether you've guessed the translation correctly or not.
- **Data Persistence**: Your progress is saved, so you can continue learning from where you left off.

## How to Use

1. Launch the Flash App Game.
2. You'll see a flashcard with a Japanese word displayed.
3. Try to guess the English translation.
4. Click the appropriate button to mark your guess as correct or wrong.
5. The app will present you with the next flashcard.
6. Your progress is automatically saved.

## Requirements

- Python 3.x
- `pandas` library
- `tkinter` library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kibshh/flash_app_game.git
```

2. Navigate to the project directory and run the application:

```bash
python main.py
```

## IMPORTANT NOTE: WHEN YOU LEARN ALL THE WORDS AND THERE IS NONE LEFT, MAKE SURE TO DELETE words_to_learn.csv OR COPY THE CONTENTS OF japanese_words.csv INTO IT

## File Structure

- **main.py**: Contains the main logic for the Flash App Game.
- **config.py**: Configuration file for defining constants and settings.
- **data/**:
  - **japanese_words.csv**: Contains the initial set of Japanese words for learning.
  - **words_to_learn.csv**: Stores the user's progress and words they need to learn.
- **images/**: Contains images used in the application.
- **README.md**: The documentation file you are currently reading.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
