#Remove a part of a given array between given indexes l and r (inclusive).

#Example
#For inputArray = [2, 3, 2, 3, 4, 5], l = 2 and r = 4, the output should be
#removeArrayPart(inputArray, l, r) = [2, 3, 5].

#Input/Output
#[time limit] 4000ms (py)

#[input] array.integer inputArray
#Constraints:
#2 ≤ inputArray.length ≤ 10,
#-10 ≤ inputArray[i] ≤ 10.

#[input] integer l
#Constraints:
#0 ≤ l ≤ r.

#[input] integer r
#Constraints:
#l ≤ r < inputArray.length.

def removeArrayPart(inputArray, l, r):
    return inputArray[0:l]+inputArray[r+1:]
