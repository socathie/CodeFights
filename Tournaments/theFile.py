def theFile(version1, version2):

    len1 = len(version1)
    len2 = len(version2)
    maxLen = []
    take = []
    maxLen.append([0] * (len2 + 1))
    take.append([False] * (len2 + 1))
    for i in range(1, len1 + 1):
        maxLen.append([0] * (len2 + 1))
        take.append([False] * (len2 + 1))
        for j in range(1, len2 + 1):
            if version1[i - 1] == version2[j - 1]:
                maxLen[i][j] = maxLen[i - 1][j - 1] + 1
                take[i][j] = True
            else:
                maxLen[i][j] = max(maxLen[i - 1][j], maxLen[i][j - 1])
    answer = []
    i = len1
    j = len2
    while i > 0 and j > 0:
        if take[i][j]:
            i -= 1
            j -= 1
            answer.append(version1[i])
        else:
            if maxLen[i - 1][j] > maxLen[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return ''.join(list(reversed(answer)))
