def gravitation(rows):

    minTimer = len(rows)
    answer = []
    for i in range(len(rows[0])):
        finish = len(rows) - 1
        timer = 0
        for j in range(len(rows) - 1, -1, -1):
            if rows[j][i] == '#':
                timer = finish - j
                finish -= 1
        if timer == minTimer:
            answer.append(i)
        if timer < minTimer:
            minTimer = timer
            answer = [i]
    return answer

'''You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns. Stones are falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached the ground or they are not blocked by another motionless stone). Given the state of the box at some moment in time, find out which columns become motionless first.

Example

For

rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]
the output should be gravitation(rows) = [1, 4].

Check out the image below for better understanding:



Input/Output

[time limit] 4000ms (py)
[input] array.string rows

A non-empty array of strings of equal length consisting only of #-s and .-s describing the box at a specific moment in time. Sharps represent stones, and dots represent empty cells. row[0] corresponds to the upper row. Last element of rows corresponds to the ground level.

Constraints:
2 ≤ rows.length ≤ 10,
2 ≤ rows[i].length ≤ 10.

[output] array.integer

A sorted array containing numbers of all columns (leftmost column's number is 0) in which movements will stop at the same second and earlier than in any other column. Assume that if there are no stones in a column then movement stops immediately, i.e. after 0 seconds.'''
