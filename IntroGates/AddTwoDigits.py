#You are given a two-digit integer n. Return the sum of its digits.
#Example
#For n = 29, the output should be
#addTwoDigits(n) = 11.
#Input/Output
#[time limit] 4000ms (py)
#[input] integer n
#A positive two-digit integer.
#Constraints:
#10 ≤ n ≤ 99.
#[output] integer
#The sum of the first and second digits of the input number.

def addTwoDigits(n):
    d1 = n%10
    d2 = (n-d1)/10
    return d1+d2
