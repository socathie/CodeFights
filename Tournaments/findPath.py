def findPath(matrix):

    positionX = -1
    positionY = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                positionX = i
                positionY = j
    for i in range(1, len(matrix) * len(matrix[0])):
        found = False
        nextX = -1
        nextY = -1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx * dy == 0:
                    if (positionX + dx >= 0 and positionX + dx < len(matrix)
                    and  positionY + dy >= 0 and positionY + dy < len(matrix[0])):
                        if matrix[positionX + dx][positionY + dy] == i + 1:
                            found = True
                            nextX = positionX + dx
                            nextY = positionY + dy
        if found:
            positionX = nextX
            positionY = nextY
        else:
            return False
    return True
