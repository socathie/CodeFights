def arrayCenter(A):

    n = len(A)
    sumA = A[0]
    minA = A[0]
    for i in range(1, n):
        sumA += A[i]
        minA = min(minA, A[i])

    B = []
    for i in range(n):
        if abs(n * A[i] - sumA) < n * minA:
            B.append(A[i])

    return B
