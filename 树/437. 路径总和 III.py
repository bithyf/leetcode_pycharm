def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """

    def count(node, sum):
        if node is None:
            return 0
        if node.val == sum:
            return 1 + count(node.left, 0) + count(node.right, 0)
        return count(node.left, sum - node.val) + count(node.right, sum - node.val)
    
    def travl(node, sum):
        if node is None:
            return 0
        path = count(node, sum)
        return path + travl(node.left, sum) + travl(node.right, sum)

    return travl(root, sum)
