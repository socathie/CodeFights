def perfectCity(s,f):
    if int(s[1])==s[1]:
        x = math.ceil(min(s[0],f[0]))
        y = math.floor(max(s[0],f[0]))
        return abs(s[1]-f[1])+min(abs(x-s[0])+abs(x-f[0]),abs(y-s[0])+abs(y-f[0]))
    else:
        x = math.ceil(min(s[1],f[1]))
        y = math.floor(max(s[1],f[1]))
        return abs(s[0]-f[0])+min(abs(x-s[1])+abs(x-f[1]),abs(y-s[1])+abs(y-f[1]))
