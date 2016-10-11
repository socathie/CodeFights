'''Some people run along a straight line in the same direction. They start simultaneously at pairwise distinct positions and run with constant speed (which may differ from person to person).

If two or more people are at the same point at some moment we call that a meeting. The number of people gathered at the same point is called meeting cardinality.

For the given starting positions and speeds of runners find the maximum meeting cardinality assuming that people run infinitely long.

Example

For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
runnersMeetings(startPosition, speed) = 3.

In 20 seconds after the runners start running, they end up at the same point. Check out the gif below for better understanding:



Input/Output

[time limit] 4000ms (py)
[input] array.integer startPosition

A non-empty array of integers representing starting positions of runners (in meters).

Constraints:
2 ≤ startPosition.length ≤ 10,
-1000 ≤ startPosition[i] ≤ 1000.

[input] array.integer speed

Array of positive integers of the same length as startPosition representing speeds of the runners (in meters per minute).

Constraints:
speed.length = startPosition.length,
1 ≤ speed[i] ≤ 30.

[output] integer'''

def runnersMeetings(startPosition, speed):
    meet = 1
    for time in range(0,10000):
        displacement = [i*time/3 for i in speed]
        pos = set([sum(x) for x in zip(startPosition, displacement)])
        if len(pos)<len(speed):
            meet = max(meet,len(speed)-len(pos)+1)
    
    return meet
