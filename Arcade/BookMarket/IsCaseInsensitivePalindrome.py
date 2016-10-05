#Given a string, check if it can become a palindrome through a case change of some (possibly, none) letters.

#Example
#For inputString = "AaBaa", the output should be
#isCaseInsensitivePalindrome(inputString) = true.
#"aabaa" is a palindrome as well as "AABAA", "aaBaa", etc.

#For inputString = "abac", the output should be
#isCaseInsensitivePalindrome(inputString) = false.
#All the strings which can be obtained via changing case of some group of letters, i.e. "abac", "Abac", "aBAc" and 13 more, are not palindromes.

#Input/Output
#[time limit] 4000ms (py)

#[input] string inputString
#Non-empty string consisting of letters.
#Constraints:
#4 ≤ inputString.length ≤ 10.

#[output] boolean

def isCaseInsensitivePalindrome(inputString):
    inputString = inputString.lower()
    size = len(inputString)
    temp = 1
    for i in range(0,size/2):
        if inputString[i]==inputString[-i-1]:
            temp *=1
        else:
            temp *=0
    
    if temp ==0:
        return False
    else:
        return True
