def loadTimeEstimator(sizes, uploadingStart, V):
    if sizes ==[]:
        return []
    curSizes = []
    l = min(uploadingStart)
    r = max(uploadingStart)
    time = [0 for i in range(len(sizes))]
    for i in range(l,r+1):
        nonzero = [j for j in curSizes if j!=0]
        curSizes = [j-float(V)/len(nonzero) if j!=0 else 0 for j in curSizes]
        if curSizes!=[]:
            for j in range(len(curSizes)):
                if curSizes[j]<=0 and time[j]==0:
                    curSizes[j]=0
                    time[j]=i
        while uploadingStart!=[] and uploadingStart[0]==i:
            curSizes.append(sizes[0])
            del uploadingStart[0]
            del sizes[0]
    
    while True:
        i += 1
        nonzero = [j for j in curSizes if j!=0]
        if len(nonzero)==0:
            break
        curSizes = [j-float(V)/len(nonzero) if j!=0 else 0 for j in curSizes]
        if curSizes!=[]:
            for j in range(len(curSizes)):
                if curSizes[j]<=0 and time[j]==0:
                    curSizes[j]=0
                    time[j]=i
    return time
