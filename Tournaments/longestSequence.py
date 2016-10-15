def longestSequence(A):

    best = 1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            diff = A[j] - A[i]
            if diff == 0:
                continue
            cur = 1
            last = A[i]
            for k in range(j, len(A)):
                if A[k] - last == diff:
                    cur += 1
                    last = A[k]
            if cur > best:
                best = cur

    return best

