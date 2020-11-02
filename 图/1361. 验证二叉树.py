class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

        node = []
        for num in leftChild + rightChild:
            if num != -1:
                node.append(num)
        node = list(set(node))
        if len(node) != n - 1:
            return False

        root = sum(list(range(0, n))) - sum(node)
        visited = []

        # print(root)

        def visit(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited.append(node)
            return visit(leftChild[node]) and visit(rightChild[node])

        return visit(root) and len(visited) == n


n = 4
leftChild = [1, -1, 3, -1]
rightChild = [2, -1, -1, -1]
test = Solution()
if test.validateBinaryTreeNodes(n, leftChild, rightChild):
    print(1)
else:
    print(0)
