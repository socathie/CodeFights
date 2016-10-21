def prime(x):
    if x in [0, 1]:
        return False
    for n in xrange(2, int(x ** 0.5 + 1)):
        if x % n == 0:
            return False
    return True


def greatestCommonPrimeDivisor(a, b):
    g = -1
    for i in range(a+1):
        if prime(i) and b%i==a%i==0:
            g = i
    return g
