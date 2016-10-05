#Define an integer's roundness as the number of trailing zeroes in it.

#Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

#Example
#For n = 902200100, the output should be
#increaseNumberRoundness(n) = true.

#For instance, one may swap the leftmost 0 with 1.

#For n = 11000, the output should be
#increaseNumberRoundness(n) = false.

#Input/Output
#[time limit] 4000ms (py)

#[input] integer n
#A positive integer.
#Constraints:
#100 ≤ n ≤ 109.

#[output] boolean
#true if it's possible to increase n's roundness, false otherwise.

def increaseNumberRoundness(n):
    while n%10==0:
        n //= 10
    
    temp = 1
    while n:
        temp *= n%10
        n//=10
    
    if temp ==0:
        return True
    else:
        return False
