from treenode import TreeNode


def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def buildtree(left, right):
        if left > right:
            return [None]
        trees = []
        for mid in range(left, right + 1):
            lefttrees = buildtree(left, mid - 1)
            righttrees = buildtree(mid + 1, right)

            for leftnode in lefttrees:
                for rightnode in righttrees:
                    curnode = TreeNode(mid)
                    curnode.left = leftnode
                    curnode.right = rightnode
                    trees.append(curnode)

        return trees
    buildtree(1, n)
                    
