# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        head = root
        while head.left:
            head = head.left
        rear = root
        while rear.right:
            rear = rear.right

        def travel(node):
            f = b = node
            if node.left is not None:
                f, m = travel(node.left)
                m.right = node
                node.left = m
            if node.right is not None:
                m, b = travel(node.right)
                m.left = node
                node.right = m
            return f, b

        travel(root)
        head.left = rear
        rear.right = head
        return head
 