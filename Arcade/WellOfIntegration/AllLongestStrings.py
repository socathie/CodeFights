#Given an array of strings, return another array containing all of its longest strings.

#Example
#For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
#allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

#Input/Output
#[time limit] 4000ms (py)

#[input] array.string inputArray
#A non-empty array.
#Constraints:
#1 ≤ inputArray.length ≤ 10,
#1 ≤ inputArray[i].length ≤ 10.

#[output] array.string
#Array of the longest strings, stored in the same order as in the inputArray.

def allLongestStrings(inputArray):
    maxLen = 0
    for i in range(0,len(inputArray)):
        maxLen = max(maxLen,len(inputArray[i]))
    
    return [i for i in inputArray if len(i)==maxLen]
