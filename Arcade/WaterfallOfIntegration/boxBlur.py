def pixel(matrix,i,j):
    total = 0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            total += matrix[x][y]
    return total//9

def boxBlur(image):
    sol = []
    row = len(image)
    col = len(image[0])
    for i in range(1,row-1):
        temp = []
        for j in range(1,col-1):
            temp.append(pixel(image,i,j))
        sol.append(temp)
    
    return sol

'''Last night you had to study, but decided to party instead. Now there is a black and white photo of you that is about to go viral. You cannot let this ruin your reputation, so you want to apply box blur algorithm to the photo to hide its content.

The algorithm works as follows: each pixel x in the resulting image has a value equal to the average value of the input image pixels' values from the 3 × 3 square with the center at x. All pixels at the edges are cropped.

As pixel's value is an integer, all fractions should be rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

In the given example all boundary pixels were cropped, and the value of the pixel in the middle was obtained as (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) / 9 = 15 / 9 = ~rounded down~ = 1.

Input/Output

[time limit] 4000ms (py)
[input] array.array.integer image

An image is stored as a rectangular matrix of non-negative integers.

Constraints:
3 ≤ image.length ≤ 10,
3 ≤ image[0].length ≤ 10,
0 ≤ image[i][j] ≤ 255.

[output] array.array.integer

A blurred image.'''
