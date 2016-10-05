#Given an integer n, return the largest number that contains exactly n digits.
#Example
#For n = 2, the output should be
#largestNumber(n) = 99.
#Input/Output
#[time limit] 4000ms (py)
#[input] integer n
#Constraints:
#1 ≤ n ≤ 7.
#[output] integer
#The largest integer of length n.

def largestNumber(n):
    temp = 0
    for x in range(0,n):
        temp += 9*pow(10,x)
    return temp
