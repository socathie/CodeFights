X = lambda a,b: [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]

d = lambda a,b: sum([i*j for (i,j) in zip(a,b)])

def raycast(t,r):
    u = [j-i for (i,j) in zip(t[0],t[1])]
    v = [j-i for (i,j) in zip(t[0],t[2])]
    n = X(u,v)
    w = [j-i for (i,j) in zip(t[0],r[0])]
    a = -float(d(n,w))
    b = d(n,r[1])
    if b==0:
        if a==0:
            return r[0]
        else:
            return []
    if (a/b)<0:
        return []
    
    I = [(a/b)*j+i for (i,j) in zip(r[0],r[1])]
    uu = d(u,u)
    vv = d(v,v)
    uv = d(u,v)
    w = [i-j for (i,j) in zip(I,t[0])]
    wu = d(w,u)
    wv = d(w,v)
    D = float(uv*uv-uu*vv)
    s = (uv * wv - vv * wu) / D
    if (s<0 or s>1):
        return []
    t = (uv * wu - uu * wv) / D
    if (t<0 or (s+t)>1):
        return []
    I.append(pow(sum([(i-j)*(i-j) for (i,j) in zip(r[0],I)]),.5))
    return ["{0:.2f}".format(i) for i in I]

'''Raycasting

Raycasting is a method used in game development to find how a ray intersects a model. It can be used, for example, to find out how a user selects a model with his mouse.

Models are usually covered with triangular mesh. Take a look at the model below for an example:


A lot of algorithms were developed for the raycasting. One of the simplest methods is to check each triangle of the model's mesh. Obviously, it's not very clever and not efficient, but it's a good method to begin exploring the raycasting algorithms with.

Given a triangle of a mesh and a ray, your task is to determine at which point the ray will intersect the triangle, and find the distance to this point. Note, that if the ray is parallel to the triangle, it's not considered to be an intersection.

If the ray doesn't intersect the model, return an empty array.
All values of the resulting array should be rounded to two decimal places.

Example

For

triangle = [[-2,  2, 1], 
            [ 2,  2, 1], 
            [ 0, -4, 1]]
and

ray = [[0, 0, 0], 
       [0, 0, 1]]
the output should be
raycast(triangles, ray) = [0, 0, 1, 1].



Input/Output

[time limit] 4000ms (py)
[input] array.array.float triangle

One of mesh triangles. The triangle is given as an array of its vertices, where for each vertex its coordinates are given in the format [x, y, z]. Each value is given with no more than 2 decimal places.

Note, that the vertices can be given in both clockwise and counterclockwise order.

Constraints:
triangle.length = 3,
triangle[i].length = 3,
-500 ≤ triangle[i][j] ≤ 500.

[input] array.array.float ray

Ray given as an array of two elements, where the first element denotes its source, and the second one denotes its direction. Each value is given with no more than 2 decimal places.

Constraints:
ray.length = 2,
ray[i].length = 3,
-500 ≤ ray[i][j] ≤ 500.

[output] array.float

Coordinates of the Intersection and the distance to it, or an empty array if the ray doesn't intersect the triangle.

All values should be rounded to two decimal places.'''
