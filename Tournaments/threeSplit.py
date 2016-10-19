def threeSplit(a):

    need = 0
    for x in a:
        need += x
    need /= 3

    ans = 0
    firstPoints = 0
    curSum = 0
    for i in range(0, len(a) - 1):
        curSum += a[i]
        if curSum == need:
            firstPoints += 1
        if curSum == 2 * need:
            ans += firstPoints
            if need == 0:
                ans -= 1

    return ans
