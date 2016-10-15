def howManyLines(X, Y):

    result = []
    for i in range(1, len(X)):
        result.append(0)

    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            A = Y[i] - Y[j] 
            B = X[j] - X[i]
            C = - A * X[i] - B * Y[i]
            countPoints = 0
            for k in range(len(X)):
                if A * X[k] + B * Y[k] + C == 0:
                    countPoints += 1
            result[countPoints - 2] += 1
    for i in range(len(X) - 1):
        result[i] /= (i + 1) * (i + 2) / 2
    return result
