def firstOperationCharacter(expr):

    balance = 0
    maxAdditionPriority = -1
    maxMultiplicationPriority = -1
    additionIndex = -1
    multiplicationIndex = -1

    for i in range(len(expr)):
        if expr[i] == '(':
            balance += 1
        if expr[i] == ')':
            balance -= 1
        if expr[i] == '+':
            if balance > maxAdditionPriority:
                maxAdditionPriority = balance
                additionIndex = i
        if expr[i] == '*':
            if balance > maxMultiplicationPriority:
                maxMultiplicationPriority = balance
                multiplicationIndex = i

    if maxAdditionPriority > maxMultiplicationPriority:
        return additionIndex
    else:
        return multiplicationIndex
