'''A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.

A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with the corresponding (i.e. having the same index) letter of some ciphertext alphabet.

Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.

Example

For string1 = "aacb" and string2 = "aabc", the output should be
isSubstitutionCipher(string1, string2) = true.

Any ciphertext alphabet that starts with acb... would make this transformation possible.

For string1 = "aa" and string2 = "bc", the output should be
isSubstitutionCipher(string1, string2) = false.

Input/Output

[time limit] 4000ms (py)
[input] string string1

A string consisting of lowercase characters.

Constraints:
1 ≤ string1.length ≤ 10.

[input] string string2

A string consisting of lowercase characters of the same length as string1.

Constraints:
string2.length = strin1.length.

[output] boolean'''

def isSubstitutionCipher(string1, string2):
    string1count = []
    string2count = []
    for i in range(0,len(string1)):
        string1count.append(string1.count(string1[i]))
    for i in range(0,len(string2)):
        string2count.append(string2.count(string2[i]))
    
    for i in range(0,len(string1count)):
        if string1count.count(string1count[i])!=string2count.count(string1count[i]):
            return False
    
    return True
