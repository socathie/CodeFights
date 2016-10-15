def equationSolutions(L, R):

    result = 0
    for a in range(L, R + 1):
        b = min(a+1,L)
        while b <= R:
            if a * a * a == b * b:
                result += 1
            b += 1
    return result
