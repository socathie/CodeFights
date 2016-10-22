def specialNumbers(l, r):

    ans = 0
    for i in range(l, r + 1):
        digits = str(i)
        ok = True
        for j in range((len(digits) + 1) / 2):
            if digits[j] == '6' or digits[j] == '9':
                ok &= ord(digits[len(digits) - 1 - j]) == ord('9') - ord(digits[j]) + ord('6')
            elif digits[j] == '8' or digits[j] == '0':
                ok &= digits[j] == digits[len(digits) - 1 - j]
            else:
                ok = False
        if ok:
            ans += 1

    return ans
