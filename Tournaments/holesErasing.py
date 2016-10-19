def holesErasing(matrix):

    answer = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])):
            if not matrix[i][j]:
                hole = True
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx!=dy:
                            if (0 <= i + dx and i + dx < len(matrix)
                            and 0 <= j + dy and j + dy < len(matrix[0])):
                                if not matrix[i + dx][j + dy]:
                                    hole = False
                if hole:
                    line.append(True)
                else:
                    line.append(False)
            else:
                line.append(True)
        answer.append(line)

    return answer
