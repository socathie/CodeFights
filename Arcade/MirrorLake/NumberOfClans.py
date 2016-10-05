#Let's call two integers A and B friends if each integer from the array divisors is a divisor of both A and B or neither A nor B. If two integers are friends, they are said to be in the same clan. How many clans are the integers from 1 to k, inclusive, broken into?

#Example
#For divisors = [2, 3] and k = 6, the output should be
#numberOfClans(divisors, k) = 4.
#The numbers 1 and 5 are friends and form a clan, 2 and 4 are friends and form a clan, and 3 and 6 do not have friends and each is a clan by itself. So the numbers 1 through 6 are broken into 4 clans.

#Input/Output
#[time limit] 4000ms (py)

#[input] array.integer divisors
#A non-empty array of positive integers.
#Constraints:
#2 ≤ divisors.length < 10,
#1 ≤ divisors[i] ≤ 10.

#[input] integer k
#A positive integer.
#Constraints:
#5 ≤ k ≤ 10.

#[output] integer

def numberOfClans(divisors, k):
    clan = []
    for i in range(1,k+1):
        vec = []
        for j in range(0,len(divisors)):
            if i%divisors[j]==0:
                vec.append(1)
            else:
                vec.append(0)
        clan.append(vec)
    
    clanSet = []
    for i in range(0,len(clan)):
        if clan[i] not in clanSet:
            clanSet.append(clan[i])
    
    return len(clanSet)
