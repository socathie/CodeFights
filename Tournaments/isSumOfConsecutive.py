def isSumOfConsecutive(n):
    for i in reversed(range(n//2+1)):
        s = 0
        for j in reversed(range(i+1)):
            s += j
            if s==n:
                return True
    return False
