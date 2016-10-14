def isInformationConsistent(evidences):
    for i in range(len(evidences[0])):
        info = 0
        for j in range(len(evidences)):
            if evidences[j][i]*info<0:
                return False
            else:
                info += evidences[j][i]
    return True

'''Court is in session. We got a group of witnesses who have all taken an oath to tell the truth. The prosecutor is pointing at the defendants one by one and asking each witnesses a simple question - "guilty or not?". The witnesses are allowed to respond in one of the following three ways:

I am sure he/she is guilty.
I am sure he/she is innocent.
I have no idea.
The prosecutor has a hunch that one of the witnesses might not be telling the truth so she decides to cross-check all of their testimonies and see if the information gathered is consistent, i.e. there are no two witnesses A and B and a defendant C such that A says C is guilty while B says C is innocent.

Example

For

evidences = [[ 0, 1, 0, 1], 
             [-1, 1, 0, 0], 
             [-1, 0, 0, 1]]
the output should be
isInformationConsistent(evidences) = true;

For

evidences = [[ 1, 0], 
             [-1, 0], 
             [ 1, 1],
             [ 1, 1]]
the output should be
isInformationConsistent(evidences) = false.

Input/Output

[time limit] 4000ms (py)
[input] array.array.integer evidences

2-dimensional array of integers representing the set of testimonials. evidences[i][j] is the testimonial of the ith witness on the jth defendant. -1 means "innocent", 0 means "no idea", and 1 means "guilty".

Constraints:
2 ≤ evidences.length ≤ 5,
2 ≤ evidences[0].length ≤ 10.

[output] boolean

true if the evidence is consistent, false otherwise.'''
