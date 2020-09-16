def maxProbability(n: int, edges, succProb, start: int, end: int) -> float:
    path = {}
    edges = tuple(edges)
    for i in range(len(edges)):
        path[tuple(edges[i])] = succProb[i]

    cost = [0] * n
    leftnode = [i for i in range(0, n)]
    del leftnode[start]
    prenode = start
    precost = 1
    i = 0
    while i < n:
        maxindex = leftnode[0]
        for node in leftnode:
            if (prenode, node) in path:
                cost[node] = max(cost[node], path[(prenode, node)] * precost)
            elif (node, prenode) in path:
                cost[node] = max(cost[node], path[(node, prenode)] * precost)
            maxindex = node if cost[node] > cost[maxindex] else maxindex

        precost = cost[maxindex]
        prenode = maxindex
        cost[prenode] = 0
        del leftnode[leftnode.index(prenode)]
        if prenode == end:
            return precost
        i += 1
    return 0

n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2
print(maxProbability(n,edges,succProb,start, end))