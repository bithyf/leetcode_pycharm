class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        pre = list(range(n))

        def find(a):
            if a != pre[a]:
                pre[a] = find(pre[a])
            return pre[a]

        num_Connected = 0
        extra = 0
        for connection in connections:
            ra = find(connection[0])
            rb = find(connection[1])
            if ra == rb:
                extra += 1
            else:
                pre[rb] = ra
        for idx, p in enumerate(pre):
            if idx == find(idx):
                num_Connected += 1
        if num_Connected - 1 > extra:
            return -1
        return num_Connected - 1
