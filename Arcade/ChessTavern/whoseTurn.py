def whoseTurn(p):
    if p == "b1;g1;b8;g8":
        return True
    p = p.split(";")
    white = 0
    black = 0
    if p[0]!="b1":
        s = p[0]
        temp = ord(s[0])-ord("b")+int(s[1])-1
        if temp%2!=0:
            white += 1
    if p[1]!="g1":
        s = p[1]
        temp = ord(s[0])-ord("g")+int(s[1])-1
        if temp%2!=0:
            white += 1
    if p[2]!="b8":
        s = p[2]
        temp = ord(s[0])-ord("b")+int(s[1])-8
        if temp%2!=0:
            black += 1
    if p[3]!="g8":
        s = p[3]
        temp = ord(s[0])-ord("g")+int(s[1])-8
        if temp%2!=0:
            black += 1

    if white%2==black%2:
        return True
    
    return False

'''Imagine a standard chess board with only two white and two black knights placed in their standard starting positions: the white knights on b1 and g1; the black knights on b8 and g8.



There are two players: one plays for white, the other for black. During each move, the player picks one of his knights and moves it to an unoccupied square according to standard chess rules. Thus, a knight on d5 can move to any of the following squares: b6, c7, e7, f6, f4, e3, c3, and b4, as long as it is not occupied by either a friendly or an enemy knight.



The players take turns in making moves, starting with the white player. Given the configuration p of the knights after an unspecified number of moves, determine whose turn it is.

Example

For p = "b1;g1;b8;g8", the output should be
whoseTurn(p) = true.

The configuration corresponds to the initial state of the game. Thus, it's white's turn.

Input/Output

[time limit] 4000ms (py)
[input] string p

The positions of the four knights, starting with white knights, separated by a semicolon, in the chess notation.

[output] boolean

true if white is to move, false otherwise.'''
