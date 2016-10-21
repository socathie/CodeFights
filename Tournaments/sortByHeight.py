def sortByHeight(a):
    for i in range(len(a)):
        minIndex = -1
        tmp = a[i]
        if a[i] == -1:
            continue
        for j in range(i,len(a)):
            if a[j] != -1:
                if minIndex == -1 or a[j] < a[minIndex]:
                    minIndex = j
        a[i] = a[minIndex]
        a[minIndex] = tmp
    return a
