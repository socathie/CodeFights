def largestNumber(n):
    temp = 0
    for x in range(0,n):
        temp += 9*pow(10,x)
    return temp
