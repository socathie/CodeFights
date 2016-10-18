def typeaheadSearch(q):
    db = []
    sol = []
    i = 0
    while q != []:
        while q[0][0]=="ADD":
            db.append([q[0][2],float(q[0][3]),q[0][4].lower(),i])
            i += 1
            del q[0]
            if q==[]:
                break
        if q==[]:
            break
        db = sorted(db,key = lambda x: (-x[1],-x[3]))
        while q[0][0]=="QUERY":
            sol.append([])
            limit = int(q[0][1])
            if limit==0:
                del q[0]
                break
            s = q[0][2].lower()
            s = s.split(" ")
            for d in db:
                match = True
                for k in s:
                    if k not in d[2]:
                        match = False
                print sol
                if match:
                    sol[-1].append(d[0])
                    limit -= 1
                    if limit==0:
                        break
            del q[0]
            if q==[]:
                break
                
        if q==[]:
            break
            
        while q[0][0]=="DEL":
            for i in range(len(db)):
                if q[0][1] == db[i][0]:
                    del db[i]
                    break
            del q[0]
            if q==[]:
                break
    return sol
