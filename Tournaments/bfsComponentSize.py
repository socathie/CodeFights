def bfsComponentSize(matrix):
    cnt = 0
    for i in range(len(matrix)):
        if matrix[1][i]:
            cnt += 1
    return cnt+1
