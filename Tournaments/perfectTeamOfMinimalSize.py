def perfectTeamOfMinimalSize(n, candidates):

    MAX_MASK = 1 << n

    knowledge = [0] * len(candidates)
    for i in range(len(candidates)):
        for j in range(len(candidates[i])):
            knowledge[i] = knowledge[i] | (1 << candidates[i][j])
    teamSize = [-1] * MAX_MASK
    teamSize[0] = 1
    for i in range(len(teamSize)):
        if teamSize[i] == -1:
            continue
        for j in range(len(knowledge)):
            i2 = i | knowledge[j]
            if teamSize[i2] == -1 or teamSize[i2] > teamSize[i] + 1:
                teamSize[i2] = teamSize[i] + 1

    return teamSize[MAX_MASK - 1]
