"""

给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。

如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。
"""
from listnode import ListNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root is None:
            return False
        queue = [root]
        while len(queue) > 0:
            print("-----")
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.val == head.val:
                if self.dps(head.next, node.left) or self.dps(head.next, node.right):
                    return True
        return False

    def dps(self, head, root):
        if head is None:
            return True
        elif root:
            if root.val == head.val:
                return self.dps(head.next, root.left) or self.dps(head.next, root.right)
            return False
        return False