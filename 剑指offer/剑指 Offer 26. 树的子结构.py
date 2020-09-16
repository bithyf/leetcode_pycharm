from treenode import TreeNode


def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    def SubStructure(nodea, nodeb):
        if nodeb is None:
            return True
        if nodea is None:
            return False
        if nodea.val == nodeb.val:
            return SubStructure(nodea.left, nodeb.left) \
                   and SubStructure(nodea.right, nodeb.right)
        else:
            return False

    stack = []
    pa = A
    while len(stack) > 0 or pa:
        if SubStructure(pa, B):
            return True
        if pa.left:
            stack.append(pa.left)
        if pa.right:
            stack.append(pa.right)
        if len(stack) > 0:
            pa = stack.pop(0)
        else:
            pa = None
    return False