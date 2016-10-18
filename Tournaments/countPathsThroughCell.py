def countPathsThroughCell(n, m, x, y):
    ##
    # List dp is used to store dynamic programming values.
    ##
    dp = []
    for i in range(n + 1):
        line = []
        for j in range(m + 1):
            line.append(0)
        dp.append(line)

    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            dp[i + 1][j] += dp[i][j] 
            dp[i][j + 1] += dp[i][j]

    return dp[x][y] * dp[n - 1 - x][m - 1 - y]
