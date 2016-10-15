def truncateString(s):
    while s!="" and (int(s[0])%3==0 or int(s[-1])%3==0 or (int(s[0])+int(s[-1]))%3==0):
        if int(s[0])%3==0:
            s = s[1:]
        elif int(s[-1])%3==0:
            s = s[:-1]
        elif (int(s[0])+int(s[-1]))%3==0:
            s = s[1:-1]
    return s
