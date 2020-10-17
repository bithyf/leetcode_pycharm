def findRedundantConnection(self, edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    ds = {}

    def find(a):
        if a not in ds:
            ds[a] = a
        elif ds[a] != a:
            ds[a] = find(ds[a])
        return ds[a]

    for edge in edges:
        ra = find(edge[0])
        rb = find(edge[1])
        if ra == rb:
            return edge
        ds[ra] = rb
