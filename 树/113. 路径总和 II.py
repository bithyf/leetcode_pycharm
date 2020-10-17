from treenode import TreeNode


def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    def pathfind(root, path, paths, sum):
        if not root:
            return
        if not root.left and not root.right:
            # print(path + [root.val])
            if root.val == sum:
                paths.append(path + [root.val])
            return
        pathfind(root.left, path + [root.val], paths, sum - root.val)
        pathfind(root.right, path + [root.val], paths, sum - root.val)

    paths = []
    pathfind(root, [], paths, sum)
    return paths

# print([1] + [2])
