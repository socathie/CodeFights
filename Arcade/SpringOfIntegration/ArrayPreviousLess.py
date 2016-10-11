#Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.

#Example
#For items = [3, 5, 2, 4, 5], the output should be
#arrayPreviousLess(items) = [-1, 3, -1, 2, 4].

#Input/Output
#[time limit] 4000ms (py)

#[input] array.integer items
#Non-empty array of positive integers.
#Constraints:
#3 ≤ items.length ≤ 15,
#1 ≤ items[i] ≤ 200.

#[output] array.integer
#Array containing answer values computed as described above.

def arrayPreviousLess(items):
    array = []
    for i in range(0,len(items)):
        pos = -1
        for j in range(0,i):
            if items[j]<items[i]:
                pos = j
        if pos == -1:
            array.append(-1)
        else:
            array.append(items[pos])
    return array
