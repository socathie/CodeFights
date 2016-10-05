#Given an array of integers, we need to find the number of "holes" that need to be filled such that it contains all the integers from some range.

#Example
#For sequence = [6, 2, 3, 8], the output should be
#makeArrayConsecutive2(sequence) = 3.
#We need to add in 4, 5 and 7.

#Input/Output
#[time limit] 4000ms (py)

#[input] array.integer sequence
#An array of distinct integers.
#Constraints:
#1 ≤ sequence.length ≤ 10,
#-10 ≤ sequence[i] ≤ 10.

#[output] integer
#The minimal number of integers that need to be added to sequence such that it contains every integer from an interval [L, R] (for some L, R) and no other integers.

def makeArrayConsecutive2(sequence):
    minimum = min(sequence)
    maximum = max(sequence)
    size = len(sequence)
    return maximum-minimum-size+1
