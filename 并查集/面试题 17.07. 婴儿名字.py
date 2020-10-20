class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        pre = {}

        def sepreate(name):
            for i in range(len(name)):
                if name[i] == '(':
                    break
            return i

        def sepreate_name(name):
            for i in range(len(name)):
                if name[i] == ',':
                    break
            name1 = name[1: i]
            name2 = name[i + 1: -1]
            return name1, name2

        def find(a):
            if a not in pre:
                pre[a] = a

            if a != pre[a]:
                pre[a] = find(pre[a])
            return pre[a]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra < rb:
                pre[rb] = ra
            else:
                pre[ra] = rb

        for synonym in synonyms:
            name1, name2 = sepreate_name(synonym)
            union(name1, name2)

        frequence = {}
        for name in names:
            mid = sepreate(name)
            frequence[name[:mid]] = int(name[mid + 1: -1])
        for name in frequence:
            rname = find(name)
            if rname != name:
                if rname not in frequence:
                    frequence[rname] = 0
                frequence[rname] += frequence[name]
        new_names = []
        for idx in pre:
            if idx == pre[idx]:
                new_names.append(idx + '(' + str(frequence[idx]) + ')')

        return new_names


test = Solution()
names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]

new = test.trulyMostPopular(names, synonyms)
print(new)
