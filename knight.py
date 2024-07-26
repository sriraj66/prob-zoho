def is_safe(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solve_knight_tour_util(board, curr_x, curr_y, move_i, x_move, y_move, n):
    if move_i == n**2:
        return True

    for k in range(8):
        next_x, next_y = curr_x + x_move[k], curr_y + y_move[k]
        if is_safe(next_x, next_y, board, n):
            board[next_x][next_y] = move_i
            if solve_knight_tour_util(board, next_x, next_y, move_i + 1, x_move, y_move, n):
                return True
            board[next_x][next_y] = -1
    return False

def solve_knight_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0
    if not solve_knight_tour_util(board, 0, 0, 1, x_move, y_move, n):
        print("Solution does not exist")
    else:
        print_solution(board, n)

# Example usage:
solve_knight_tour(8)
