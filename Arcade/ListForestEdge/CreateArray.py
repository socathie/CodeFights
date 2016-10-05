#Given an integer size, return array of length size filled with 1s.

#Example
#For size = 4, the output should be
#createArray(size) = [1, 1, 1, 1].

#Input/Output
#[time limit] 4000ms (py)

#[input] integer size
#A positive integer.
#Constraints:
#1 ≤ size ≤ 10.

#[output] array.integer

def createArray(size):
    a = []
    for x in range(0,size):
        a.append(1)
    return a
