def optimalStockBasket(stocks, riskBudget):
    for i in reversed(range(len(stocks))):
        if stocks[i][0]<=0:
            del stocks[i]
    
    dp = [0 for col in range(riskBudget+1)]
    port = [[] for col in range(riskBudget+1)]
    dp[0] = 0
    
    for i in range(1,riskBudget+1):
        m = []
        temp = []
        for j in stocks:
            if j[1]<=i and j not in port[i-j[1]]:
                m.append(dp[i-j[1]]+j[0])
                temp.append(j)
        if m !=[]:
            dp[i] = max(m)
            j = m.index(max(m))
            port[i] = port[i-temp[j][1]]+[temp[j]]
        else:
            dp[i]=0
            port[i] = []
    print port
    return dp[riskBudget]
