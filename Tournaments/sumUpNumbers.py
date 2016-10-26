def sumUpNumbers(s):
    s = re.split("\D",s)
    s = [int(i) for i in s if i!=""]
    return sum(s)
