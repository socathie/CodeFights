def findSquareSide(x, y):
    d = []
    for i in range(len(x)-1):
        d.append((y[i-1]-y[i])**2+(x[i-1]-x[i])**2)
    
    return min(d)
