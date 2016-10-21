def digitalSumSort(a):

    def digitalSum(n):
        digitalSumValue = 0
        while n > 0:
            digitalSumValue += n%10
            n//=10
        return digitalSumValue

    buckets = dict()
    for i in range(len(a)):
        digitalSumValue = digitalSum(a[i])
        if digitalSumValue not in buckets:
            buckets[digitalSumValue] = []
        buckets[digitalSumValue].append(a[i])

    b = []
    for digitalSumValue in sorted(buckets):
        bucket = buckets[digitalSumValue]
        bucket.sort()
        for i in range(len(bucket)):
            b.append(bucket[i])

    return b
