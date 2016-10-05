'''Given a string consisting of lowercase English letters, find the largest square which can be obtained by reordering its characters and replacing them with digits (leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.

If there is no solution, return -1.

Example

For s = "ab", the output should be
constructSquare(s) = 81;

For s = "zzz", the output should be
constructSquare(s) = -1.

There are no 3-digit square numbers with identical digits.

For s = "aba", the output should be
constructSquare(s) = 900.

It can be obtained after reordering the initial string into "baa".

Input/Output

[time limit] 4000ms (py)
[input] string s

Constraints:
2 ≤ s.length < 10.

[output] integer'''

def constructSquare(s):
    counted = []
    num = []
    for i in range(0,len(s)):
        if s[i] not in counted:
            num.append(s.count(s[i]))
            counted.append(s[i])
    digits = sum(num)
    num = sorted(num)
    
    
    
    for j in range(int(math.ceil(pow(pow(10,digits),.5))),0,-1):
        sq = str(int(pow(j,2)))
        counted = []
        numSq = []
        for i in range(0,len(sq)):
            if sq[i] not in counted:
                numSq.append(sq.count(sq[i]))
                counted.append(sq[i])
        numSq = sorted(numSq)
        if num == numSq:
            return int(sq)
    
    return -1
