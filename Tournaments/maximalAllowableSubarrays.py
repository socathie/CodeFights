def maximalAllowableSubarrays(inputArray, maxSum):
    sol = []
    for i in range(len(inputArray)):
        j = i
        while sum(inputArray[i:j+1])<=maxSum and j<len(inputArray):
            j += 1
        sol.append(j-1)
    return sol
