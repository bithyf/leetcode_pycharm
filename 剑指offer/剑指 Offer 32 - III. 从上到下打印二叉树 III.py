# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#             """
#         if root is None:
#             return []
#
#         stack = [root]
#         nums = []
#         t = 1
#         while len(stack) > 0:
#             tem = []
#             tem_num = []
#             for node in stack:
#                 tem_num.append(node.val)
#                 if node.left:
#                     tem.append(node.left)
#                 if node.right:
#                     tem.append(node.right)
#             if t == 1
#                 nums.append(tem_num)
#                 t *= -1
#             else:
#                 nums.append(tem_num[-1::])
#                 t *= -1
#             stack = tem
#         return nums

a = [1, 2, 3]
print(a[::-1])
