from treenode import TreeNode


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def change(node):
            if node is None:
                return

            node.left, node.right = node.right, node.left
            change(node.left)
            change(node.right)

        change(root)
        return root

# num = [1, 2, 3]
# print(num[::-1])
