#dynamic programming

def closestSequence2(a, b):
    n = len(a)
    m = len(b)
    dp = [[0 for c in range(m)] for r in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i==0:
                dp[i][j]=abs(b[j]-a[0])
            elif j>i:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j-1]+abs(a[i]-b[j]))
            elif j==i:
                dp[i][j] = dp[i-1][j-1]+abs(a[i]-b[j])
    
    return dp[n-1][m-1]

'''The difference between two sequences of the same length a1, a2, a3,..., an and b1, b2, b3,..., bn can be defined as the sum of absolute differences between their respective elements:

diff(a, b) = |a1 - b1| + |a2 - b2| + ... + |an - bn|.

For the given sequences a and b (not necessarily having the same lengths) find a subsequence b' of b such that diff(a, b') is minimal. Return this difference.

Example

For a = [1, 2, 6] and b = [0, 1, 3, 4, 5], the output should be
closestSequence2(a, b) = 2.

The best subsequence will be b' = [1, 3, 5] which has a difference of 2 with a.

Input/Output

[time limit] 4000ms (py)
[input] array.integer a

Constraints:
3 ≤ a.length ≤ 1000,
-1000 ≤ a[i] ≤ 1000.

[input] array.integer b

Constraints:
a.length ≤ b.length ≤ 1000,
-1000 ≤ b[i] ≤ 1000.

[output] integer'''
