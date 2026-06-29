import random

board = [" "] * 9

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def board_full():
    return " " not in board

print("Welcome to Tic-Tac-Toe!")
print("You are X")
print("""
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

while True:
    # Player move
    print_board()

    try:
        move = int(input("Enter your move (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Invalid position!")
            continue

        if board[move] != " ":
            print("That position is already taken!")
            continue

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break

        if board_full():
            print_board()
            print("It's a draw!")
            break

        # AI move
        available = [i for i in range(9) if board[i] == " "]
        ai_move = random.choice(available)
        board[ai_move] = "O"

        print(f"AI chose position {ai_move + 1}")

        if check_winner("O"):
            print_board()
            print("🤖 AI wins!")
            break

        if board_full():
            print_board()
            print("It's a draw!")
            break

    except ValueError:
        print("Please enter a valid number.")
