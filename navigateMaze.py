"""
Navigate a maze - use backtracking to travel through a maze
Conditions:
Maze is m x n size
Start at upper left, destination is bottom right
Can only move right or down
0 represents dead end, 1 represents open position

If a solution exists, 1 represents possible path taken to reach destination
"""

import numpy as np

# Check if position is blocked or not
def check_position(maze, row, col):
    maze_shape = np.array(maze).shape
    
    if row < maze_shape[0] and col < maze_shape[1] and maze[row][col] == 1:
        return True
    
    return False
    
# Solve maze
def solve_maze(maze, solution, row=0, col=0):
    
    maze_shape = np.array(maze).shape
    max_row_index = maze_shape[0] - 1
    max_col_index = maze_shape[1] - 1
    
    # Check if current position is the destination   
    if (row == max_row_index) and (col == max_col_index) and \
        (maze[max_row_index][max_col_index] == 1):
            
        solution[row][col] = 1
        return True
    
    if check_position(maze, row, col):
        
        solution[row][col] = 1
        
        # try next possible positions
        if solve_maze(maze, solution, row + 1, col):
            return True
        
        if solve_maze(maze, solution, row, col + 1):
            return True
        
        solution[row][col] = 0
        return False

# Find path
def find_path(maze):
    
    path = np.zeros(np.array(maze).shape, dtype=int)
    
    if solve_maze(maze, path):
        for row in range(path.shape[0]):
            for col in range(path.shape[1]):
                print(path[row][col], end=' ')
            print('')
            
    elif not check_position(maze, 0, 0):
        print("Can't enter maze")
        
    else:
        print("Can't reach destination")

        
# =============================DRIVER CODE========================================

test_maze = [[1, 1, 0, 0, 0],
             [1, 0, 1, 0, 1],
             [1, 1, 1, 1, 0],
             [0, 0, 1, 1, 1]]

find_path(test_maze)