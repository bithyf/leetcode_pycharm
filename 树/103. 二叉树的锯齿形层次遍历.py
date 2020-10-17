def zigzagLevelOrder(root):
    """
       :type root: TreeNode
       :rtype: List[List[int]]
    """
    if not root:
        return []
    stack = [root]
    nums = []
    t = 1
    while len(stack):
        num = []
        level = []
        for node in stack:
            num.append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        nums.append(num[::t])
        t *= -1
        stack = level
    return nums


a = [1, 2, 3]
b = a[::1]

print(b)
