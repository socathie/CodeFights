def numberOfTriangles2(sticks):
    cnt = 0
    sticks = sorted(sticks,reverse = True)
    for i in range(len(sticks)):
        for j in range(i+1,len(sticks)):
            for k in range(j+1,len(sticks)):
                if sticks[k]+sticks[j]>sticks[i]:
                    cnt += 1

    return cnt
