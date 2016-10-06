#You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of the pieces after cutting. How many ways can you do it?

#It is guaranteed that the sum of all elements in the array is divisible by 3.

#Example
#For a = [0, -1, 0, -1, 0, -1], the output should be
#threeSplit(a) = 4.

#Input/Output
#[time limit] 4000ms (py)

#[input] array.integer a
#Constraints:
#5 ≤ a.length ≤ 104,
#-108 ≤ a[i] ≤ 108.

#[output] integer
#It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.

def threeSplit(a):
    goal = sum(a)/3
    ways = 0
    sum1 = 0
    for i in range(1,len(a)-1):
        sum1 += a[i-1]
        if sum1==goal:
            sum2 = sum(a[i:])
            for j in range(i+1,len(a)):
                sum2 -= a[j-1]
                if sum2==goal:
                    ways+=1
    return ways
