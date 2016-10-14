def polygonPerimeter(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    perimeter = 0
    for i in range(nrow):
        for j in range(ncol):
            if matrix[i][j]:
                perimeter += 4
    
    for i in range(nrow):
        for j in range(ncol):
            if j != ncol-1:
                if matrix[i][j] and matrix[i][j+1]:
                    perimeter -= 2
            if i != nrow-1:
                if matrix[i][j] and matrix[i+1][j]:
                    perimeter -= 2
    
    return perimeter

'''You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is possible to get from any black cell to any other one through connected adjacent (sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit length.

It's guaranteed that there is at least one black cell on the table.

Example

For

matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]
the output should be
polygonPerimeter(matrix) = 12.



For

matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]
the output should be
polygonPerimeter(matrix) = 16.



Input/Output

[time limit] 4000ms (py)
[input] array.array.boolean matrix

A matrix of booleans representing the rectangular board where true means a black cell and false means a white one.

Constraints:
2 ≤ matrix.length ≤ 5,
2 ≤ matrix[0].length ≤ 5.

[output] integer'''
