def closestSequence3(a, b):

    def recursiveSearch(posA, posB, diff):
        if posA == len(a):
            return diff
        if posB == len(b):
            return float('inf')
        return min(recursiveSearch(posA, posB + 1, diff),
                   recursiveSearch(posA + 1, posB + 1,
                                   diff + abs(a[posA] - b[posB])))

    return recursiveSearch(0, 0, 0)
