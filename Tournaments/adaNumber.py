def adaNumber(line):
    atLeastOneDigit = False
    if line[len(line) - 1] == '#':
        i = 0
        base = 0
        while line[i] != '#' and base <= 16:
            if line[i] != '_':
                if '0' <= line[i] and line[i] <= '9':
                    base = base * 10 + ord(line[i]) - ord('0')
                else:
                    return False
            i += 1
        if base < 2 or base > 16:
            return False
        i += 1
        while i < len(line) - 1:
            if line[i] != '_':
                digit = -1
                if 'a' <= line[i] and line[i] <= 'f':
                    digit = ord(line[i]) - ord('a') + 10
                if 'A' <= line[i] and line[i] <= 'F':
                    digit = ord(line[i]) - ord('A') + 10
                if '0' <= line[i] and line[i] <= '9':
                    digit = ord(line[i]) - ord('0')
                if 0 <= digit and digit < base:
                    atLeastOneDigit = True
                else:
                    return False
            i += 1
    else:
        for i in range(len(line)):
            if line[i] != '_':
                if '0' <= line[i] and line[i] <= '9':
                    atLeastOneDigit = True
                else:
                    return False
    return atLeastOneDigit
