def onboard(a,n):
    if ord("a")<=a<=ord("h") and 1<=n<=8:
        return True
    return False
    
def chessKnightMoves(cell):
    move = 0
    cell = [ord(cell[0]),int(cell[1])]
    moves = [[1,2],[2,1],[-1,-2],[-2,-1],[-1,2],[-2,1],[1,-2],[2,-1]]
    for m in moves:
        if onboard(cell[0]+m[0],cell[1]+m[1]):
            move+=1
    return move

'''Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



Example

For cell = "a1", the output should be
chessKnightMoves(cell) = 2.



For cell = "c2", the output should be
chessKnightMoves(cell) = 6.



Input/Output

[time limit] 4000ms (py)
[input] string cell

String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

[output] integer'''
