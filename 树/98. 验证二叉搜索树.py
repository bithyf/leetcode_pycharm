def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    import sys

    stack = []
    minnum = -sys.maxsize - 1
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            if node.val <= minnum:
                return False
            minnum = node.val
            root = node.right
    return True