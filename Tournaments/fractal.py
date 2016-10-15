def fractal(n):
    size = (1 << n) - 1
 
    result = [[0 for i in range(size)] for j in range(size)]
    resultTmp = [[0 for i in range(size)] for j in range(size)]

    def draw(n, row, column, angle):
        size = (1 << n) - 1
        if angle != 0:
            draw(n, row, column, 0)
            while angle > 0:
                angle -= 1
                for i in range(size):
                    for j in range(size):
                        x = result[row + i][column + j]
                        i0 = j
                        j0 = size - i - 1
                        resultTmp[row + i0][column + j0] = (x >> 1) | ((x & 1) << 3)
                for i in range(row, row + size):
                    for j in range(column, column + size):
                        result[i][j] = resultTmp[i][j]
            return
        if n == 1:
            result[row][column] = (1 << 3) - 1
            return
        add = size / 2 + 1
        draw(n-1,row,column,0)
        if n % 2 == 1:
            draw(n - 1, row + add, column, 2)
            draw(n - 1, row, column + add, 3)
            draw(n - 1, row + add, column + add, 3)
            result[row][column + add - 1] = (
                result[row][column + add - 1] | (1 << 2))
            result[row + add - 1][column + add] = (
                result[row + add - 1][column + add] | (1 << 3))
            result[row + size - 1][column + add - 1] = (
                result[row + size - 1][column + add - 1] | (1 << 0))
        else:
            draw(n - 1, row + add, column, 1)
            draw(n - 1, row, column + add, 2)
            draw(n - 1, row + add, column + add, 1)
            result[row + add - 1][column] = (
                result[row + add - 1][column] | (1 << 3))
            result[row + add][column + add - 1] = (
                result[row + add][column + add - 1] | (1 << 2))
            result[row + add - 1][column + size - 1] = (
                result[row + add - 1][column + size - 1] | (1 << 1))

    draw(n, 0, 0, 0)
    answer = [[chr(0) for i in range((size + 1) * 2 - 1)] for j in range(size + 1)]
    for i in range(size):
        for j in range(size):
            cell = result[i][j]
            if (cell >> 2) % 2 == 1:
                answer[i][j * 2 + 1] = '_'
            if (cell >> 0) % 2 == 1:
                answer[i + 1][j * 2 + 1] = '_'
            if (cell >> 3) % 2 == 1:
                answer[i + 1][j * 2] = '|'
            if (cell >> 1) % 2 == 1:
                answer[i + 1][j * 2 + 2] = '|'

    for i in range(size + 1):
        for j in range((size + 1) * 2 - 1):
            if ord(answer[i][j]) == 0:
                answer[i][j] = ' '
            if (answer[i][j] == ' ' and j > 0 and
              answer[i][j - 1] == '_' and j + 1 < len(answer[i]) and
              answer[i][j + 1] == '_'):
                answer[i][j] = '_'
    return answer
