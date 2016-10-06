'''Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same(maximum) number of votes, assume there is no winner at all.

Example

For votes = [2, 3, 5, 2] and k = 3, the output should be
electionsWinners(votes, k) = 2.

Input/Output

[time limit] 4000ms (py)
[input] array.integer votes

A non-empty array of non-negative integers. Its ith element denotes the number of votes cast for the ith candidate.

Constraints:
4 ≤ votes.length ≤ 105,
0 ≤ votes[i] ≤ 104.

[input] integer k

The number of voters who haven't cast their vote yet.

Constraints:
0 ≤ k ≤ 105.

[output] integer'''

def electionsWinners(votes, k):
    winner  = 0
    for i in range(0,len(votes)):
        newVotes = list(votes)
        newVotes[i] += k
        if newVotes[i] == max(newVotes) and newVotes.count(newVotes[i])==1:
            winner += 1
    
    return winner
