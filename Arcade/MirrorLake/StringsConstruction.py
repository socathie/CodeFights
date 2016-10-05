#How many strings equal to A can be constructed using letters from the string B? Each letter can be used only once and in one string only.

#Example
#For A = "abc" and B = "abccba", the output should be
#stringsConstruction(A, B) = 2.
#We can construct 2 strings A with letters from B.

#Input/Output
#[time limit] 4000ms (py)

#[input] string A
#String to construct, A contains only lowercase English letters.
#Constraints:
#3 ≤ A.length ≤ 10.

#[input] string B
#String containing needed letters, B contains only lowercase English letters.
#Constraints:
#3 ≤ B.length ≤ 50.

#[output] integer

def stringsConstruction(A, B):
    time = 20
    for i in range(0,len(A)):
        time = min(time,B.count(A[i])/A.count(A[i]))
    
    return time
