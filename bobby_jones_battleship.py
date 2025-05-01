"""
┌───────────────────────────────────────────────────────────────────────────┐
│                               Battleship Game                             │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Bobby Jones                                                         │
│ Date: 4/21/25                                                             │
│ Log: 1.0                                                                  │
│ Bonus Features: Player vs Player mode, Customizable ship placement,       │
│                 Random first player, Play again option,                   │
│                 Extra turn after hit, 12x12 board size                    │
│ Description: A simplified implementation of the classic Battleship game   │
│              with both single and multiplayer modes.                      │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
"""

import random

def clear_screen():
    """
    Clears the console screen without using os module.
    
    This function prints multiple newlines to create the effect of clearing the screen.
    """
    print("\n" * 49)  # Print 49 newlines to push previous content off screen

def create_board(size=12):
    """
    Creates an empty game board of specified size.
    
    Args:
        size (int): The dimensions of the square board. Default is 12x12.
        
    Returns:
        list: A 2D list representing the empty game board.
    """
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_board(board, hide_ships=False):
    """
    Displays the game board in a user-friendly format.
    
    Args:
        board (list): 2D list representing the game board.
        hide_ships (bool): If True, hides ship positions ('O'). Default is False.
    """
    size = len(board)
    
    # Display single digit numbers for columns
    print("   ", end="")
    for i in range(size):
        if i < 10:
            print(f" {i} ", end="")
        else:
            print(f"{i} ", end="")
    print("\n   ", end="")
    print("---" * size)
    
    # Print rows with row numbers
    for i in range(size):
        if i < 10:
            print(f" {i}|", end="")
        else:
            print(f"{i}|", end="")
        for j in range(size):
            cell = board[i][j]
            # Hide ships when hide_ships is True
            if hide_ships and cell == 'O':
                print("   ", end="")
            else:
                print(f" {cell} ", end="")
        print()
    
    # Print key for symbols and compass
    print("\nKey: 'O' = Ship, 'X' = Miss, '+' = Hit       Compass:  N  ")
    print("                                                      W+E  ")
    print("                                                       S   ")

def place_ship(board, size, row, col, direction):
    """
    Places a ship of specified size on the board.
    
    Args:
        board (list): 2D list representing the game board.
        size (int): The size of the ship to place.
        row (int): Starting row coordinate.
        col (int): Starting column coordinate.
        direction (str): Direction of ship placement ('N', 'S', 'E', or 'W').
        
    Returns:
        bool: True if ship was placed successfully, False otherwise.
    """
    board_size = len(board)
    
    # Determine direction offsets
    if direction == 'N':  # North - going up
        dr, dc = -1, 0
    elif direction == 'S':  # South - going down
        dr, dc = 1, 0
    elif direction == 'E':  # East - going right
        dr, dc = 0, 1
    elif direction == 'W':  # West - going left
        dr, dc = 0, -1
    else:
        return False
    
    # Check if ship fits within board boundaries
    for i in range(size):
        new_row = row + i * dr
        new_col = col + i * dc
        
        if new_row < 0 or new_row >= board_size or new_col < 0 or new_col >= board_size:
            return False
        
        # Check if position is already occupied
        if board[new_row][new_col] != ' ':
            return False
    
    # Place ship
    for i in range(size):
        new_row = row + i * dr
        new_col = col + i * dc
        board[new_row][new_col] = 'O'
    
    return True

def place_random_ships(board, ship_sizes):
    """
    Randomly places ships of specified sizes on the board.
    
    Args:
        board (list): 2D list representing the game board.
        ship_sizes (list): List of ship sizes to place on the board.
        
    Returns:
        int: Total number of ship cells placed on the board.
    """
    ship_count = 0
    board_size = len(board)
    
    for size in ship_sizes:
        placed = False
        attempts = 0
        max_attempts = 100  # Prevent infinite loop
        
        while not placed and attempts < max_attempts:
            direction = random.choice(['N', 'S', 'E', 'W'])
            row = random.randint(0, board_size - 1)
            col = random.randint(0, board_size - 1)
            
            placed = place_ship(board, size, row, col, direction)
            attempts += 1
        
        if placed:
            ship_count += size
    
    return ship_count

