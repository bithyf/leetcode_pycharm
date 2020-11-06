class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = {}  #
        inNum = [0] * numCourses  # 入度
        for edge in prerequisites:
            inNum[edge[0]] += 1
            if edge[1] not in adj:
                adj[edge[1]] = [edge[0]]
            else:
                adj[edge[1]].append(edge[0])

        zeroNode = [i for i in range(numCourses) if inNum[i] == 0]
        order = []
        while len(zeroNode) > 0:
            if zeroNode[0] in adj:
                for idx in adj[zeroNode[0]]:
                    inNum[idx] -= 1
                    if inNum[idx] == 0:
                        zeroNode.append(idx)
            order.append(zeroNode[0])
            del zeroNode[0]
        if len(order) < numCourses:
            return []
        return order
       