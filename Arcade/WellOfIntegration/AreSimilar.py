def areSimilar(A, B):
    if A==B:
        return True
    i = 0
    while i<len(A):
        if A[i]==B[i]:
            A.pop(i)
            B.pop(i)
        else:
            i += 1
    if len(A)!=2:
        return False
    B.reverse()
    if A==B:
        return True
    else:
        return False

'''Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements.

Given two arrays, check whether they are similar.

Example

For A = [1, 2, 3] and B = [1, 2, 3], the output should be
areSimilar(A, B) = true;
For A = [1, 2, 3] and B = [2, 1, 3], the output should be
areSimilar(A, B) = true;
For A = [1, 2, 2] and B = [2, 1, 1], the output should be
areSimilar(A, B) = false.
Input/Output

[time limit] 4000ms (py)
[input] array.integer A

Array of integers.

Constraints:
3 ≤ A.length ≤ 105,
1 ≤ A[i] ≤ 1000.

[input] array.integer B

Array of integers of the same length as A.

Constraints:
B.length = A.length,
1 ≤ B[i] ≤ 1000.

[output] boolean

true if A and B are similar, false otherwise.'''

def areSimilar(A, B):
    if A==B:
        return True
    
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            if A == B:
                return True
            A[j] = A[i]
            A[i] = temp
            
    return False
