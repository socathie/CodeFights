#You are playing an RPG. Currently your points total is equal to experience. To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.

#Given values experience, threshold and reward, check if you reach the next level after killing the monster.

#Example
#For experience = 10, threshold = 15 and reward = 5, the output should be
#reachNextLevel(experience, threshold, reward) = true;
#For experience = 10, threshold = 15 and reward = 4, the output should be
#reachNextLevel(experience, threshold, reward) = false.

#Input/Output
#[time limit] 4000ms (py)

#[input] integer experience
#Constraints:
#3 ≤ experience ≤ 250.

#[input] integer threshold
#Constraints:
#5 ≤ threshold ≤ 300.

#[input] integer reward
#Constraints:
#2 ≤ reward ≤ 65.

#[output] boolean
#true if you reach the next level, false otherwise.

def reachNextLevel(experience, threshold, reward):
    if experience+reward >=threshold:
        return True
    else:
        return False
