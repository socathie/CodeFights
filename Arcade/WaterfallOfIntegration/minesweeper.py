def neighbors(matrix,i,j,row,col):
    mine = 0
    if not ((i < 1) or (j < 1)):
        if matrix[i - 1][j - 1]:
            mine+=1
    if not (i < 1):
        if matrix[i - 1][j]:
            mine+=1
    if not ((i < 1) or (j >= col-1)):
        if matrix[i - 1][j + 1]:
            mine+=1
    if not (j >= col-1):
        if matrix[i][j + 1]:
            mine+=1
    if not ((i >= row-1) or (j >= col-1)):
        if matrix[i + 1][j + 1]:
            mine+=1
    if not (i >= row-1):
        if matrix[i + 1][j]:
            mine+=1
    if not ((i >= row-1) or (j < 1)):
        if matrix[i + 1][j - 1]:
            mine+=1
    if not (j < 1):
        if matrix[i][j - 1]:
            mine+=1
    return mine
            
def minesweeper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    sol = []
    for i in range(0,row):
        temp = []
        for j in range(0,col):
            temp.append(neighbors(matrix,i,j,row,col))
        sol.append(temp)
    
    return sol
    
'''In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]       
Check out the image below for better understanding:



Input/Output

[time limit] 4000ms (py)
[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.

Constraints:
2 ≤ matrix.length ≤ 5,
2 ≤ matrix[0].length ≤ 5.

[output] array.array.integer

Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.'''
