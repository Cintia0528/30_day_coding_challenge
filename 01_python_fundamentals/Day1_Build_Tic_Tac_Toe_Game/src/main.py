import random


# ----------------------------
# Board Utilities
# ----------------------------

def create_board():
    return [' ' for _ in range(10)]


def print_board(board):
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('   |   |   ')
    print()


def is_space_free(board, pos):
    return board[pos] == ' '


def is_board_full(board):
    return ' ' not in board[1:]


def is_winner(board, letter):
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or
        (board[1] == letter and board[5] == letter and board[9] == letter) or
        (board[3] == letter and board[5] == letter and board[7] == letter)
    )


# ----------------------------
# Moves
# ----------------------------

def insert_mark(board, mark, pos):
    board[pos] = mark


def player_move(board):
    while True:
        try:
            pos = int(input("Choose position (1-9): "))
            if pos in range(1, 10) and is_space_free(board, pos):
                return pos
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


def select_random(moves):
    return random.choice(moves)


def computer_move(board):
    possible_moves = [i for i in range(1, 10) if is_space_free(board, i)]

    # Win or block
    for letter in ['O', 'X']:
        for move in possible_moves:
            copy = board[:]
            copy[move] = letter
            if is_winner(copy, letter):
                return move

    # Corners
    corners = [i for i in possible_moves if i in [1, 3, 7, 9]]
    if corners:
        return select_random(corners)

    # Center
    if 5 in possible_moves:
        return 5

    # Edges
    edges = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges:
        return select_random(edges)


# ----------------------------
# Main Game Loop
# ----------------------------

def main():
    print("Welcome to Tic Tac Toe!")
    board = create_board()
    print_board(board)

    while not is_board_full(board):

        # Player
        pos = player_move(board)
        insert_mark(board, 'X', pos)
        print_board(board)

        if is_winner(board, 'X'):
            print("Congratulations, you won!")
            break

        # Computer
        move = computer_move(board)
        if move:
            insert_mark(board, 'O', move)
            print("Computer chose position", move)
            print_board(board)

        if is_winner(board, 'O'):
            print("You lost!")
            break

    if is_board_full(board):
        print("It's a tie!")

    replay = input("Play again? (y/n): ")
    if replay.lower() == 'y':
        main()


if __name__ == "__main__":
    main()