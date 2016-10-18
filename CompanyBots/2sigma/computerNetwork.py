def computerNetwork(n, network):
    if n == 1:
        return 0
    dp = [100000 for col in range(n)]
    
    dummy = list(network)
    network = []
    for i in range(len(dummy)):
        temp = sorted(dummy[i][:2])
        network.append([])
        network[i].append(temp[0])
        network[i].append(temp[1])
        network[i].append(dummy[i][2])
    network = sorted(network,key = lambda x: (x[0],x[1]))
    for i in range(n):
        for x in network:
            if x[1]==i+1 and x[0]==1:
                dp[i] = x[2]
                
    for i in range(n):
        m = dp[i]
        for j in range(i):
            for x in network:
                if x[1]==i+1 and x[0]==j+1:
                    m = min(m,dp[j]+x[2])
        dp[i] = m

    return dp[-1]
