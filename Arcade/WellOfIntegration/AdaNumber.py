'''Consider two following representations of a non-negative integer:

A simple decimal integer, constructed of a non-empty sequence of digits from 0 to 9;
An integer with at least one digit in a base from 2 to 16 (inclusive), enclosed between # characters, and preceded by the base, which can only be a number between 2 and 16 in the first representation. For digits from 10 to 15 characters a, b, ..., f and A, B, ..., F are used.
Additionally, both representations may contain underscore (_) characters; they are used only as separators for improving legibility of numbers and can be ignored while processing a number.

Your task is to determine whether the given string is a valid integer representation.

Note: this is how integer numbers are represented in the programming language Ada.

Example

For line = "123_456_789", the output should be
adaNumber(line) = true;
For line = "16#123abc#", the output should be
adaNumber(line) = true;
For line = "10#123abc#", the output should be
adaNumber(line) = false;
For line = "10#10#123ABC#", the output should be
adaNumber(line) = false;
For line = "10#0#", the output should be
adaNumber(line) = true;
For line = "10##", the output should be
adaNumber(line) = false.
Input/Output

[time limit] 4000ms (py)
[input] string line

A non-empty string.

Constraints:
2 ≤ line.length ≤ 30.

[output] boolean

true if line is a valid integer representation, false otherwise.'''

def adaNumber(line):
    line = line.replace("_","")
    
    if "#" not in line:
        return line.isdigit()
    elif line.count("#")!=2:
        return False
    
    line = line.split("#")
    if not line[0].isdigit():
        return False
    elif int(line[0])<2 or int(line[0])>16:
        return False
    
    if line[1]=='':
        return False
    
    for i in range(2,11):
        if int(line[0])==i:
            for j in range(0,len(line[1])):
                if not '0'<=line[1][j]<=str(i-1):
                    return False
                
    for i in range(11,17):
        if int(line[0])==i:
            for j in range(0,len(line[1])):
                if not ('0'<=line[1][j]<='9' or 'a'<=line[1][j]<=chr(i-11+ord('a')) or 'A'<=line[1][j]<=chr(i-11+ord('A'))):
                    return False 

    return True
