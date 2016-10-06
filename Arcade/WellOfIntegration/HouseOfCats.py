#There are some people and cats in a house. You are given the number of legs they have all together. Your task is to return an array containing every possible number of people that could be in the house sorted in ascending order. It's guaranteed that each person has 2 legs and each cat has 4 legs.

#Example
#For legs = 6, the output should be
#houseOfCats(legs) = [1, 3].
#There could be either 1 cat and 1 person (4 + 2 = 6) or 3 people (2 * 3 = 6).
#For legs = 2, the output should be
#houseOfCats(legs) = [1].
#There can be only 1 person.

#Input/Output
#[time limit] 4000ms (py)

#[input] integer legs
#The total number of legs in the house.
#Constraints:
#0 ≤ legs ≤ 45.

#[output] array.integer
#Every possible number of people that can be in the house.

def houseOfCats(legs):
    maxCat = legs//4
    output = []
    for i in range(0,maxCat+1):
        people = (legs-i*4)//2
        output.insert(0,people)
        
    return output
