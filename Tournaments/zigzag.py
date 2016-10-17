def zigzag(a):

    best = 1
    left = 0
    while left < len(a):
        right = left + 1
        while right < len(a):
            if right == left + 1:
                if a[left] == a[right]:
                    break

            else:
                if ((a[right - 1] - a[right - 2]) *
                    (a[right - 1] - a[right]) <= 0):
                    break
            right += 1
        best = max(best, right - left + 1)
        left = right
        if left < len(a) and a[left - 1] != a[left]:
            left -= 1

    return best-1
