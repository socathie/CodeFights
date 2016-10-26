def makeArrayConsecutive(sequence):

    answer = []
    current_position = 0

    sequence.sort()
    for i in range(sequence[0], sequence[len(sequence) - 1]):
        if sequence[current_position] != i:
            answer.append(i)
        else:
            current_position += 1

    return answer
