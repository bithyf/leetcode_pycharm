# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder) -> TreeNode:
    def recurision(prebegin, inbegin, inend):
        if inbegin > inend:
            return None
        node = TreeNode(preorder[prebegin])
        for i in range(inbegin, inend + 1):
            if inorder[i] == preorder[prebegin]:
                break
        node.left = recurision(prebegin + 1, inbegin, i - 1)
        node.right = recurision(prebegin + i - inbegin + 1, i + 1, inend)
        return node

    return recurision(0, 0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
buildTree(preorder, inorder)
