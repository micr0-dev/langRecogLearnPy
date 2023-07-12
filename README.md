# langRecogLearnPy

## Overview

langRecogLearnPy is a Python-based, text-based game aimed at helping users learn to recognize various languages. Leveraging the power of Google's Translate API, the game presents the user with phrases translated into different languages and asks the user to guess which language it is.

## Features

- Wide variety of languages: The game includes a broad range of languages from around the world, from French and German to Hindi and Japanese.
- Persistent progress tracking: The game tracks your progress and stores it in a .csv file. This way, you can see how you're improving over time and which languages you're having the most trouble with.
- User-friendly: The game is text-based, which makes it easy to understand and play. You just need to enter your guess, and the game will tell you if you're right or wrong, and what the correct language was.
- Stats tracking: Apart from recording each guess, the game also provides summary statistics, such as your total number of guesses, accuracy rate, and the languages you most often guess correctly and incorrectly.

## Installation

1. Clone this repository: `git clone https://github.com/yourusername/langRecogLearnPy.git`
2. Navigate to the cloned repo: `cd langRecogLearnPy`
3. Ensure you have the necessary Python packages installed. You can install them using pip:
   - `pip install googletrans pandas fuzzywuzzy python-Levenshtein`

## Usage

To run the game, navigate to the directory containing the script and type `python langRecogLearnPy.py` in your terminal.

The game will ask you for your username and then provide you with a translated phrase. Your task is to guess the language of the translated phrase. If you need to skip a phrase, just type `skip`. If you wish to quit the game, type `quit`.

You can review your stats by typing `data`. This will display your total guesses, your accuracy rate, the language you most often guess correctly, the language you often guess incorrectly, and the top five language mix-ups.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE v3 - see the LICENSE file for details.
