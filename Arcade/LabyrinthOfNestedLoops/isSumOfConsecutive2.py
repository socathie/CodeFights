def isSumOfConsecutive2(n):
    way = 0
    for i in range(1,n//2+1):
        temp = 0
        j = i
        while temp < n:
            temp += j
            j += 1
        if temp == n:
            way += 1
    
    return way

'''Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
isSumOfConsecutive2(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
isSumOfConsecutive2(n) = 0.

There are no ways to represent n = 8.

Input/Output

[time limit] 4000ms (py)
[input] integer n

A positive integer.

Constraints:
1 ≤ n ≤ 25.

[output] integer'''
