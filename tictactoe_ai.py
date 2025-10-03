

import math


# Board setup
# ----------------------------
board = [' ' for _ in range(9)]  # 3x3 board
human = 'X'
ai = 'O'


# ----------------------------
# Display board
# ----------------------------
def display_board():
    print("\n")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


# ----------------------------
# Check winner
# ----------------------------
def check_winner(b, player):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for cond in win_cond:
        if all(b[i] == player for i in cond):
            return True
    return False


# ----------------------------
# Check tie
# ----------------------------
def check_tie(b):
    return ' ' not in b


# ----------------------------
# Minimax Algorithm
# ----------------------------
def minimax(b, depth, is_maximizing):
    if check_winner(b, ai):
        return 1
    elif check_winner(b, human):
        return -1
    elif check_tie(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = ai
                score = minimax(b, depth+1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = human
                score = minimax(b, depth+1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score


# ----------------------------
# AI Move
# ----------------------------
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = ai


# ----------------------------
# Human Move
# ----------------------------
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = human
                break
            else:
                print("Cell occupied! Try again.")
        except (IndexError, ValueError):
            print("Invalid input! Enter number 1-9.")


# ----------------------------
# Main Game Loop
# ----------------------------
def main():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    display_board()

    while True:
        human_move()
        display_board()
        if check_winner(board, human):
            print("Congratulations! You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

        print("AI is making a move...")
        ai_move()
        display_board()
        if check_winner(board, ai):
            print("AI wins! Better luck next time.")
            break
        if check_tie(board):
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()
