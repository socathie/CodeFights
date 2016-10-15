def mergeKArrays(arrays):
    firstUnused = []
    result = []
    n = 0
    for i in range(len(arrays)):
        firstUnused.append(0)
        n +=  arrays[i] 
    for i in range(n):
        minIndex = -1
        minValue = 0
        for j in range(len(arrays)):
            if firstUnused[j] < len(arrays[j]):
                if minIndex == -1 or minValue > arrays[j][firstUnused[j]]:
                    minIndex = j
                    minValue = arrays[j][firstUnused[j]]
        result.append(minValue)
        firstUnused[minIndex] += 1
    return result
