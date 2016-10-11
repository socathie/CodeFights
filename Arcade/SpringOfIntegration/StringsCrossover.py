#Define crossover operation over two equal-length strings A and B as follows:
#the result of that operation is a string of the same length as the input strings
#result[i] is chosen at random between A[i] and B[i]
#Given array of strings inputArray and a string result, find for how many pairs of strings from inputArray the result of the crossover operation over them may be equal to result.

#Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot include the same element of the array twice (however, if there are two equal elements in the array, they can form a pair).

#Example
#For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output should be
#stringsCrossover(inputArray, result) = 2.

#Input/Output
#[time limit] 4000ms (py)

#[input] array.string inputArray
#A non-empty array of equal-length strings.
#Constraints:
#2 ≤ inputArray.length ≤ 10,
#1 ≤ inputArray[i].length ≤ 10.

#[input] string result
#A string of the same length as each of the inputArray elements.
#Constraints:
#result.length = inputArray[i].length.

#[output] integer

def stringsCrossover(inputArray, result):
    aLen = len(inputArray)
    sLen = len(result)
    pairs = 0
    for i in range(0,aLen):
        for j in range(i+1,aLen):
            crossover = True
            for k in range(0,sLen):
                if inputArray[i][k]!=result[k] and inputArray[j][k]!=result[k]:
                    crossover = False
                    break
            if crossover:
                pairs += 1
    return pairs
