def matrixTransposition(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    m = []
    
    for j in range(ncol):
        m.append([])
        for i in range(nrow):
            m[j].append(matrix[i][j])
    
    return m
