def rowsRearranging(matrix):

    def swapRows(row1, row2):
        for i in range(len(matrix[0])):
            temp = matrix[row1][i]
            matrix[row1][i] = matrix[row2][i]
            matrix[row2][i] = temp

    for i in range(len(matrix)):
        minIndex = i
        for j in range(i, len(matrix)):
            if matrix[j][0] < matrix[minIndex][0]:
                minIndex = j
        swapRows(i, minIndex)

    answer = True
    for i in range(len(matrix[0])):
        for j in range(1, len(matrix)):
            if matrix[j][i] <= matrix[j - 1][i]:
                answer = False

    return answer
