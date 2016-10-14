def sudoku(grid):
    d1 = []
    d2 = []
    for i in range(0,9):
        if len(set(grid[i]))!=9:
            return False
        if len(set([row[i] for row in grid]))!=9:
            return False
        
    for i in range(0,9,3):
        for j in range(0,9,3): 
            box = grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]
            if len(set(box))!=9:
                return False
            
    return True

'''Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For the first example below, the output should be true. For the other grid, the output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.



Input/Output

[time limit] 4000ms (py)
[input] array.array.integer grid

A matrix representing 9 × 9 grid already filled with numbers.

[output] boolean

true if the given grid represents a correct solution to Sudoku, false otherwise.'''
