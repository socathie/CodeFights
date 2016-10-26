def divNumber(k, l, r):

    ans = 0
    for i in range(l, r + 1):
        n = i
        divs = 1
        j = 2
        while j * j <= n:
            pow_ = 0
            while n % j == 0:
                n /= j
                pow_ += 1
            divs *= pow_ + 1 
            if divs > k:
                break
            j += 1
        if n > 1:
            divs *= 2
        if divs == k:
            ans += 1

    return ans
