#Proper nouns always begin with a capital letter, followed by small letters.

#Correct a given proper noun so that it fits this statement.

#Example
#For noun = "pARiS", the output should be
#properNounCorrection(noun) = "Paris";
#For noun = "John", the output should be
#properNounCorrection(noun) = "John".

#Input/Output
#[time limit] 4000ms (py)

#[input] string noun
#A string representing a proper noun with a mix of capital and small Latin letters.
#Constraints:
#1 ≤ noun.length ≤ 10.

#[output] string
#Corrected (if needed) noun.

def properNounCorrection(noun):
    return noun[0].upper()+noun[1:].lower()
