def kikCode(userId):
    if userId == "0":
        return []
    userId = "{0:b}".format(int(userId))
    userId = "0"*max(0,52-len(userId)) + userId
    userId = userId[::-1]
    userId = [userId[:3],userId[3:7],userId[7:15],userId[15:25],userId[25:37],userId[37:]]
    print userId
    code = []
    for i in range(6):
        line = []
        numSeg = len(userId[i])
        deg = 360/numSeg
        for j in range(numSeg):
            if userId[i][j]=="1":
                if (i+1,j*deg) not in line:
                    line.append((i+1,j*deg))
                else:
                    line = line[:-1]
                line.append((i+1,(j+1)*deg))
        if len(line)>2 and (i+1,0) in line and (i+1,360) in line:
            temp = line[1][1]
            line = line[2:-1]
            line.insert(0,(i+1,temp+360))
        line.sort()
        for i in range(0,len(line),2):
            code.append([list(line[i]),list(line[i+1])])
        
    return code
                
