'''An alphanumeric ordering of strings is defined as follows: each string is considered as a sequence of tokens, where each token is a letter or a number (as opposed to an isolated digit, as is the case of lexicographic ordering). For example, the tokens of a string "ab01c004" are [a, b, 01, c, 004]. In order to compare two strings, you break them down into tokens and compare corresponding pairs of tokens with each other (i.e. first token of the first string, with the first token of the second string etc).

Here is how tokens are compared:

If a letter is compared with another letter, the usual order applies.
A number is always less than a letter.
When two numbers are compared, their values are compared. Leading zeros, if any, are ignored.
If at some point one string has no more tokens left while the other one still does, the one with fewer tokens is considered smaller.

If the two strings s1 and s2 appear to be equal, consider the smallest index i such that tokens(s1)[i] and tokens(s2)[i] (where tokes(s)[i] is the ith token of string s) differ only by the number of leading zeros. If no such i exists, the strings are indeed equal. Otherwise, the string whose ith token has more leading zeros is considered less.

Here are some examples of comparing strings using alphanumeric ordering.

"a" < "a1" < "ab"
"ab42" < "ab000144" < "ab00144" < "ab144" < "ab000144x"
"x11y012" < "x011y13"
Example

For s1 = "a" and s2 = "a1", the output should be
alphanumericLess(s1, s2) = true;
For s1 = "ab" and s2 = "a1", the output should be
alphanumericLess(s1, s2) = false.
Input/Output

[time limit] 4000ms (py)
[input] string s1

String, consisting of Latin letters and digits.

Constraints:
1 ≤ s1.length ≤ 10.

[input] string s2

String, consisting of Latin letters and digits.

Constraints:
1 ≤ s2.length ≤ 10.

[output] boolean

true if s1 is alphanumerically strictly less than s2, false otherwise.'''

def alphanumericLess(s1, s2):
    if s1==s2:
        return False
    
    seq1 = ([i for i in re.split(r'(\d+|\D)', s1) if i])
    seq2 = ([i for i in re.split(r'(\d+|\D)', s2) if i])
    allEqual = True
    
    if len(seq1)>len(seq2):
        return False
    elif len(seq1)<len(seq2):
        return True
    
    for i in range(0,len(seq1)):
        if 'a'<=seq1[i]<='z':
            if seq1[i]>seq2[i]:
                return False
            elif seq1[i]<seq2[i]:
                allEqual = False
        else:
            if int(seq1[i])>int(seq2[i]):
                return False
            elif int(seq1[i])<int(seq2[i]):
                allEqual = False
    
    if allEqual:
        for i in range(0,len(seq1)):
            if 'a'<=seq1[i]<='z':
                pass
            else:
                if int(seq1[i])==int(seq2[i]):
                    if len(seq1[i])<len(seq2[i]):
                        return False
    return True
