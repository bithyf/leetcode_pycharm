from treenode import TreeNode


def buildTree(preorder, inorder) -> TreeNode:

    def Tree(pre, ino):
        if len(pre) == 0:
            return None
        else:
            node = TreeNode(pre[0])
            index = ino.index(pre[0])

            if index > 0:
                node.left = Tree(pre[1: index + 1], ino[0:index])
            if index < len(pre) - 1:
                node.right = Tree(pre[index + 1:], ino[index + 1:])
            return node

    return Tree(preorder, inorder)


p = [3,2,1]
o = [2,3,1]
node = buildTree(p, o)
node.travel()