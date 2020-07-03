# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(inorder, postorder) -> TreeNode:
    def recurision(postend, inbegin, inend):
        if inbegin > inend:
            return None
        node = TreeNode(postorder[postend])
        for i in range(inbegin, inend + 1):
            if inorder[i] == postorder[postend]:
                break
        node.left = recurision(postend - (inend - i + 1), inbegin, i - 1)
        node.right = recurision(postend - 1, i + 1, inend)
        return node

    return recurision(len(postorder) - 1, 0, len(inorder) - 1)


postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]
buildTree(postorder, inorder)