def get_player_ship_placement(board, ship_sizes, player_name):
    """
    Allows player to place ships manually on their board.
    
    Args:
        board (list): 2D list representing the player's game board.
        ship_sizes (list): List of ship sizes to place on the board.
        player_name (str): Name of the player for display purposes.
        
    Returns:
        int: Total number of ship cells placed on the board.
    """
    board_size = len(board)
    ship_count = 0
    
    print(f"\n{player_name}, place your ships!")
    
    for ship_size in ship_sizes:
        placed = False
        
        while not placed:
            print_board(board)
            print(f"\nPlacing ship of size {ship_size}")
            
            try:
                row = int(input(f"Enter row (0-{board_size-1}): "))
                if row < 0 or row >= board_size:
                    print(f"Invalid row! Please enter a number between 0 and {board_size-1}.")
                    continue
                
                col = int(input(f"Enter column (0-{board_size-1}): "))
                if col < 0 or col >= board_size:
                    print(f"Invalid column! Please enter a number between 0 and {board_size-1}.")
                    continue
                
                direction = input("Enter direction (N, S, E, W): ").upper()
                if direction not in ['N', 'S', 'E', 'W']:
                    print("Invalid direction! Please enter N, S, E, or W.")
                    continue
                
                placed = place_ship(board, ship_size, row, col, direction)
                
                if not placed:
                    print("Cannot place ship there. It either doesn't fit or overlaps with another ship.")
            except ValueError:
                print("Please enter valid numbers for coordinates.")
        
        ship_count += ship_size
        clear_screen()
    
    print_board(board)
    print(f"\n{player_name}, all your ships have been placed!")
    clear_screen()
    
    return ship_count

def get_valid_shot(board_size, shots_taken):
    """
    Gets valid shot coordinates from the player.
    
    Args:
        board_size (int): Size of the game board.
        shots_taken (list): List of previously taken shots to avoid duplicates.
        
    Returns:
        tuple: A tuple of (row, col) representing valid shot coordinates.
    """
    while True:
        try:
            row = int(input(f"Enter row (0-{board_size-1}): "))
            if row < 0 or row >= board_size:
                print(f"Invalid row! Please enter a number between 0 and {board_size-1}.")
                continue
            
            col = int(input(f"Enter column (0-{board_size-1}): "))
            if col < 0 or col >= board_size:
                print(f"Invalid column! Please enter a number between 0 and {board_size-1}.")
                continue
            
            if (row, col) in shots_taken:
                print("You already fired at that location. Try again.")
                continue
            
            return row, col
        except ValueError:
            print("Please enter valid numbers for coordinates.")

def take_shot(board, row, col, shots_taken):
    """
    Processes a shot at the given coordinates and updates the board.
    
    Args:
        board (list): 2D list representing the game board.
        row (int): Row coordinate of the shot.
        col (int): Column coordinate of the shot.
        shots_taken (list): List to track shots already taken.
        
    Returns:
        bool: True if the shot hit a ship, False otherwise.
    """
    shots_taken.append((row, col))
    
    if board[row][col] == 'O':
        board[row][col] = '+'
        return True
    else:
        board[row][col] = 'X'
        return False

def computer_shot(board_size, shots_taken):
    """
    Generates a random valid shot for the computer.
    
    Args:
        board_size (int): Size of the game board.
        shots_taken (list): List of previously taken shots to avoid duplicates.
        
    Returns:
        tuple: A tuple of (row, col) representing valid shot coordinates.
    """
    available_shots = [(i, j) for i in range(board_size) for j in range(board_size) if (i, j) not in shots_taken]
    return random.choice(available_shots)

def count_hits(board):
    """
    Counts the number of hits on the board.
    
    Args:
        board (list): 2D list representing the game board.
        
    Returns:
        int: The number of hits ('+') on the board.
    """
    return sum(row.count('+') for row in board)

def add_privacy_barrier():
    """
    Adds a privacy barrier between player turns to prevent peeking.
    """
    print("\n\n" + "*" * 80)
    print("\n" * 40)  # Add many blank lines
    print("*" * 80 + "\n\n")
    input("Press Enter to continue to your turn...")
    clear_screen()

