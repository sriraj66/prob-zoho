def is_safe(maze, x, y, n):
    """Check if x, y is a valid cell in the maze"""
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def solve_maze_util(maze, x, y, sol):
    """Utilize backtracking to solve the maze"""
    n = len(maze)
    
    # If (x, y) is the goal, mark it and return True
    if x == n - 1 and y == n - 1:
        sol[x][y] = 1
        return True
    
    if is_safe(maze, x, y, n):
        # Mark x, y as part of the solution path
        sol[x][y] = 1
        
        # Move forward in the x direction
        if solve_maze_util(maze, x + 1, y, sol):
            return True
        
        # If moving in x direction doesn't give a solution, move down in the y direction
        if solve_maze_util(maze, x, y + 1, sol):
            return True
        
        # If moving down in y direction doesn't give a solution, move back up in the x direction
        if solve_maze_util(maze, x - 1, y, sol):
            return True
        
        # If moving back up in x direction doesn't give a solution, move left in the y direction
        if solve_maze_util(maze, x, y - 1, sol):
            return True
        
        # If none of the above movements work, BACKTRACK: unmark x, y as part of the solution path
        sol[x][y] = 0
        return False
    
    return False

def solve_maze(maze):
    """Solve the maze and print the solution path"""
    n = len(maze)
    sol = [[0 for _ in range(n)] for _ in range(n)]
    
    if not solve_maze_util(maze, 0, 0, sol):
        print("No solution exists")
        return False
    
    for row in sol:
        print(row)
    return True

# Example maze
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze)
