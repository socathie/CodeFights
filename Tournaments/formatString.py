def formatString(input):
    input = re.sub("\s+"," ",input)
    if input[0]==" ":
        input = input[1:]
    if input[-1]==" ":
        input = input[:-1]
    return input
