'''You found two items in a treasure chest! The first item weights weight1 and is worth value1, and the second item weights weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Example

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 8, the output should be
knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

You can only carry the first item.

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 9, the output should be
knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

You're strong enough to take both of the items with you.

Input/Output

[time limit] 4000ms (py)
[input] integer value1

Constraints:
2 ≤ value1 ≤ 20.

[input] integer weight1

Constraints:
2 ≤ weight1 ≤ 5.

[input] integer value2

Constraints:
2 ≤ value2 ≤ 20.

[input] integer weight2

Constraints:
2 ≤ weight2 ≤ 5.

[input] integer maxW

Constraints:
1 ≤ maxW ≤ 20.

[output] integer'''

def knapsackLight(value1, weight1, value2, weight2, maxW):
    temp = 0
    if value1>value2:
        if weight1<maxW:
            temp += value1
            maxW -= weight1
        if weight2<maxW:
            temp += value2
    else:
        if weight2<maxW:
            temp += value2
            maxW -= weight2
        if weight1<=maxW:
            temp += value1
            
    return temp
