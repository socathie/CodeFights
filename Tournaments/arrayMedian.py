def arrayMedian(sequence):
    n = len(sequence)
    sequence.sort()

    if (n % 2 == 0):
        return (sequence[n / 2] + sequence[n / 2 - 1]) / 2.0
    else:
        return sequence[(n - 1) / 2]
