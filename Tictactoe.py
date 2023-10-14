def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That position is already taken. Try again.")

    if moves == 9:
        print_board(board)
        print("It's a tie!")

tic_tac_toe()
