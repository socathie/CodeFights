def fareySequence(n, m):

    class Fraction:
        a = None
        b = None

        def __init__(self, a, b):
            self.a = a
            self.b = b


        def isReduced(self):
            return self.gcd(self.a, self.b) == 1

        def gcd(self, a, b):
            return b if a == 0 else self.gcd(b % a, a)

        # method used for sorting ('less than')
        def __lt__(self, f):
            return self.a * f.b < self.b * f.a

        def toString(self):
            return str(self.a) + '/' + str(self.b)


    fractions = []
    for i in range(1, n + 1):
        for j in range(i + 1):
            f = Fraction(j, i)
            if f.isReduced():
                fractions.append(f)

    fractions.sort()
    return fractions[m - 1].toString()
