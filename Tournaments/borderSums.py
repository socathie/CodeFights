def borderSums(matrix):

    result = []

    for i in range(len(matrix) / 2):
        result.append(0)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            border = min(i, j)
            border = min(border, len(matrix) - i - 1)
            border = min(border, len(matrix) - j - 1)
            result[border] += matrix[i][j] 

    return result
