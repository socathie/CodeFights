'''Yesterday you found some shoes in your room. Each shoe is described by two values:

type indicates if it's a left or a right shoe;
size is the size of the shoe.
Your task is to check whether it is possible to pair the shoes you found in such a way that each pair consists of a right and a left shoe of an equal size.

Example

For

shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [0, 23]]
the output should be
pairOfShoes(shoes) = true;

For

shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [1, 23]]
the output should be
pairOfShoes(shoes) = false.

Input/Output

[time limit] 4000ms (py)
[input] array.array.integer shoes

Array of shoes. Each shoe is given in the format [type, size], where type is either 0 or 1 for left and right respectively, and size is a positive integer.

Constraints:
1 ≤ shoes.length ≤ 25,
1 ≤ shoes[i][1] ≤ 100.

[output] boolean

true if it is possible to pair the shoes, false otherwise.'''

def pairOfShoes(shoes):
    if shoes==[] or len(shoes)%2!=0:
        return False
    
    while shoes!=[]:
        shoe = shoes[0]
        if [1-shoe[0],shoe[1]] not in shoes:
            return False
        else:
            shoes = shoes[1:]
            i = 0
            while shoes[i] != [1-shoe[0],shoe[1]]:
                i += 1
            shoes =shoes[0:i]+shoes[i+1:]
    
    return True
