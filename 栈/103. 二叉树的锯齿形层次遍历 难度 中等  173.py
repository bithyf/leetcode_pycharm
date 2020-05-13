from treenode import TreeNode


def zigzagLevelOrder(root: TreeNode):
    if root is None:
        return []
    queue = [root]
    nums = []
    rev = 0
    while len(queue) != 0:
        num = []
        while len(queue) != 0:
            num.append(queue.pop(0))
        for node in num:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if rev == 0:
            nums.append([node.val for node in num])
            rev = 1
        else:
            nums.append(reversed([node.val for node in num]))
            rev = 0

        print(nums)
    return nums