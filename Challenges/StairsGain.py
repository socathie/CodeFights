def StairsGain(s):
    return (len(s)-2*s.count('g'))*3/2

'''You're standing in front of a staircase with some steps painted gray and others painted yellow. When climbing up the stairs you can either put your foot on the next step, or on the one after it (i.e. you can step over the next step).

Putting your foot on a yellow step gives you 1 point and stepping over it gives you 2 points. When you put your your foot on a gray step you lose 2 points, and when you step over it you lose 1 point.

As the first move, you should put your foot to the first or the second step, and as your last move you must put your foot on the last step.

Determine the maximum possible score you can get having climbed up the stairs.

Example

For stairs = "ygy", the output should be
StairsGain(stairs) = 1.

According to the rules, there are three ways to go to the top of the stairs:

Stepping on each step. Then the score will be 1 + (- 2) + 1 = 0.
Stepping on the first step, stepping over the second step right at the third one. In this case the score is: 1 + (- 1) + 1 = 1.
Making the first move on the second step, and then moving on the third one. Here the score equals to: 2 + (- 2) + 1 = 1.
Thus, the highest possible score is 1.

Input/Output

[time limit] 4000ms (py)
[input] string stairs

A string consisting of letters "y" and "g" representing the sequence of colors of the stairs.

Constraints:
1 ≤ stairs.length ≤ 104.

[output] integer

The maximum possible score you can get having climbed up the stairs.'''
