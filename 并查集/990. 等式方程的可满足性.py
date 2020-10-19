class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """

        unequal = []
        pre = {}

        def find(a):
            if a != pre[a]:
                pre[a] = find(pre[a])
            return pre[a]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            pre[rb] = ra

        for equation in equations:
            if equation[0] not in pre:
                pre[equation[0]] = equation[0]
            if equation[3] not in pre:
                pre[equation[3]] = equation[3]
            if equation[1:3] == "==":
                union(equation[0], equation[3])
            else:
                unequal.append(equation)

        for equal in unequal:
            if find(equal[0]) == find(equal[3]):
                return False
        return True
