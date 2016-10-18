def textJustification(words, L):

    text = []
    currentWord = 0

    while currentWord < len(words):
        left = currentWord
        right = left
        currentSum = len(words[left])

        while right + 1 < len(words) and currentSum + len(words[right + 1]) + 1 <= L:
            currentSum += len(words[right + 1]) + 1
            right += 1

        if left == right:
            line = words[left]
            for i in range(L - len(words[left])):
                line += ' '
            text.append(line)
        else:
            freeSpace = L - currentSum
            minimalSpaceLen = 1 + freeSpace / (right - left)
            extraSpaces = freeSpace % (right - left)
            minimalSpace = ''
            for i in range(minimalSpaceLen):
                minimalSpace += ' '

            line = ''
            for i in range(left, right):
                line += words[i] + minimalSpace
                if extraSpaces > 0:
                    line += ' '
                    extraSpaces -= 1

            text.append(line + words[right])
        currentWord = right + 1

    return text
