from treenode import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def travel(l, r):

            if l == r is None:
                return True
            if l and r:
                return l.val == r.val \
                       and travel(l.left, r.right) \
                       and travel(l.right, r.left)
            return False

        travel(root.left, root.right)
