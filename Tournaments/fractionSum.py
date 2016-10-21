def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def fractionSum(A, B):
    d = A[1]*B[1]
    n = A[0]*B[1]+B[0]*A[1]
    g = gcd(d,n)
    return [n/g,d/g]
