def arrayEqualization(a, k):

    best = len(a)

    for i in range(len(a)):
        x = a[i]
        ans = 0
        cur = -1
        for j in range(len(a)):
            if cur == -1 and a[j] != x:
                cur = 0
            if cur >= 0:
                cur += 1
            if cur == k or cur >= 0 and j == len(a) - 1:
                ans += 1
                cur = -1
        best = min(best, ans)

    return best
