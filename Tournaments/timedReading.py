def timedReading(maxLength, text):
    count = 0
    i = 0
    while i < len(text):
        lengthOfWord = 0
        while i < len(text) and text[i].isalpha():
            lengthOfWord += 1
            i += 1
        if 0 < lengthOfWord <= maxLength:
            count += 1
        i += 1
    return count
