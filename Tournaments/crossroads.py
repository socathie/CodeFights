def crossroads(road1, road2, crossTime):
    j = 0
    for i in range(len(road1)):
        while j < len(road2) and road2[j] < road1[i]:
            if road2[j] + crossTime > road1[i]:
                return True
            j += 1
        if j < len(road2) and road1[i] + crossTime > road2[j]:
            return True
    return False
