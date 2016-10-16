def i(x):
    if x=="-"or x=="" or x=="+":
        return int(x+"1")
    else:
        return int(x)

def EquationCaptcha(q):
    r = re.match(r"((-*\d*)x([+-]\d+)=(-*\d+)|(-*\d+)([+-]\d*)x=(-*\d+)|(-*\d+)=(-*\d*)x([+-]\d+)|(-*\d+)=(-*\d+)([+-]\d*)x)",q)
    for j in range(4):
        if r.group(3*j+2) is not None:
            r = [i(r.group(3*j+2)),i(r.group(3*j+3)),i(r.group(3*j+4))]
            if j==0:
                return (r[2]-r[1])/r[0]
            if j==1:
                return (r[2]-r[0])/r[1]
            if j==2:
                return (r[0]-r[2])/r[1]
    return (r[0]-r[1])/r[2]
