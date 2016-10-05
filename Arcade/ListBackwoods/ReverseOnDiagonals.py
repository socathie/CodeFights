'''The longest diagonals of a square matrix are defined as follows:

    the first longest diagonal goes from the top left corner to the bottom right one;
    the second longest diagonal goes from the top right corner to the bottom left one.

Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

the output should be

reverseOnDiagonals(matrix) = [[9, 2, 7],
                              [4, 5, 6],
                              [3, 8, 1]]

Input/Output

    [time limit] 4000ms (py)

    [input] array.array.integer matrix

    Constraints:
    1 ≤ matrix.length ≤ 10,
    matrix.length = matrix[i].length,
    1 ≤ matrix[i][j] ≤ 1000.

    [output] array.array.integer

    Matrix with the order of elements on its longest diagonals reversed.'''

def reverseOnDiagonals(matrix):
    size = len(matrix)
    for i in range(0,size/2):
        temp = matrix[i][i]
        matrix[i][i] = matrix[size-i-1][size-i-1]
        matrix[size-i-1][size-i-1] = temp
        temp = matrix[size-i-1][i]
        matrix[size-i-1][i] = matrix[i][size-i-1]
        matrix[i][size-i-1] = temp
    return matrix
