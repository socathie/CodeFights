'''It's Christmas time! To share his Christmas spirit with all his friends, young Christmas elf decided to send each of them a Christmas e-mail with a nice Christmas tree. Unfortunately, Internet traffic is very expensive in the North Pole, so instead of sending an actual image he decided to draw the tree using only asterisks ('*' symbols). He has given you the specs (see below) and your task is to write a program that would generate trees following the spec and some initial parameters.

Here is a formal definition of how the tree should be built but before you read it the elf HIGHLY recommends looking first at the examples that follow:

Each tree has a crown, that looks as follows:

 *
 *
***
Define a line as a horizontal group of asterisks and a level as a collection of levelHeight lines stacked one on top of the other.

Below the crown there are levelNum levels.

The tree is perfectly symmetric so all the middle asterisks of the lines lie on the center of the tree.

Each line of the same level (excluding the first one) has two more asterisks than the previous one (one on each end);

The number of asterisks in the first line of each level is chosen as follows:

the first line of the first level has 5 asterisks;
the first line of each consecutive level contains two more asterisks than the first line of the previous level.
And finally there is the tree foot which has a height of levelNum and a width of:

levelHeight asterisks if levelHeight is odd;
levelHeight + 1 asterisks if levelHeight is even.
Given levelNum and levelHeight, return the Christmas tree of the young elf.

Example

For levelNum = 1 and levelHeight = 3, the output should be

christmasTree(levelNum, levelHeight) =
    ["    *",
     "    *",
     "   ***",
     "  *****",
     " *******",
     "*********",
     "   ***"]
, which represents the following tree:

            ___
      *        |
      *        |-- the crown      
     ***    ___|       
    *****      |
   *******     |-- level 1
  ********* ___|
     ***    ___|-- the foot
For levelNum = 2 and levelHeight = 4, the output should be

christmasTree(levelNum, levelHeight) = 
    ["      *", 
     "      *", 
     "     ***", 
     "    *****", 
     "   *******", 
     "  *********", 
     " ***********", 
     "   *******", 
     "  *********", 
     " ***********", 
     "*************", 
     "    *****", 
     "    *****"]
, which represents the following tree:

                ___ 
        *          |
        *          | -- the crown
       ***      ___|
      *****        |
     *******       | -- level 1
    *********      |
   ***********  ___|
     *******       |
    *********      | -- level 2
   ***********     |
  ************* ___|
      *****        | -- the foot
      *****     ___|
Input/Output

[time limit] 4000ms (py)
[input] integer levelNum

A positive integer, the number of levels.

Constraints:
1 ≤ levelNum ≤ 8.

[input] integer levelHeight

The number of lines in each level.

Constraints:
3 ≤ levelHeight ≤ 8.

[output] array.string

The Christmas tree according to the specs and the inputs. Output elements should not contain trailing whitespaces, and at least one of them should start with '*' symbol.'''

def christmasTree(levelNum, levelHeight):
    maxW = 5+(levelHeight-1)*2
    width = 5+(levelHeight-1)*2+(levelNum-1)*2
    crown = [" "*((width-1)//2)+"*"," "*((width-1)//2)+"*"," "*(((width-1)/2-1))+"***"]
    tree = crown
    
    for i in range(levelNum):
        for j in range(5+i*2,maxW+i*2+1,2):
            space = " "*((width-j)//2)
            line = space+"*"*j
            tree.append(line)
    
    if levelHeight%2==0:
        foot = "*"*(levelHeight+1)
    else:
        foot = "*"*levelHeight
    foot = " "*((width-len(foot))//2)+foot
    for i in range(levelNum):
        tree.append(foot)
    return tree
