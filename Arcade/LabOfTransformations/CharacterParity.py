#Given a character, check if it represents an odd digit, an even digit or not a digit at all.

#Example
#For symbol = '5', the output should be
#characterParity(symbol) = "odd";
#For symbol = '8', the output should be
#characterParity(symbol) = "even";
#For symbol = 'q', the output should be
#characterParity(symbol) = "not a digit".

#Input/Output

#[time limit] 4000ms (py)
#[input] char symbol
#[output] string

def characterParity(symbol):
    if '0'>symbol or '9'<symbol:
        return "not a digit"
    
    symbol = int(symbol)
    if symbol%2 == 0:
        return "even"
    else:
        return "odd"
