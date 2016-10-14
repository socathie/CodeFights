def replaceAllDigitsRegExp(inputString):
    return  re.sub(r'\d','#',inputString)

#Implement a function that replaces each digit in the given string with a '#' character.

#Example
#For input = "There are 12 points", the output should be
#replaceAllDigitsRegExp(input) = "There are ## points".

#Input/Output
#[time limit] 4000ms (py)

#[input] string input
#Constraints:
#5 ≤ input.length ≤ 20.

#[output] string
