# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def travel(self):
        print(self.val)
        if self.left:
            self.left.travel()
        if self.right:
            self.right.travel()

