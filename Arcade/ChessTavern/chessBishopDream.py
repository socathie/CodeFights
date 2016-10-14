def chessBishopDream(boardSize, pos, Dir, k):
    [x,y] = boardSize
    orgPos = list(pos)
    initDir = list(Dir)
    for n in range(x*y*4):
        orgDir = list(Dir)

        if pos[0]+Dir[0]<0:
            Dir[0] = 1
        elif pos[0]+Dir[0]>=x:
            Dir[0] = -1
        if pos[1]+Dir[1]<0:
            Dir[1] = 1
        elif pos[1]+Dir[1]>=y:
            Dir[1] = -1
        print pos,Dir
        temp = [(i+j)/2 for (i,j) in zip(orgDir,Dir)]
        pos = [i+j for (i,j) in zip(pos,temp)]
        if n==(k-1):
            break
        if pos == orgPos and Dir==initDir:
            print n
            break
    
    if n!=(k-1):
        for m in range(k%(n+1)):
            orgDir = list(Dir)

            if pos[0]+Dir[0]<0:
                Dir[0] = 1
            elif pos[0]+Dir[0]>=x:
                Dir[0] = -1
            if pos[1]+Dir[1]<0:
                Dir[1] = 1
            elif pos[1]+Dir[1]>=y:
                Dir[1] = -1
            print pos,Dir
            temp = [(i+j)/2 for (i,j) in zip(orgDir,Dir)]
            pos = [i+j for (i,j) in zip(pos,temp)]
            
    return pos

'''In ChessLand there is a small but proud chess bishop with a recurring dream. In the dream the bishop finds itself on an n × m chessboard with mirrors along each edge, and it is not a bishop but a ray of light. This ray of light moves only along diagonals (the bishop can't imagine any other types of moves even in its dreams), it never stops, and once it reaches an edge or a corner of the chessboard it reflects from it and moves on.

Given the initial position and the direction of the ray, find its position after k steps where a step means either moving from one cell to the neighboring one or reflecting from a corner of the board.

Example

For boardSize = [3, 7], initPosition = [1, 2],
initDirection = [-1, 1] and k = 13, the output should be
chessBishopDream(boardSize, initPosition, initDirection, k) = [0, 1].

Here is the bishop's path:

[1, 2] -> [0, 3] -(reflection from the top edge)-> [0, 4] -> 
[1, 5] -> [2, 6] -(reflection from the bottom right corner)-> [2, 6] ->
[1, 5] -> [0, 4] -(reflection from the top edge)-> [0, 3] ->
[1, 2] -> [2, 1] -(reflection from the bottom edge)-> [2, 0] -(reflection from the left edge)->
[1, 0] -> [0, 1]


Input/Output

[time limit] 4000ms (py)
[input] array.integer boardSize

An array of two integers, the number of rows and columns, respectively. Rows are numbered by integers from 0 to boardSize[0] - 1, columns are numbered by integers from 0 to boardSize[1] - 1 (both inclusive).

Constraints:
1 ≤ boardSize[i] ≤ 20.

[input] array.integer initPosition

An array of two integers, indices of the row and the column where the bishop initially stands, respectively.

Constraints:
0 ≤ initPosition[i] < boardSize[i].

[input] array.integer initDirection

An array of two integers representing the initial direction of the bishop. If it stands in (a, b), the next cell he'll move to is (a + initDirection[0], b + initDirection[1]) or whichever it'll reflect to in case it runs into a mirror immediately.

Constraints:
initDirection[i] ∈ {-1, 1}.

[input] integer k

Constraints:
1 ≤ k ≤ 109.

[output] array.integer

The position of the bishop after k steps.'''
