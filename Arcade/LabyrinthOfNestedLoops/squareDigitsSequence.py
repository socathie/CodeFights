def squareDigitsSequence(a0):
    a = []
    a.append(a0)
    
    index = 2
    temp = 0
    while a0:
        temp += pow((a0%10),2)
        a0 //= 10
    
    while temp not in a:
        index += 1
        a.append(temp)
        a0 = temp
        temp = 0
        while a0:
            temp += pow((a0%10),2)
            a0 //= 10
    
    return index
        
'''Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

Given the first element a0, find the length of the sequence.

Example

For a0 = 16, the output should be
squareDigitsSequence(a0) = 9.

Here's how elements of the sequence are constructed:

a0 = 16
a1 = 12 + 62 = 37
a2 = 32 + 72 = 58
a3 = 52 + 82 = 89
a4 = 82 + 92 = 145
a5 = 12 + 42 + 52 = 42
a6 = 42 + 22 = 20
a7 = 22 + 02 = 4
a8 = 42 = 16, which has already occurred before (a0)
Thus, there are 9 elements in the sequence.

For a0 = 103, the output should be
squareDigitsSequence(a0) = 4.

The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.

Input/Output

[time limit] 4000ms (py)
[input] integer a0

First element of a sequence, positive integer.

Constraints:
1 ≤ a0 ≤ 650.

[output] integer'''
