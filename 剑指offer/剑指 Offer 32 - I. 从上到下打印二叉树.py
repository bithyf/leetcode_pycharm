from treenode import TreeNode


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        nums = []
        while len(stack) > 0:
            tem = []
            for node in stack:
                nums.append(node.val)
                if node.left:
                    tem.append(node.left)
                if node.right:
                    tem.append(node.right)
            stack = tem
        return nums
