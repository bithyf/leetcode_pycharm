from treenode import TreeNode


def inorderTraversal(self, root: TreeNode):
    num = []
    stack = []
    node = root
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            num.append(node.val)
            node = node.right
    return num