def play_battleship():
    """
    Main function to run the Battleship game.
    
    This function handles the game setup, player turns, and win conditions.
    """
    clear_screen()
    print("Welcome to Battleship!")
    
    # Game setup
    board_size = 12  # 12x12 board
    ship_sizes = [2, 2, 3, 3, 4, 5]  # Added a ship of length 5
    max_turns = 10  # Default max turns
    hits_to_win = 19  # Win condition
    
    # Game mode selection
    game_mode = ""
    while game_mode not in ['1', '2']:
        game_mode = input("Select game mode:\n1. Player vs Computer\n2. Player vs Player\nEnter choice (1 or 2): ")
    
    player1_name = input("Enter Player 1's name: ")
    player1_board = create_board(board_size)
    player1_shots_taken = []
    player1_hits = 0
    
    if game_mode == '1':
        player2_name = "Computer"
        player2_board = create_board(board_size)
        player2_ships = place_random_ships(player2_board, ship_sizes)
        player2_shots_taken = []
        player2_hits = 0
    else:
        player2_name = input("Enter Player 2's name: ")
        player2_board = create_board(board_size)
        player2_shots_taken = []
        player2_hits = 0
    
    # Player 1 places ships
    clear_screen()
    player1_ships = get_player_ship_placement(player1_board, ship_sizes, player1_name)
    
    # Add privacy barrier
    add_privacy_barrier()
    
    # Player 2 places ships if human
    if game_mode == '2':
        clear_screen()
        player2_ships = get_player_ship_placement(player2_board, ship_sizes, player2_name)
        add_privacy_barrier()
    
    # Decide who goes first
    current_player = random.choice([1, 2])
    print(f"{player1_name if current_player == 1 else player2_name} goes first!")
    
    # Game loop
    turns_remaining = max_turns * 2  # Total turns for both players
    game_over = False
    
    while not game_over and turns_remaining > 0:
        clear_screen()
        
        if current_player == 1:
            # Player 1's turn
            print(f"{player1_name}'s turn!")
            print(f"Turns remaining: {turns_remaining}")
            print(f"Current hits: {player1_hits}/{hits_to_win}")
            
            # Show boards
            print(f"\n{player1_name}'s board:")
            print_board(player1_board)
            print(f"\n{player2_name}'s board:")
            print_board(player2_board, hide_ships=True)
            
            # Take shot
            print(f"\n{player1_name}, enter your shot coordinates:")
            row, col = get_valid_shot(board_size, player1_shots_taken)
            hit = take_shot(player2_board, row, col, player1_shots_taken)
            
            # Show result
            if hit:
                print("HIT!")
                player1_hits += 1
                if player1_hits >= hits_to_win:
                    print(f"{player1_name} has reached {hits_to_win} hits and wins the game!")
                    game_over = True
                    winner = player1_name
                else:
                    print(f"You get another turn, {player1_name}!")
                    input("\nPress Enter to continue...")
                    continue  # Stay with current player for another turn
            else:
                print("MISS!")
            
            # Switch players
            current_player = 2
            
        else:
            # Player 2's turn
            print(f"{player2_name}'s turn!")
            print(f"Turns remaining: {turns_remaining}")
            print(f"Current hits: {player2_hits}/{hits_to_win}")
            
            if game_mode == '2':
                # Add privacy barrier between turns in 2-player mode
                add_privacy_barrier()
                
                # Show boards for human player 2
                print(f"\n{player2_name}'s board:")
                print_board(player2_board)
                print(f"\n{player1_name}'s board:")
                print_board(player1_board, hide_ships=True)
                
                # Take shot
                print(f"\n{player2_name}, enter your shot coordinates:")
                row, col = get_valid_shot(board_size, player2_shots_taken)
            else:
                # Computer player takes shot
                print(f"\n{player2_name} is taking a shot...")
                row, col = computer_shot(board_size, player2_shots_taken)
                print(f"The computer fires at row {row}, column {col}")
            
            hit = take_shot(player1_board, row, col, player2_shots_taken)
            
            # Show result
            if hit:
                print("HIT!")
                player2_hits += 1
                if player2_hits >= hits_to_win:
                    print(f"{player2_name} has reached {hits_to_win} hits and wins the game!")
                    game_over = True
                    winner = player2_name
                else:
                    print(f"{player2_name} gets another turn!")
                    input("\nPress Enter to continue...")
                    continue  # Stay with current player for another turn
            else:
                print("MISS!")
            
            # Switch players
            current_player = 1
        
        turns_remaining -= 1
        input("\nPress Enter to continue...")
        
        # Add privacy barrier between turns in 2-player mode
        if game_mode == '2':
            add_privacy_barrier()
    
    # Game over
    clear_screen()
    print("\nGame Over!")
    
    if game_over:
        print(f"{winner} wins!")
    else:
        # Check who has more hits
        if player1_hits > player2_hits:
            print(f"{player1_name} wins with {player1_hits} hits vs {player2_hits} hits!")
        elif player2_hits > player1_hits:
            print(f"{player2_name} wins with {player2_hits} hits vs {player1_hits} hits!")
        else:
            print(f"It's a tie! Both players have {player1_hits} hits.")
    
    # Show final boards
    print(f"\n{player1_name}'s final board:")
    print_board(player1_board)
    print(f"\n{player2_name}'s final board:")
    print_board(player2_board)
    
    # Ask to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_battleship()
    else:
        print("Thanks for playing Battleship!")

if __name__ == "__main__":
    play_battleship()
