#Given a positive integer number and a certain length, we need to modify the given number to have a specified length. We are allowed to do that either by cutting out leading digits (if the number needs to be shortened) or by adding 0s in front of the original number.

#Example
#For number = 1234 and width = 2, the output should be
#integerToStringOfFixedWidth(number, width) = "34";
#For number = 1234 and width = 4, the output should be
#integerToStringOfFixedWidth(number, width) = "1234";
#For number = 1234 and width = 5, the output should be
#integerToStringOfFixedWidth(number, width) = "01234".

#Input/Output
#[time limit] 4000ms (py)

#[input] integer number
#A non-negative integer.
#Constraints:
#0 ≤ number ≤ 105.

#[input] integer width
#A positive integer representing the desired length.
#Constraints:
#1 ≤ width ≤ 5.

#[output] string
#The modified version of number as described above.

def integerToStringOfFixedWidth(number, width):
    number = str(number)
    
    while len(number)>width:
        number = number[1:]
        
    while len(number)<width:
        number = "0"+number
    
    return number
