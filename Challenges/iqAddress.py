def iqAddress(n):
    r = ""
    n=float(n)
    while n!=1:
        r = str(n%10.5) + r
        n = math.ceil(n/2)
    return "1"+r
    

'''Have you ever heard of an IQ-address? For the given integer n, it is calculated as follows:

Let result = "".
If n = 1, prepend "1" to the beginning of result and return it as an answer.
Prepend n % 10.5 to the beginning of result.
Divide n by 2 with rounding up to the nearest integer.
Go to step 2.
Given an integer n, your task is to return IQ-address generated from it.

Example

For n = 21, the output should be
iqAddress(n) = "12.03.06.00.50.0".

Here's why:

21% 10.5 = 0.0
11% 10.5 = 0.5
6 % 10.5 = 6.0
3 % 10.5 = 3.0
2 % 10.5 = 2.0
Thus, the answer is "1"+"2.0"+"3.0"+"6.0"+"0.5"+"0.0" = "12.03.06.00.50.0".

Input/Output

[time limit] 4000ms (py)
[input] integer n

Constraints:
0 ≤ n ≤ 105.

[output] string

The IQ-address generated from n.'''
