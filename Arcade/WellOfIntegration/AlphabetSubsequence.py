#Check whether the given string is a subsequence of the plaintext alphabet.

#Example
#For s = "effg" or s = "cdce", the output should be
#alphabetSubsequence(s) = false;
#For s = "ace" or s = "bxz", the output should be
#alphabetSubsequence(s) = true.

#Input/Output
#[time limit] 4000ms (py)

#[input] string s
#Constraints:
#2 ≤ s.length ≤ 15.

#[output] boolean
#true if the given string is a subsequence of the alphabet, false otherwise.

def alphabetSubsequence(s):
    maxAlpha = ord('a')-1
    for i in range(0,len(s)):
        if ord(s[i]) <= maxAlpha:
            return False
        maxAlpha = max(maxAlpha,ord(s[i]))
    return True
