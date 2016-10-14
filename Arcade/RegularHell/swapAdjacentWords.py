def swapAdjacentWords(s):
    return re.sub(r'(\w+) (\w+)', r'\2 \1', s)

'''You are given a string consisting of words separated by whitespace characters, where the words consist only of Latin letters. Your task is to swap pairs of consecutive words and return the result.

Example

For s = "CodeFight On", the output should be
swapAdjacentWords(s) = "On CodeFight";
For s = "How are you today guys", the output should be
swapAdjacentWords(s) = "are How today you guys".
Input/Output

[time limit] 4000ms (py)
[input] string s

A string consisting of whitespace characters (' ') and Latin letters. There is exactly one whitespace character between two consecutive words, and both the first and the last characters of s are not equal to ' '.

Constraints:
0 ≤ s.length ≤ 100.

[output] string

String s with pairs of adjacent words swapped.'''
