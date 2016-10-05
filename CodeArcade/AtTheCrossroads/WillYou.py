'''Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.

Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

Example

For young = true, beautiful = true and loved = true, the output should be
willYou(young, beautiful, loved) = false.

Young and beautiful people are loved according to Mary's belief.

For young = true, beautiful = false and loved = true, the output should be
willYou(young, beautiful, loved) = true.

Mary doesn't believe that not beautiful people can be loved.

Input/Output

[time limit] 4000ms (py)
[input] boolean young
[input] boolean beautiful
[input] boolean loved
[output] boolean

true if the person contradicts Mary's belief, false otherwise.'''

def willYou(young, beautiful, loved):
    if young and beautiful and loved:
        return False
    elif young and beautiful and not loved:
        return True
    elif (young and beautiful) or loved:
        return True
    else:
        return False
