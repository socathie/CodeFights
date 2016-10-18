def subarrayCount(a, k):

    result = 0
    left = 0
    for i in range(len(a) + 1):
        if i == len(a) or a[i] <= k:
            result += (i - left) * (i - left + 1) / 2
            left = i + 1

    return result
