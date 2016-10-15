def multisetPermutations(multiset):

    factorials = [1]
    for i in range(1, len(multiset) + 1):
        factorials.append(factorials[i - 1] * i)

    multiset.sort()
    groups = [1]
    for i in range(1, len(multiset)):
        if multiset[i] == multiset[i - 1]:
            groups[len(groups) - 1] += 1
        else:
            groups.append(1)

    result = factorials[len(multiset)]
    for j in range(len(groups)):
        result /= factorials[groups[j]]

    return result
