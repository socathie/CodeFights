def fractionMultiplication(A, B):

    def gcdEuclid(a, b):
        if a == 0:
            return b
        return gcdEuclid(b % a, a)

    C = [A[0] * B[0], A[1] * B[1]]
    gcd = gcdEuclid(C[0], C[1])

    C[0] /= gcd
    C[1] /= gcd

    return C
