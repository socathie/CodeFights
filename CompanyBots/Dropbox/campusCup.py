def campusCup(emails):
    schools = []
    scores = []
    for e in emails:
        e = e.split("@")[1]
        if e not in schools:
            schools.append(e)
            scores.append(20)
        else:
            scores[schools.index(e)] += 20
    
    five = []
    three = []
    two = []
    one = []
    none = []
    
    for i in range(len(schools)):
        if scores[i]>=500:
            five.append(schools[i])
        elif scores[i]>=300:
            three.append(schools[i])
        elif scores[i]>=200:
            two.append(schools[i])
        elif scores[i]>=100:
            one.append(schools[i])
        else:
            none.append(schools[i])
    five.sort()
    three.sort()
    two.sort()
    one.sort()
    none.sort()
    
    return five+three+two+one+none
