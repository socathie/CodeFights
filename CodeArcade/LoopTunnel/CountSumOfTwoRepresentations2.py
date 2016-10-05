'''Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2 and r = 4, the output should be
countSumOfTwoRepresentations2(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

Input/Output

[time limit] 4000ms (py)
[input] integer n

A positive integer.

Constraints:
5 ≤ n ≤ 10^9.

[input] integer l

A positive integer.

Constraints:
1 ≤ l ≤ r.

[input] integer r

A positive integer.

Constraints:
l ≤ r ≤ 10^9,
l - r ≤ 10^6.

[output] integer'''

def countSumOfTwoRepresentations2(n, l, r):
    temp = 0
    if l <= n//2 <= r:
        if n%2 == 0:
            return min([(n//2-l)+1,(r-n//2)+1])
        else:
            return min([(n//2-l),(r-n//2)])
    else:
        return 0
