'''
Author: Bobby Jones
Date: 12/19/24
Description: Allows the user to play hangman against the computer from a set dictionary of random words from which it chooses randomly
Bugs: None
'''
import random

def select_word():
    """
    Selects a random word from a predefined list.
    
    Returns:
        str: A randomly selected word.
    """
    words = ["python", "hangman", "algorithm", "developer", "programming"]
    return random.choice(words).lower()

def display_board(word, guessed_letters):
    """
    Displays the current state of the word with guessed letters and the hangman graphic.
    
    Args:
        word (str): The word being guessed.
        guessed_letters (list): List of guessed letters.
    """
    # Display word with blanks for unguessed letters
    display = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"\nWord: {display}")

def draw_hangman(guesses_left):
    """
    Draws the hangman based on the number of guesses left.
    
    Args:
        guesses_left (int): Number of incorrect guesses left.
    """
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           0   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           0   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           0   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           0   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           0   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           0   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[6 - guesses_left])

def get_valid_input():
    """
    Prompts the user for valid input (a single letter).
    
    Returns:
        str: The valid input letter.
    """
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a single letter.")

def play_game():
    """
    Executes the main Hangman game loop.
    """
    word = select_word()
    guessed_letters = set()
    incorrect_letters = set()
    incorrect_guesses = 0
    max_guesses = 6

    print("Welcome to Hangman!")
    while incorrect_guesses < max_guesses:
        display_board(word, guessed_letters)
        draw_hangman(max_guesses - incorrect_guesses)
        print(f"Guesses left: {max_guesses - incorrect_guesses}")
        print(f"Incorrect guesses: {', '.join(sorted(incorrect_letters))}")
        
        guess = get_valid_input()
        
        if guess in guessed_letters or guess in incorrect_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            incorrect_letters.add(guess)
            incorrect_guesses += 1
            print("Incorrect guess.")

    draw_hangman(0)
    print(f"You lost! The word was: {word}")

def main():
    """
    Main function to handle game flow and replay option.
    """
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing Hangman! Goodbye!")
            break

if __name__ == "__main__":
    main()
