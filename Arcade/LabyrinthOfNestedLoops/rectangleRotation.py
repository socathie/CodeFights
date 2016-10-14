def rectangleRotation(a, b):
    pt = 0
    radius = pow(a/2,2)+pow(b/2,2)
    radius = int(math.ceil(pow(radius,.5)))
    
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            x = i*math.cos(math.radians(-45)) - j*math.sin(math.radians(-45))
            y = i*math.sin(math.radians(-45)) + j*math.cos(math.radians(-45))
            if -a/2<=x<=a/2 and -b/2<=y<=b/2:
                pt += 1
    return pt

'''A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?

Example

For a = 6 and b = 4, the output should be
rectangleRotation(a, b) = 23.

The following picture illustrates the example, and the 23 points are marked green.



Input/Output

[time limit] 4000ms (py)
[input] integer a

A positive even integer.

Constraints:
2 ≤ a ≤ 50.

[input] integer b

A positive even integer.

Constraints:
2 ≤ b ≤ 50.

[output] integer

The number of inner points with integer coordinates.'''
