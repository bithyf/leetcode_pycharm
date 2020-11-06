class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = {}  #
        inNum = [0] * numCourses  # 入度
        for edge in prerequisites:
            inNum[edge[0]] += 1
            if edge[1] not in adj:
                adj[edge[1]] = [edge[0]]
            else:
                adj[edge[1]].append(edge[0])
        while len(adj) > 0:
            out = []
            if 0 in inNum:
                index = inNum.index(0)
                inNum[index] = -1
                if index in adj:  # 若节点在邻接表里
                    for idx in adj[index]:
                        inNum[idx] -= 1
                    del adj[index]
            else:
                return False
        return True
