def isLucky(n):

    digits = []
    sum = 0

    while (n > 0):
        digits.append(n % 10)
        n = n / 10

    for i in range(len(digits)):
        if i < len(digits) / 2:
            sum += digits[i]
        else:
            sum -= digits[i]

    if sum != 0:
        return False
    return True
