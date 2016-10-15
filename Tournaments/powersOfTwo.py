def powersOfTwo(n):

    ans = []
    cur = 1
    while n > 0:
        if n % 2 == 1:
            ans.append(cur)
        n >>= 1
        cur <<= 1

    return ans
