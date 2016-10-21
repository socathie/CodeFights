def evenDigitsOnly(n):

    if n == 0:
        return True
    if n % 2 != 0:
        return False
    return evenDigitsOnly(n//10)
