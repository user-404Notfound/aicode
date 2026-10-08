import math

board = [" "] * 9


def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(player):
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def minimax(is_max):
    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if " " not in board:
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best


def best_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


print("TIC-TAC-TOE")
print("You = X, Computer = O")
print("Enter position from 1 to 9")

display()

while True:

    pos = int(input("Enter your position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move!")
        continue

    board[pos] = "X"

    if winner("X"):
        display()
        print("You Win!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    move = best_move()
    board[move] = "O"

    print("Computer selected position:", move + 1)

    if winner("O"):
        display()
        print("Computer Wins!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    display()
