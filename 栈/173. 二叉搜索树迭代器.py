"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。


"""
from treenode import TreeNode
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.__appendleft(root)

    def __appendleft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            self.__appendleft(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.stack) == 0:
            return False
        return True


