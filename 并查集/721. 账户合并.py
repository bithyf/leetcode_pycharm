class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        if len(accounts) == 0:
            return []
        pre = list(range(len(accounts)))

        def find(a):
            if pre[a] != a:
                pre[a] = find(pre[a])
            return pre[a]

        graph = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in graph:
                    graph[accounts[i][j]].append(i)
                else:
                    graph[accounts[i][j]] = [i]

        for peoplelist in graph:
            for people in graph[peoplelist]:
                ra = find(graph[peoplelist][0])
                rb = find(people)
                pre[rb] = ra
        new_account = []
        for people in range(len(pre)):
            if people != pre[people]:
                pre_people = find(people)
                accounts[pre_people] += accounts[people][1:]
        for people in range(len(pre)):
            if people == pre[people]:
                new_account.append(accounts[people])
        for account in new_account:
            account[1:] = list(set(account[1:]))
            account[1:] = sorted(account[1:])
        return new_account


a = Solution()
accounts = [["David", "David0@m.co", "David4@m.co", "David3@m.co"],
            ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
            ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
            ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
            ["David", "David4@m.co", "David1@m.co", "David3@m.co"]]

b = a.accountsMerge(accounts)
print(b)
