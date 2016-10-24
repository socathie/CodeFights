def findHeapPredicate(heap):

    allGreater, allLess = True, True
    i = 0
    while 2 * i + 1 < len(heap):
        sign1 = heap[i] - heap[2 * i + 1]
        sign2 = 0
        if 2 * i + 2 < len(heap):
            sign2 = heap[i] - heap[2 * i + 2]
        allGreater = allGreater and sign1 >= 0 and sign2 >= 0
        allLess = allLess and sign1 <= 0 and sign2 <= 0
        i += 1

    if allGreater and allLess:
        return '?'
    elif allGreater:
        return '>='
    elif allLess:
        return '<='
    else:
        return '!'
