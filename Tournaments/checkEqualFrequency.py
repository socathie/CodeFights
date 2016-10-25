def checkEqualFrequency(inputArray):
    temp = list(set(inputArray))
    cnt = inputArray.count(temp[0])
    for i in range(1,len(temp)):
        if inputArray.count(temp[i]) != cnt:
            return False
    return True
