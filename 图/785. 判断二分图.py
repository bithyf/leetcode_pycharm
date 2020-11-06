class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        tp = [0] * len(graph)
        tp[0] = 1

        def travel(node):
            # print(node)
            real = True
            for n in graph[node]:
                if tp[n] == 0:
                    tp[n] = -tp[node]
                    real = real and travel(n)
                elif tp[n] == tp[node]:
                    return False
            return real

        # r = True
        for i in range(len(tp)):
            if tp[i] == 0:
                tp[i] = 1
                if not travel(i):
                    return False
        return True
