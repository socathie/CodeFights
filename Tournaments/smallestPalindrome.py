def smallestPalindrome(s0):

    s = list(s0)

    i = len(s) / 2
    while i < len(s) and s[i] == s[len(s) - i - 1]:
        i += 1
    if i == len(s):
        return s0

    if s[i] < s[len(s) - 1 - i]:
        while i < len(s):
            s[i] = s[len(s) - i - 1]
            i += 1
        return ''.join(s)
    else:
        i = (len(s) - 1) / 2
        while s[i] == 'z':
            i -= 1
        s[i] = chr(ord(s[i]) + 1)
        i += 1
        while 2 * i < len(s):
            s[i] = 'a'
            i += 1
        while i < len(s):
            s[i] = s[len(s) - i - 1]
            i += 1
        return ''.join(s)
