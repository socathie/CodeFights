#Given some substring of a cyclic string s, find the length of the smallest possible string that can be concatenated to itself many times to obtain s.

#Example
#For s = "cabca", the output should be
#cyclicString(s) = 3.

#Input/Output
#[time limit] 4000ms (py)

#[input] string s
#Constraints:
#3 ≤ s.length ≤ 15.

#[output] integer

def cyclicString(s):
    lenS = len(s)
    for i in range(0,lenS):
        sub = s[0:i+1]
        times = lenS//(i+1)+1
        if s in sub*times:
            return i+1
