def splitByValue(k, elements):
    less = []
    more = []
    for e in elements:
        if e<k:
            less.append(e)
        else:
            more.append(e)
    return less+more
