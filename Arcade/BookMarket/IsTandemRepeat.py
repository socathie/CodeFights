#Determine whether the given string can be obtained by one concatenation of some string to itself.

#Example
#For inputString = "tandemtandem", the output should be
#isTandemRepeat(inputString) = true;
#For inputString = "qqq", the output should be
#isTandemRepeat(inputString) = false;
#For inputString = "2w2ww", the output should be
#isTandemRepeat(inputString) = false.

#Input/Output
#[time limit] 4000ms (py)

#[input] string inputString
#Constraints:
#3 ≤ inputString.length ≤ 15.

#[output] boolean
#true if inputString represents a string concatenated to itself, false otherwise.

def isTandemRepeat(inputString):
    size = len(inputString)
    if inputString[0:size/2]==inputString[size/2:]:
        return True
    else:
        return False
