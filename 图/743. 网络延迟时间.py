class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # 最短到达时间
        arrive = {K: 0}
        from collections import defaultdict
        adj = defaultdict(list)
        for time in times:
            adj[time[0]].append(time[1:])

        def travel(node):
            if node not in adj:
                return
            for n in adj[node]:
                if n[0] not in arrive:
                    arrive[n[0]] = n[1] + arrive[node]
                    travel(n[0])
                else:
                    if arrive[n[0]] > n[1] + arrive[node]:
                        arrive[n[0]] = n[1] + arrive[node]
                        travel(n[0])

        if len(arrive) == N:
            return max(arrive.values())
        return -1
