def arrayPacking(a):

    res = 0
    for i in range(len(a)):
        res |= a[i] << i*8

    return res
