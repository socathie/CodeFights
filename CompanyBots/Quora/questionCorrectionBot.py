def questionCorrectionBot(q):
    while q[0]==" ":
        q = q[1:]
    while q[-1]==" ":
        q = q[:-1]
    q = re.sub(r" +"," ",q)
    q = re.sub(r" *, *",", ",q)
    while q[len(q)-2]=="?":
        q = q[:-1]
    q = q[0].upper()+q[1:]
    if q[-1]!="?":
        q += "?"
    return q
