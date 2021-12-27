# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:16:30 2021

@author: Marchiano

Sudoku solver using backtraking algorithm

Steps followed:
1) Find empty position on grid
2) Check if value on specified grid position is admissible
3) If valid, solve recursively the puzzle by repeating steps 1 and 2 for the entire grid.
   Otherwise, reset position that was just filled to initial unfilled state.
"""     
        
# find empty element in grid (represented by 0) and return position
# if no empty element is found, return None
def find_empty(grid):
    gridDim = 9
    
    for row in range(gridDim):
        for col in range(gridDim):
            if grid[row][col] == 0:
                return (row, col)
    
    return None


# check if number of interest is valid in given position
# num: number of interest (1 to 9)
# pos: position of number of interest as tuple (row, col)
# grid: sudoku grid
def is_valid(num, pos, grid):
    gridDim = 9
    boxDim = 3
    
    row_num = pos[0] # row the number of interest is in
    col_num = pos[1] # column the number of interest is in
    
    # check if num already exists in specified row and return False (for not valid) if it exists
    for col in range(gridDim):
        if grid[row_num][col] == num:
            return False

    # check if num already exists in specified column and return False (for not valid) if it exists
    for row in range(gridDim):
        if grid[row][col_num] == num:
            return False

    # check if num already exists in its box and return False (for not valid) if it exists
    row_box = row_num // boxDim
    col_box = col_num // boxDim
    
    for row in range(row_box * boxDim, row_box * boxDim + boxDim):
        for col in range(col_box * boxDim, col_box * boxDim + boxDim):
            if grid[row][col] == num:
              return False
    
    # check if num already exists in its 3x3 box and return False (for not valid) if it exists
    # Check box
    # box_x = pos[1] // 3
    # box_y = pos[0] // 3

    # for row in range(box_y*3, box_y*3 + 3):
    #     for col in range(box_x * 3, box_x*3 + 3):
    #         if grid[row][col] == num:
    #             return False
            
    return True
            

# solve Sudoku puzzle given grid and return solution if it exists
def sudoku_solver(grid):
    gridDim = 9
    start = 1 # number Sudoku puzzle starts at
    
    empty_pos = find_empty(grid)
    
    # base case
    if bool(empty_pos):
        row, col = empty_pos
    else:
        return True # return True if no empty positions exist and thus, solution exists
    
    for n in range(start, gridDim + 1):
        if is_valid(n, (row, col), grid):
            grid[row][col] = n
            
            if sudoku_solver(grid): # recursive solver call
                return True
            
            grid[row][col] = 0 # reset the board
        
    return False


# print sudoku solution if it exists
# otherwise, print statement that no solution found  
def print_solution(grid):
    if sudoku_solver(grid):
        gridDim = 9
    
        for row in range(gridDim):
            for col in range(gridDim):
                print(grid[row][col], end=' ')
            print('') # print nothing to start on new line since default end in print is '\n'
    else:
        print("No solution found")
        
        
# =============================DRIVER CODE========================================

grid = [[0, 0, 3, 0, 0, 0, 0, 0, 9],
          [0, 0, 0, 0, 7, 0, 0, 0, 0],
          [2, 0, 0, 5, 8, 0, 3, 0, 0],
          [0, 8, 0, 1, 5, 0, 0, 0, 4],
          [0, 0, 0, 0, 0, 7, 5, 0, 0],
          [1, 0, 0, 0, 0, 9, 0, 0, 0],
          [0, 4, 0, 0, 0, 0, 0, 6, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0],
          [8, 0, 0, 2, 3, 0, 9, 0, 0]]

print_solution(grid)
    