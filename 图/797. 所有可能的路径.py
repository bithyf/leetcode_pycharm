class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths = []

        def travel(node, path):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path)
            for rear in graph[node]:
                travel(rear, path[:])

        travel(0, [])
