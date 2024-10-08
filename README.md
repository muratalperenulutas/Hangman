# Hangman Game

Hangman is a classic word-guessing game where players try to guess a secret word by suggesting letters within a limited number of attempts. This version of Hangman includes additional features such as difficulty levels, hints, and the ability to save and load your game progress.

## Features

- **Three Difficulty Levels**: Choose from Easy, Medium, or Hard levels to match your skill.
- **Hints**: Get helpful hints related to the word you are trying to guess.
- **Save and Load**: Save your game progress and continue playing later.
- **Scoring System**: Scores are calculated based on correct guesses, remaining attempts, and the complexity of the word.

## How to Play

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/muratalperenulutas/Hangman.git
    cd Hangman
    ```

2. **Run the Game**:
    ```sh
    python main.py
    ```

3. **Follow the Prompts**:
    - Select the difficulty level.
    - Guess letters one by one or guess the entire word.
    - Use hints if needed by typing 'hint'.
    - Try to guess the entire word before you run out of attempts.

## Example Gameplay

```sh
Welcome to Hangman Game!

1. Easy (1)
2. Medium (2)
3. Hard (3)
Enter difficulty level: 1

You have 6 attempts
Word: _______

         ------
         |    |
         |
         |
         |
         |
        ---

Guess a letter, guess the word or type 'hint' for a hint:t
Incorrect guess. Try again.

You have 5 attempts
Word: _______

         ------
         |    |
         |    O
         |
         |
         |
        ---

Guess a letter, guess the word or type 'hint' for a hint:h
Good guess!

You have 5 attempts
Word: h______

         ------
         |    |
         |    O
         |
         |
         |
        ---

Guess a letter, guess the word or type 'hint' for a hint:hint
Hint: It's the name of this game!

You have 5 attempts
Word: h______

         ------
         |    |
         |    O
         |
         |
         |
        ---

Guess a letter, guess the word or type 'hint' for a hint:hangman
Congratulations! You guessed the word: hangman
Your score: 500
```
## License

This project is licensed under the MIT License.

Enjoy playing Hangman and challenge your word-guessing skills!



