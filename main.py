import random
import time
import json

attempts=6

hint_dict = {
    "python": "It's a popular programming language.",
    "java": "A widely used programming language.",
    "ruby": "A dynamic, reflective, and object-oriented language.",
    "html": "Used for creating the structure of web pages.",
    "css": "Used for styling and layout of web pages.",
    "hangman": "It's the name of this game!",
    "computer": "An electronic device for processing data.",
    "keyboard": "You use it to input text into your computer.",
    "developer": "Someone who writes code to create software.",
    "algorithm": "A step-by-step procedure for solving a problem.",
    "science": "A systematic enterprise that builds and organizes knowledge.",
    "programming": "Involves writing code to create software.",
    "encryption": "The process of converting information into a secret code.",
    "interface": "A point where two systems meet and interact.",
    "javascript": "A scripting language for creating interactive web pages.",
    "framework": "A reusable set of libraries or tools for software development."
}

difficulty_levels = {
    "1": ["python", "java", "ruby", "html", "css"],
    "2": ["hangman", "computer", "keyboard", "developer", "algorithm"],
    "3": ["programming", "encryption", "interface", "javascript", "framework"]
}

def choose_word():
    while True:
        difficulty = input("1. Easy (1)\n2. Medium (2)\n3. Hard (3)\nEnter difficulty level: ")

        if difficulty in difficulty_levels:
            return random.choice(difficulty_levels[difficulty])
        else:
            print("Invalid difficulty level. Please enter 1, 2, or 3.")


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman_image(lives):
    images = [
        """
         ------
         |    |
         |
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        """
    ]
    return images[lives]

def calculate_score(correct_guesses, remaining_lives,secret_word):
    if remaining_lives==0:
        return 0
    return (len(set(secret_word))-correct_guesses)*100 + correct_guesses*50 + remaining_lives*10

def save_game_status(secret_word, guessed_letters, remaining_lives, correct_guesses, status):
    game_status = {
        "Word": secret_word,
        "GuessedLetters": guessed_letters,
        "RemainingAttempts": remaining_lives,
        "CorrectGuesses": correct_guesses,
        "GameStatus": status
    }
    with open("game.json", "w") as save_game:
        json.dump(game_status, save_game)

def load_game():
    with open("game.json", "r") as saved_game:
        game_status = json.load(saved_game)
        return (game_status["Word"], 
                game_status["GuessedLetters"], 
                game_status["RemainingAttempts"], 
                game_status["CorrectGuesses"])

def saved_game_detect():
    try:
        with open("game.json", 'r') as file:
            status = json.load(file)
            return status["GameStatus"]
    except :
        return None

def hangman():
    correct_guesses=0
    guessed_letters =[]
    remaining_lives=attempts
    
    print("Welcome to Hangman Game!\n")

    if saved_game_detect()=="continue":
        while True:
            choice=input("Saved game found! Do you want to continue?(Y/N):").lower()
            if choice=="y" or choice=="n":
                break
            else:
                print("Invalid input. Please try again.")

        if choice=="y":
            secret_word, guessed_letters, remaining_lives, correct_guesses = load_game()
            guessed_letters = list(guessed_letters)
            remaining_lives = int(remaining_lives)
            correct_guesses = int(correct_guesses)

        else:
            secret_word=choose_word()
            
    else:
        secret_word=choose_word()  
    
    while remaining_lives>0 :
        save_game_status(secret_word,guessed_letters,remaining_lives,correct_guesses,status="continue")
        displayed_word=display_word(secret_word,guessed_letters)
        print("\nYou have", remaining_lives,"attempts")
        print("Word:", displayed_word)
        print(hangman_image(6-remaining_lives))

        guess = input("Guess a letter, guess the word or type 'hint' for a hint:").lower()
        if guess == 'hint':
            print("Hint:", hint_dict.get(secret_word))
        elif guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break


        elif guess.isalpha() and len(guess) == 1: 
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("Good guess!")
                correct_guesses += 1
            else:
                remaining_lives -= 1
                print("Incorrect guess. Try again.")

        else:
            print("Invalid input.Please try again")

        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if remaining_lives==0:
        print(hangman_image(6-remaining_lives))
        print("Sorry, you ran out of attempts. The word was:", secret_word)

    print("Your score:", calculate_score(correct_guesses, remaining_lives,secret_word))
    save_game_status(secret_word,guessed_letters,remaining_lives,correct_guesses,status="finish")
    
    time.sleep(5)
    
hangman()
 