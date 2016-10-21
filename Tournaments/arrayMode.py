def arrayMode(sequence):
    count = []
    answer = 0

    for i in range(0, 10):
        count.append(0)
    for i in range(len(sequence)):
        count[sequence[i] - 1] += 1
        if count[sequence[i] - 1] > count[answer]:
            answer = sequence[i] - 1
    return answer + 1
