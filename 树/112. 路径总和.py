from treenode import TreeNode


def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    if root.left is None and root.right is None:
        return sum == root.val
    return self.hasPathSum(root.left, sum - root.val) or\
           self.hasPathSum(root.right, sum - root.val)