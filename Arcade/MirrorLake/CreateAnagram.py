#You are given two strings s and t of the same length, consisting of uppercase English letters. Your task is to find the minimum number of "replacement operations" needed to get some anagram of the string t from the string s. A replacement operation is performed by picking exactly one character from the string s and replacing it by some other character.

#Example
#For s = "AABAA" and t = "BBAAA", the output should be
#createAnagram(s, t) = 1;
#For s = "OVGHK" and t = "RPGUC", the output should be
#createAnagram(s, t) = 4.

#Input/Output
#[time limit] 4000ms (py)

#[input] string s
#Constraints:
#5 ≤ s.length ≤ 35.

#[input] string t
#Constraints:
#t.length = s.length.

#[output] integer
#The minimum number of replacement operations needed to get an anagram of the string t from the string s.

def createAnagram(s, t):
    change = 0
    for i in range(0,len(s)):
        change += abs(s.count(s[i])-t.count(s[i]))/s.count(s[i])
        
    return change
