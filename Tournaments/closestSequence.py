def closestSequence(a, b):
    bestDiff = -1
    maskBound = 1 << len(b)

    for mask in range(maskBound):
        diff = 0
        curPos = 0
        for i in range(len(b)):
            if (mask & (1 << i)) != 0:
                diff += abs(b[i]-a[curPos]) 
                curPos += 1
                if curPos == len(a):
                    break
        if curPos == len(a) and (bestDiff == -1 or diff < bestDiff):
            bestDiff = diff

    return bestDiff
