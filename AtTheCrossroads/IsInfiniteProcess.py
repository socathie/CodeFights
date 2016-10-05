'''Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

For a = 2 and b = 6, the output should be
isInfiniteProcess(a, b) = false;
For a = 2 and b = 3, the output should be
isInfiniteProcess(a, b) = true.
Input/Output

[time limit] 4000ms (py)
[input] integer a

Constraints:
0 ≤ a ≤ 20.

[input] integer b

Constraints:
0 ≤ b ≤ 20.

[output] boolean

true if the pseudocode will never stop, false otherwise.'''

def isInfiniteProcess(a, b):
    if b<a:
        return True
    
    if (b-a)%2 ==0:
        return False
    else:
        return True
