def sequencePeakElement(sequence):
    left = 1
    right = len(sequence) - 2
    while left < right:
        middle = (left + right) / 2
        if sequence[middle] > max(sequence[middle - 1], sequence[middle + 1]):
            left = right = middle
            break
        if sequence[middle - 1] < sequence[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return sequence[left]
