class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        adj = {}
        for edge in edges:
            if edge[0] not in adj:
                adj[edge[0]] = []
            if edge[1] not in adj:
                adj[edge[1]] = []

            adj[edge[0]].append(edge[1])

            adj[edge[1]].append(edge[0])
        leaves = [d for d in adj if len(adj[d]) == 1]

        # layer = 0

        while len(adj) > 2:
            t = []
            # layer += 1
            while len(leaves) > 0:
                leaf = leaves.pop()
                # 删去叶子结点，以及相应的边
                for node in adj[leaf]:
                    # 删除邻接表中的叶子节点
                    adj[node].remove(leaf)
                    if len(adj[node]) == 1:
                        t.append(node)
                del adj[leaf]
            leaves = t
        return adj.keys()
