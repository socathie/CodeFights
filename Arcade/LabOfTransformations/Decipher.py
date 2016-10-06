#Consider the following ciphering algorithm:

#For each character replace it with its code.
#Concatenate all of the obtained numbers.
#Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.

#Note: here the character's code means its decimal ASCII code, the numerical representation of a character used by most modern programming languages.

#Example
#For cipher = "10197115121", the output should be
#decipher(cipher) = "easy".

#Explanation: charCode('e') = 101, charCode('a') = 97, charCode('s') = 115 and charCode('y') = 121.

#Input/Output

#[time limit] 4000ms (py)

#[input] string cipher
#A non-empty string which is guaranteed to be a cipher for some other string of lowercase letters.
#Constraints:
#2 ≤ cipher.length ≤ 100.

#[output] string

def decipher(cipher):
    decipher = []
    while cipher:
        if cipher[0]=='9':
            decipher.append(cipher[0:2])
            cipher = cipher[2:]
        else:
            decipher.append(cipher[0:3])
            cipher = cipher[3:]
    
    for i in range(0,len(decipher)):
        decipher[i] = chr(int(decipher[i]))
    
    return "".join(decipher)
