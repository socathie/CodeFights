def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def numberOfPairsForLCM(value):
    cnt = 0
    for a in range(1,value+1):
        for b in range(a,value+1):
            if a*b/gcd(a,b)==value:
                cnt += 1
    return cnt
                
