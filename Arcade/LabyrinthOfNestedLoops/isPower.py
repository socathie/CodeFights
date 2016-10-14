def isPower(n):
    for a in range(0,int(pow(n,.5))+1):
        for b in range(0,int(math.log(n,2))+1):
            if pow(a,b) == n:
                return True
    
    return False

#Determine if the given number is a power of some non-negative integer.

#Example
#For n = 125, the output should be
#isPower(n) = true;
#For n = 72, the output should be
#isPower(n) = false.

#Input/Output
#[time limit] 4000ms (py)

#[input] integer n
#A positive integer.
#Constraints:
#1 ≤ n ≤ 350.

#[output] boolean
#true if n can be represented in the form ab (a to the power of b) where a and b are some non-negative integers and b ≥ 2, false otherwise.
