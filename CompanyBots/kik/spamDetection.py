def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def spamDetection(messages, spamSignals):
    output = []
    lenM = len(messages)
    #test 1
    cnt = 0
    for m in messages:
        if len(m[0].split(" "))<5:
            cnt+=1
    if float(cnt)>0.9*lenM:
        g = gcd(cnt,lenM)
        output.append("failed: "+str(cnt//g)+"/"+str(lenM//g))
    else:
        output.append("passed")
        
    #test 2
    users = list(set([m[1] for m in messages]))
    failed = []
    for u in users:
        msg = []
        for m in messages:
            if m[1]==u:
                msg.append(m[0])
        for m in msg:
            if len(msg)<2:
                break
            if 2*msg.count(m)>len(msg):
                failed.append(u)
    failed = sorted(list(set(failed)))
    if len(failed)>=1:
        line = "failed:"
        for f in failed:
            line += " "+str(f)
        output.append(line)
    else:
        output.append("passed")
        
    #test 3
    msg = [m[0] for m in messages]
    failed = "failed: "
    for m in msg:
        if len(msg)<2:
            break
        if 2*msg.count(m)>len(msg):
            failed += m
            break
    if failed != "failed: ":
        output.append(failed)
    else:
        output.append("passed")
    
    #test 4
    msg = [m.lower() for m in msg]
    msg = [re.split("\W",m) for m in msg]
    msg = [[j for j in m if j !=""] for m in msg]
    cnt = 0
    spam = []
    for m in msg:
        for i in m:
            if i in spamSignals:
                cnt += 1
                spam.append(i)
                break
    spam = sorted(list(set(spam)))
    if 2*float(cnt)>len(msg):
        failed = "failed:"
        for s in spam:
            failed += " "+s
        output.append(failed)
    else:
        output.append("passed")
        
    return output
