# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        paths = []

        def pathTravel(node, path):
            if not node:
                return

            path.append(node.val)
            # print(path)

            if sum(path) == _sum:
                # print(path)
                if node.left is None and node.right is None:
                    # print(path)
                    paths.append(path[:])
                    del path[-1]
                    return
            pathTravel(node.left, path)
            pathTravel(node.right, path)
            del path[-1]

        pathTravel(root, [])
        return paths
