def sumBelowBound(bound):

    left = 0
    right = bound + 1
    while right - left > 1:
        middle = (left + right) / 2
        if middle * (middle + 1) / 2 <= bound:
            left = middle
        else:
            right = middle

    return left
