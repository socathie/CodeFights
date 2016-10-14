def maximumSum(A, Q):
    A.sort()
    b = [0]*len(A)
    for q in Q:
        for i in range(q[0],q[1]+1):
            b[i] += 1
    b.sort()
    sol = 0
    for i in range(len(A)):
        sol += A[i]*b[i]
    return sol

'''You are given an array of integers A. Range sum query is defined by a pair of non-negative integers L and R (L <= R). An output to a range sum query on the given array is the sum of all elements of A with indices from L to R inclusive.

Find an algorithm that given a list of range sum queries can rearrange the array A in such a way that the total sum of all of the query outputs is maximized.

Example

For A = [2, 1, 2] and Q = [[0, 1]], the output should be
maximumSum(A, Q) = 4.

Input/Output

[time limit] 4000ms (py)
[input] array.integer A

An initial array.

Constraints:
2 ≤ A.length ≤ 10,
1 ≤ A[i] ≤ 10.

[input] array.array.integer Q

Array of range sum queries, each query is an array of two non-negative integers.

Constraints:
1 ≤ Q.length ≤ 10,
0 ≤ Q[i][j] ≤ 10.

[output] integer

Maximum possible total sum of the given range sum query outputs.'''
