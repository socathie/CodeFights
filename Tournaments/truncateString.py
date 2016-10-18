def truncateString(s):
    while s!="" and (int(s[0])%3==0 or int(s[-1])%3==0 or (int(s[0])+int(s[-1]))%3==0):
        if int(s[0])%3==0:
            s = s[1:]
        elif int(s[-1])%3==0:
            s = s[:-1]
        elif (int(s[0])+int(s[-1]))%3==0:
            s = s[1:-1]
    return s

##########

def truncateString(s):

    def truncate(l, r):
        if l >= r:
            return ''
        newL = l
        newR = r
        left = ord(s[l]) - ord('0')
        right = ord(s[r - 1]) - ord('0')
        if left % 3 == 0:
            newL += 1
        elif right % 3 == 0:
            newR -= 1
        elif (left + right) % 3 == 0:
            newL += 1
            newR -= 1
        else:
            return s[l : r]

        return truncate(newL, newR)

    return truncate(0, len(s))
