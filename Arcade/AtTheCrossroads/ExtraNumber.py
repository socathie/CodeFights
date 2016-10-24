#You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. What is the value of the third integer?

#Example
#For a = 2, b = 7 and c = 2, the output should be
#extraNumber(a, b, c) = 7.

#The two equal numbers are a and c. The third number (b) equals 7, which is the answer.

#Input/Output
#[time limit] 4000ms (py)

#[input] integer a
#Constraints:
#1 ≤ a ≤ 109.

#[input] integer b
#Constraints:
#1 ≤ b ≤ 109.

#[input] integer c
#Constraints:
#1 ≤ c ≤ 109.

#[output] integer

def extraNumber(a, b, c):
    if a==b:
        return c
    elif a==c:
        return b
    else:
        return a
