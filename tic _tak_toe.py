def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw(board):
    return " " not in board


def main():
    board = [" "] * 9
    player = "X"

    print("=== TIC TAC TOE ===")
    print("Board positions:")
    print("""
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1

            if move not in range(9):
                print("Invalid position!")
                continue

            if board[move] != " ":
                print("Position already occupied!")
                continue

            board[move] = player

            if check_winner(board, player):
                print_board(board)
                print(f"🎉 Player {player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("🤝 It's a draw!")
                break

            player = "O" if player == "X" else "X"

        except ValueError:
            print("Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
