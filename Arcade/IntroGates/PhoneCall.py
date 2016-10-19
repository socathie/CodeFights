#Some phone usage rate may be described as follows:

#first minute of a talk costs min1 cents,
#each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
#each minute after 10th costs min11 cents.
#You have S cents on your account before the call. What is the duration of the longest call (in minutes rounded down to the nearest integer) you can have?

#Example
#For min1 = 3, min2_10 = 1, min11 = 2 and S = 20, the output should be
#phoneCall(min1, min2_10, min11, S) = 14.

#Here's why:
#the first minute costs 3 cents, which leaves you with 20 - 3 = 17 cents;
#the total cost of minutes 2 through 10 is 1 * 9 = 9, so you can talk 9 more minutes and still have 17 - 9 = 8 cents;
#each next minute costs 2 cents, which means that you can talk 8 / 2 = 4 more minutes.
#Thus, the longest call you can make is 1 + 9 + 4 = 14 minutes long.

#Input/Output
#[time limit] 4000ms (py)

#[input] integer min1
#Constraints:
#1 ≤ min1 ≤ 10.

#[input] integer min2_10
#Constraints:
#1 ≤ min2_10 ≤ 10.

#[input] integer min11
#Constraints:
#1 ≤ min11 ≤ 10.

#[input] integer S
#Constraints:
#2 ≤ S ≤ 60.

#[output] integer

def phoneCall(min1, min2_10, min11, S):
    temp = 0
    if S>=min1:
        S -= min1
        temp += 1
    else:
        return temp
    
    for x in range(0,9):
        if S>=min2_10:
            S -= min2_10
            temp +=1
    if temp == 10: 
        while S>=min11:
            S -= min11
            temp += 1
        
    return temp

##########

def phoneCall(min1, min2_10, min11, s):

    if s < min1:
        return 0
    for i in range(2, 11):
        if s < min1 + min2_10 * (i - 1):
            return i - 1
    return (s - min1 - min2_10 * 9.0) //min11 + 10

