def bfsDistancesUnweightedGraph2(matrix, vertex1, vertex2):

    visited = []
    queue = []
    distance = []

    for i in range(len(matrix)):
        visited.append(False)
        distance.append(0)

    visited[vertex1] = True
    queue.append(vertex1)
    while len(queue) > 0:
        currentVertex = queue[0]
        queue = queue[1:]
        visited[currentVertex] = True
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] =  False
                distance[nextVertex] = distance[currentVertex] + 1
                queue.append(nextVertex)

    return distance[vertex2]
