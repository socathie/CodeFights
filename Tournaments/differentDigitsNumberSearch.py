def differentDigitsNumberSearch(inputArray):

    for i in range(len(inputArray)):
        cur = inputArray[i]
        was = [False] * 10
        ok = True
        while cur > 0:
            if was[cur % 10]:
                ok = False
                break
            was[cur % 10] = True
            cur /= 10
        if ok:
            return inputArray[i]

    return -1
