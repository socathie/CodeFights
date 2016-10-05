#Given an integer n, find the minimal k such that

#k = m! (where m! = 1 * 2 * ... * m) for some integer m;
#k >= n.
#In other words, find the smallest factorial which is not less than n.

#Example
#For n = 17, the output should be
#leastFactorial(n) = 24.

#(17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

#Input/Output
#[time limit] 4000ms (py)

#[input] integer n
#A positive integer.
#Constraints:
#1 ≤ n ≤ 120.

#[output] integer

def leastFactorial(n):
    k = 1
    i = 2
    while k<n:
        k *= i
        i += 1
    return k
