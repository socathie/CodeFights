'''Miss X has only two combs in her possession, both of which are old and miss a tooth or two. She also has many purses of different length, in which she carries the combs. The only way they fit is horizontally and without overlapping. Given teeth' positions on both combs, find the minimum length of the purse she needs to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.
It is also guaranteed that the total length of two strings is smaller than 32.

Example

For comb1 = "*..*" and comb2 = "*.*", the output should be
combs(comb1, comb2) = 5.

Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.



Input/Output

[time limit] 4000ms (py)
[input] string comb1

A comb is represented as a string. If there is an asterisk ('*') in the ith position, there is a tooth there. Otherwise there is a dot ('.'), which means there is a missing tooth on the comb.

Constraints:
1 ≤ comb1.length ≤ 10.

[input] string comb2

The second comb is represented in the same way as the first one.

Constraints:
1 ≤ comb2.length ≤ 10.

[output] integer

The minimum length of a purse Miss X needs.'''

def combs(comb1, comb2):
    len1 = len(comb1)
    len2 = len(comb2)
    minLen = len1+len2
    
    for pos in range(1,len1+1):
        fit = True
        for i in range(pos,min(len1,len2+pos)):
            if comb1[i]=="*" and comb2[i-pos]=="*":
                fit = False
                break
        if fit:
            minLen = len2+pos
            break
    
    return max(minLen,len1,len2)
