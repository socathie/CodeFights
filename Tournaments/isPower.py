def isPower(n):

    if n == 1:
        return True

    for i in range(2, n):
        if n % i == 0:
            tmp = n
            while n % i == 0:
                n /= i
            if n == 1:
                return  True 
            n = tmp
    return False
