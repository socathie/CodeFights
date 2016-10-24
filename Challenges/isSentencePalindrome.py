def isSentencePalindrome(s):
    c = re.sub('\W', "", s).lower()
    return c == c[::-1]

'''As a high school student, you naturally have a favourite professor. And, even more natural, you have a least favourite one: professor X!

Having heard that you're an experienced CodeFighter, he became jealous and gave you an extra task as a homework. Given a sentence, you're supposed to find out if it's a palindrome or not.

The expected output for most of the test cases baffled you, but you quickly realize where the catch is. Looks like your professor assumes that a string is a palindrome if the letters in it are the same when you read it normally and backwards. Moreover, the tests even ignore the cases of the letters!

Given the sentence your professor wants you to test, return true if it's considered to be a palindrome by your professor, and false otherwise.

Example

For sentence = "Bob: Did Anna peep? | Anna: Did Bob?",
the output should be
isSentencePalindrome(sentence) = true.

Input/Output

[time limit] 4000ms (py)
[input] string sentence

A string consisting of various characters.

Constraints:
1 ≤ sentence ≤ 30.

[output] boolean

true if the sentence is a palindrome according to your professor and false otherwise.'''
