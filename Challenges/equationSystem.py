def inv(s):
    m = []
    m.append([])
    m[0].append(s[1][1]*s[2][2]-s[1][2]*s[2][1])
    m[0].append(s[0][2]*s[2][1]-s[0][1]*s[2][2])
    m[0].append(s[0][1]*s[1][2]-s[0][2]*s[1][1])
    m.append([])
    m[1].append(s[1][2]*s[2][0]-s[1][0]*s[2][2])
    m[1].append(s[0][0]*s[2][2]-s[0][2]*s[2][0])
    m[1].append(s[0][2]*s[1][0]-s[0][0]*s[1][2])
    m.append([])
    m[2].append(s[1][0]*s[2][1]-s[1][1]*s[2][0])
    m[2].append(s[0][1]*s[2][0]-s[0][0]*s[2][1])
    m[2].append(s[0][0]*s[1][1]-s[0][1]*s[1][0])
    d = s[0][0]*m[0][0]+s[0][1]*m[1][0]+s[0][2]*m[2][0]
    return [m,d]

def equationSystem(m):
    s = [re.split("[xyz=]",i)[0:3] for i in m]
    m = [int(i.split("=")[1]) for i in m]
    for i in range(3):
        for j in range(3):
            if s[i][j]=="-":
                s[i][j]=-1
            elif s[i][j]=="+":
                s[i][j]=1
            elif s[i][j]=="":
                s[i][j]=1
            else:
                s[i][j] = int(s[i][j])
    [s,d] = inv(s)
    sol = []
    for i in range(3):
        x = 0
        for j in range(3):
            x += s[i][j]*m[j]
        x /= d
        sol.append(x)
    return sol

'''Equation System

Max has to do his homework, but he is not very good at math. His task is to solve several equation systems, where the output is guaranteed to be integer.

Can you help Max with this difficult assignment?

Example

For

equations = ["9x+5y+4z=21", 
             "6x+3y-5z=7", 
             "3x-10y+6z=35"]
the output should be
equationSystem(equations) = [3, -2, 1].

9 * 3 + 5 * (-2) + 4 * 1 = 27 - 10 + 4 = 21, correct;
6 * 3 + 3 * (-2) - 5 * 1 = 18 - 6 - 5 = 7, correct;
3 * 3 - 10 * (-2) + 6 * 1 = 9 + 20 + 6 = 35, correct.
Input/Output

[time limit] 4000ms (py)
[input] array.string equations

Array of three strings, each representing an equation. Each equation is given in the format Ax+By+Cz=D, where all coefficients are guaranteed to be integer.

Constraints:
equations.length = 3,
-2 · 109 < A, B, C, D < 2 · 109.

[output] array.integer

Solution as an array [x, y, z].'''
