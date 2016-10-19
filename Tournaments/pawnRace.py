def pawnRace(white, black, toMove):
    wHor = ord(white[1]) - ord('0')
    wVert = ord(white[0]) - ord('a')
    bHor = ord(black[1]) - ord('0')
    bVert = ord(black[0]) - ord('a')
    if wVert == bVert and wHor < bHor:
        return 'draw'
    if abs(wVert - bVert) != 1 or wHor >= bHor:
        wRest = min(8 - wHor, 5)
        bRest = min(bHor - 1, 5)
        if wRest < bRest or wRest == bRest and toMove == 'w':
            return 'white'
        return 'black'
    winningPairs = [[2, 5], [2, 6], [3, 6], [4, 7]]
    if toMove == 'w':
        for i in range(4):
            if wHor == winningPairs[i][0] and bHor == winningPairs[i][1]:
                return 'white'
        if wHor + 1 == bHor:
            return 'white'
        return 'black'
    else:
        for i in range(4):
            if wHor == 9 - winningPairs[i][1] and bHor == 9 - winningPairs[i][0]:
                return 'black'
        if wHor + 1 == bHor:
            return 'black'
        return 'white'
