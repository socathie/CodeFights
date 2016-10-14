def bishopDiagonal(bishop1, bishop2):
    sort = sorted([bishop1,bishop2])
    bishop1 = sort[0]
    bishop2 = sort[1]
    if abs(int(bishop1[1])-int(bishop2[1]))!=ord(bishop2[0])-ord(bishop1[0]):
        return sort
    
    if bishop1[1]<bishop2[1]:
        while "a"<bishop1[0] and "1"<bishop1[1]:
            bishop1 = chr(ord(bishop1[0])-1)+str(int(bishop1[1])-1)
        while bishop2[0]<"h" and bishop2[1]<"8":
            bishop2 = chr(ord(bishop2[0])+1)+str(int(bishop2[1])+1)
        return sorted([bishop1,bishop2])
    
    if bishop1[1]>bishop2[1]:
        while "a"<bishop1[0] and bishop1[1]<"8":
            bishop1 = chr(ord(bishop1[0])-1)+str(int(bishop1[1])+1)
        while bishop2[0]<"h" and "1"<bishop2[1]:
            bishop2 = chr(ord(bishop2[0])+1)+str(int(bishop2[1])-1)
        return sorted([bishop1,bishop2])

'''In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal, they immediately rush towards the opposite ends of that same diagonal.

Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.

Example

For bishop1 = "d7" and bishop2 = "f5", the output should be
bishopDiagonal(bishop1, bishop2) = ["c8", "h3"].



For bishop1 = "d8" and bishop2 = "b5", the output should be
bishopDiagonal(bishop1, bishop2) = ["b5", "d8"].

The bishops don't belong to the same diagonal, so they don't move.


Input/Output

[time limit] 4000ms (py)
[input] string bishop1

Coordinates of the first bishop in chess notation.

[input] string bishop2

Coordinates of the second bishop in the same notation.

[output] array.string

Coordinates of the bishops in lexicographical order after they check the diagonals they stand on.'''
