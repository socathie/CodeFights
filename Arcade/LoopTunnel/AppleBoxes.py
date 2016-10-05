#There're k square apple boxes full of apples. If a box is of size m, then it contains m × m apples. You noticed two interesting properties about the boxes:

#The smallest box is of size 1, the next one is of size 2,..., all the way up to size k.
#Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
#Your task is to calculate the difference between the number of red apples and the number of yellow apples.

#Example
#For k = 5, the output should be
#appleBoxes(k) = -15.

#There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, thus the answer is 20 - 35 = -15.

#Input/Output
#[time limit] 4000ms (py)

#[input] integer k
#A positive integer.
#Constraints:
#1 ≤ k ≤ 40.

#[output] integer
#The difference between the two types of apples.

def appleBoxes(k):
    red = 0
    yellow = 0
    for i in range(1,k+1):
        if i%2==0:
            red +=i*i
        else:
            yellow +=i*i
            
    return red-yellow
