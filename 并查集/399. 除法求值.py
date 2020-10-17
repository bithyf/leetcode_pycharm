def calcEquation(self, equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    graph = {}

    for (x, y), z in zip(equations, values):
        if x in graph:
            graph[x][y] = z
        else:
            graph[x] = {y: z}

        if y in graph:
            graph[y][x] = 1 / z
        else:
            graph[y] = {x: 1 / z}

    def path(s, t):
        if s not in graph:
            return -1
        if s == t:
            return 1
        for node in graph[s].keys():
            if node == t:
                return graph[s][node]
            if node not in visited:
                visited.add(node)
                num = path(node, t)
                if num != -1:
                    return num * graph[s][node]
        return -1

    res = []
    for qs, qt in queries:
        visited = set()
        res.append(path(qs, qt))

    return res
