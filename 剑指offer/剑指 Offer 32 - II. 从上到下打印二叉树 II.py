class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
            """
        if root is None:
            return []

        stack = [root]
        nums = []

        while len(stack) > 0:
            tem = []
            tem_num = []
            for node in stack:
                tem_num.append(node.val)
                if node.left:
                    tem.append(node.left)
                if node.right:
                    tem.append(node.right)
            nums.append(tem_num)
            stack = tem
        return nums
