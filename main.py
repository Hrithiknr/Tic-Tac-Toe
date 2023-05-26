import random

# Function to create an empty board
def create_board():
    board = []
    for _ in range(3):
        row = ['-'] * 3
        board.append(row)
    return board

# Function to display the board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

# Function to get the player's move
def get_player_move(board):
    while True:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1

            if board[row][col] != '-':
                print("That spot is already taken. Try again.")
                continue

            return row, col
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

# Function to randomly select the starting player
def get_starting_player():
    return random.choice(['X', 'O'])

# Main game loop
def play_game():
    board = create_board()
    player = get_starting_player()

    while True:
        display_board(board)

        print(f"Player {player}'s turn")
        row, col = get_player_move(board)

        board[row][col] = player

        if check_winner(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

# Start the game
play_game()
