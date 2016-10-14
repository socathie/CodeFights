def rowsRearranging(matrix):
    matrix = sorted(matrix, key = lambda m: m[0])
    for i in range(len(matrix[0])):
        for j in range(len(matrix)-1):
            if matrix[j+1][i]<=matrix[j][i]:
                return False
    return True

'''Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns become strictly increasing sequences (read from top to bottom).

Example

For

matrix = [[2, 7, 1], 
          [0, 2, 0], 
          [1, 3, 1]]
the output should be
rowsRearranging(matrix) = false;

For

matrix = [[6, 4], 
          [2, 2], 
          [4, 3]]
the output should be
rowsRearranging(matrix) = true.

Input/Output

[time limit] 4000ms (py)
[input] array.array.integer matrix

A 2-dimensional array of integers.

Constraints:
1 ≤ matrix.length ≤ 10,
1 ≤ matrix[0].length ≤ 10,
-300 ≤ matrix[i][j] ≤ 300.

[output] boolean'''
