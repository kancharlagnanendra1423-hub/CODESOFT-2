# Tic-Tac-Toe Game in Python

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def board_full():
    return " " not in board

current_player = "X"

print("Welcome to Tic-Tac-Toe!")
print("Choose positions from 1 to 9 as shown below:")

print("""
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

while True:
    print_board()

    try:
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Invalid position! Choose between 1 and 9.")
            continue

        if board[move] != " ":
            print("That position is already taken!")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if board_full():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    except ValueError:
        print("Please enter a valid number.")
