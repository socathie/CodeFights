def boxesPacking(length, width, height):
    n = len(length)
    p = []
    for i in range(n):
        p.append(i)

    def comparator(p1, p2):
        vol1 = length[p1] * width[p1] * height[p1]
        vol2 = length[p2] * width[p2] * height[p2]
        return vol1 - vol2

    p = sorted(p, cmp=comparator)

    isCorrectSequence = True
    for i in range(n - 1):
        pi = p[i]
        pj = p[i + 1]
        canSwap = False
        canSwap |= (length[pi] < length[pj] and
                    width[pi] < width[pj] and
                    height[pi] < height[pj])
        canSwap |= (length[pi] < length[pj] and
                    width[pi] < height[pj] and
                    height[pi] < width[pj])
        canSwap |= (length[pi] < width[pj] and
                    width[pi] < length[pj] and
                    height[pi] < height[pj])
        canSwap |= (length[pi] < width[pj] and
                    width[pi] < height[pj] and
                    height[pi] < length[pj])
        ...
        canSwap |= (length[pi] < height[pj] and
                    width[pi] < width[pj] and
                    height[pi] < length[pj])
        isCorrectSequence &= canSwap
    return isCorrectSequence
