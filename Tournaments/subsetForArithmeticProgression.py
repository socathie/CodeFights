def subsetForArithmeticProgression(inputArray):

    result = 1

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            dif = abs(inputArray[i] - inputArray[j])
            divisor = 1
            while divisor * divisor <= dif:
                if dif % divisor == 0:
                    cnt = 0
                    pair_divisor = dif / divisor

                    if divisor > 1:
                        for k in range(len(inputArray)):
                            if abs(inputArray[i] - inputArray[k]) % divisor == 0:
                                cnt += 1
                        result = max(result, cnt)

                    cnt = 0
                    if pair_divisor > 1:
                        for k in range(len(inputArray)):
                            if abs(inputArray[i] - inputArray[k]) % pair_divisor == 0:
                                cnt += 1
                        result = max(result, cnt)
                divisor += 1

    return result
