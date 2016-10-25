f = [0,1,1,2,3,5,8,13,21,34,55,89,144,233]
s = lambda m: re.sub(" ","",m).upper()
FibonacciSecret = lambda m : "-".join([s(m)[i] for i in f if i<len(s(m))])

'''In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence. For more information, please click here.

You will be given a message. Your mission is to get all the characters in that message at positions that are present in the Fibonacci sequence (a sequence formed by the the Fibonacci number sorted in ascending order). Please ignore whitespace characters and use the extended Fibonacci.

Return the obtained characters capitalized and connected by the '-' character.

Example

For message = "The Da Vinci Code is a 2003 mystery-detective novel by Dan Brown",
the output should be
FibonacciSecret(message) = "T-H-H-E-D-V-C-E-M-T".

The first Fibonacci is 0 then the first letter is T
The second Fibonacci is 1 then the second letter is H
The third Fibonacci is 1 then the third letter is H
... and so on.
Thus, the answer should be "T-H-H-E-D-V-C-E-M-T".

Input/Output

[time limit] 4000ms (py)
[input] string message

Constraints:
1 ≤ message.length ≤ 255.

[output] string

Your decrypted message.'''
