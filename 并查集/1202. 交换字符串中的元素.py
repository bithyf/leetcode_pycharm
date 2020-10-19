class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        pre = list(range(len(s)))
        s = list(s)

        def find(a):
            if a != pre[a]:
                pre[a] = find(pre[a])
            return pre[a]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            pre[rb] = ra

        for pair in pairs:
            union(pair[0], pair[1])
        index_lists = {}
        for index, f in enumerate(pre):
            root = find(f)
            if root in index_lists:
                index_lists[root].append(index)
            else:
                index_lists[root] = [index]
        for index_list in index_lists.values():
            nums = []
            for index in index_list:
                nums.append(s[index])
            nums.sort()
            for i, index in enumerate(index_list):
                s[index] = nums[i]
        return ''.join(s)
