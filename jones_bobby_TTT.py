'''
Author: Bobby Jones
Date: 12/1/24
Description: This program allows a user to play tic tac toe, either against the computer with a random spot choice, or against a second player.
Version Log: 1.0
Bugs: None
Features: None
Sources: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/, https://www.w3schools.com/python/python_try_except.asp

'''

import random


def display_board(board):
    """
    Displays the current state of the Tic Tac Toe board in a 1-9 grid format.
    """
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-" * 9)
    print("\n")


def check_winner(board, mark):
    """
    Checks if the specified mark (X or O) has won.

    Args:
        board (list): The 1D Tic Tac Toe board.
        mark (str): The player's mark ('X' or 'O').

    Returns:
        bool: True if the player with the mark has won, False otherwise.
    """
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal top-left to bottom-right
        [2, 4, 6]   # Diagonal top-right to bottom-left
    ]
    return any(all(board[pos] == mark for pos in condition) for condition in win_conditions)


def get_player_choice(board, player):
    """
    Prompts the player for a move and returns the index for the move.

    Args:
        board (list): The Tic Tac Toe board.
        player (str): The current player ('Player 1' or 'Player 2').

    Returns:
        int: The index for the move (0-8).
    """
    while True:
        try:
            choice = int(input(f"{player}, enter your move (1-9): ")) - 1
            if 0 <= choice <= 8 and board[choice] == ' ':
                return choice
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")


def get_computer_move(board):
    """
    Returns a random unoccupied position on the board for the computer's move.

    Args:
        board (list): The Tic Tac Toe board.

    Returns:
        int: The index for the move (0-8).
    """
    empty_positions = [i for i, mark in enumerate(board) if mark == ' ']
    return random.choice(empty_positions)


def get_valid_num_players():
    """
    Prompts the user to enter the number of players and validates the input.

    Returns:
        int: 1 for single-player, 2 for two-player.
    """
    while True:
        try:
            num_players = int(input("Enter 1 for single player, or 2 for two players: "))
            if num_players in [1, 2]:
                return num_players
            else:
                print("Invalid input! Please enter 1 or 2.")
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")


def get_valid_player_mark():
    """
    Prompts Player 1 to choose their mark ('X' or 'O') and validates the input.

    Returns:
        str: The valid mark ('X' or 'O') chosen by Player 1.
    """
    while True:
        player1_mark = input("Player 1, choose your mark (X or O): ").upper()
        if player1_mark in ['X', 'O']:
            return player1_mark
        print("Invalid input! Please choose 'X' or 'O'.")


def play_game():
    """
    Plays a single game of Tic Tac Toe.
    """
    # Initialize the board
    board = [' ' for _ in range(9)]

    # Choose players
    num_players = get_valid_num_players()
    player1_mark = get_valid_player_mark()
    player2_mark = 'O' if player1_mark == 'X' else 'X'

    # Game loop
    for turn in range(9):
        display_board(board)

        # Determine current player
        current_mark = player1_mark if turn % 2 == 0 else player2_mark
        current_player = "Player 1" if turn % 2 == 0 else "Player 2"

        # Player's turn
        if current_player == "Player 1" or (current_player == "Player 2" and num_players == 2):
            move = get_player_choice(board, current_player)
        else:  # Computer's turn
            print("Computer is making a move...")
            move = get_computer_move(board)

        # Place the mark and check for a win
        board[move] = current_mark
        if check_winner(board, current_mark):
            display_board(board)
            print(f"{current_player} with '{current_mark}' wins!")
            return True

    # If no winner, it's a tie
    display_board(board)
    print("It's a tie!")
    return False


def main():
    """
    Main function to run the Tic Tac Toe game.
    """
    print("Welcome to Tic Tac Toe!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()


