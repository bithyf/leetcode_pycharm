class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        reGraph = [[]] * len(graph)
        zeroNode = []
        safe = []
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                zeroNode.append(i)
            else:
                for node in graph[i]:
                    reGraph[node].append(i)

        i = 0
        while i < len(zeroNode):
            s = zeroNode[i]
            for node in reGraph[s]:
                graph[node].remove(s)
                if len(graph[node]) == 0:
                    zeroNode.append(node)
            i += 1

        return zeroNode


a = [[]] * 3
a[2].append(1)
print(a)
