def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    stack = [root]
    nums = []

    while len(stack):
        num = []
        level = []
        for node in stack:
            num.append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        nums.append(num)
        stack = level
    return nums
