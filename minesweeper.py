import random

def initialize_board(size, mines):
    board = [[0 for _ in range(size)] for _ in range(size)]
    for _ in range(mines):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if board[x][y] != 'X':
                board[x][y] = 'X'
                break
    return board

def update_numbers(board, size):
    for x in range(size):
        for y in range(size):
            if board[x][y] == 'X':
                continue
            count = 0
            for i in range(max(0, x-1), min(size, x+2)):
                for j in range(max(0, y-1), min(size, y+2)):
                    if board[i][j] == 'X':
                        count += 1
            board[x][y] = count

def print_board(board, size):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def play_minesweeper(size, mines):
    board = initialize_board(size, mines)
    update_numbers(board, size)
    print_board(board, size)

# Example usage:
play_minesweeper(10, 10)
