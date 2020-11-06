class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        fo = defaultdict(list)
        for ticket in tickets:
            fo[ticket[0]].append(ticket[1])
        for link in fo:
            fo[link].sort(reverse=True)
        stack = []

        def travel(loc):
            while len(fo[loc]) > 0:
                des = fo[loc].pop()
                travel(des)
            stack.append(loc)

        travel('JFK')
        return stack[::-1]
