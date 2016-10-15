def christmasTree(levelNum, levelHeight):
    def makeLine(spaces, asterisks):
        return ' ' * spaces + '*' * asterisks

    maxSpaces = levelNum + levelHeight
    indent = levelHeight - 2
    res = [makeLine(maxSpaces, 1),
           makeLine(maxSpaces, 1),
           makeLine(maxSpaces - 1, 3)]

    curSpaces = maxSpaces - 1
    curAsterisks = 3

    for i in range(levelNum):
        if i == 0:
            curAsterisks += 2
            curSpaces -= 1
        else:
            curAsterisks -= indent * 2
            curSpaces += indent
        res.append(makeLine(curSpaces, curAsterisks))

        for j in range(levelHeight - 1):
            curAsterisks += 2
            curSpaces -= 1
            res.append(makeLine(curSpaces, curAsterisks))

    curSpaces = maxSpaces - levelHeight / 2
    curAsterisks = levelHeight + 1 - levelHeight % 2
    for i in range(levelNum):
        res.append(makeLine(curSpaces, curAsterisks))

    return res
