#Given an array of 2k integers (for some integer k), perform the following operations until the array contains only one element:

#On the 1st, 3rd, 5th, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
#On the 2nd, 4th, 6th, etc. iterations replace each pair of consecutive elements with their product.
#After the algorithm has finished, there will be a single element left in the array. Return that element.

#Example
#For inputArray = [1, 2, 3, 4, 5, 6, 7, 8], the output should be
#arrayConversion(inputArray) = 186.
#We have [1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186], so the answer is 186.

#Input/Output
#[time limit] 4000ms (py)

#[input] array.integer inputArray
#Constraints:
#1 ≤ inputArray.length ≤ 20,
#-9 ≤ inputArray[i] ≤ 99.

#[output] integer

def arrayConversion(inputArray):
    k = int(math.log(len(inputArray),2))
    for i in range(0,k):
        newArray = []
        if i%2==0:
            for j in range(0,len(inputArray),2):
                newArray.append(inputArray[j]+inputArray[j+1])
        else:
            for j in range(0,len(inputArray),2):
                newArray.append(inputArray[j]*inputArray[j+1])
        inputArray = newArray
    
    return inputArray[0]
