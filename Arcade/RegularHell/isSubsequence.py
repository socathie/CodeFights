def isSubsequence(t, s):
    pattern = ''
    for ch in s :
        pattern += "["+ch+"]"+"+.*"
    return re.search(pattern, t) is not None

'''Given a string s, determine if it is a subsequence of a given string t.

Example

For t = "CodeFights" and s = "CoFi", the output should be
isSubsequence(t, s) = true;

For t = "CodeFights" and s = "cofi", the output should be
the output should be
isSubsequence(t, s) = false.

Input/Output

[time limit] 4000ms (py)
[input] string t

A string consisting of Latin letters, whitespace characters (' '), digits and punctuation marks (".,?!=*+-").

Constraints:
0 ≤ t.length ≤ 500.

[input] string s

A string consisting of Latin letters, whitespace characters (' '), digits and punctuation marks (".,?!=*+-").

Constraints:
0 ≤ s.length ≤ 30.

[output] boolean

true if the s is a subsequence of t, false otherwise.'''
