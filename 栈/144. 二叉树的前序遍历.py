from treenode import TreeNode
def preorderTraversal(root: TreeNode):
    p = root
    num = []
    node = []
    while len(node) != 0 or p:
        if p:
            node.append(p)
            num.append(p.val)
            # print(p.val)
            if p.left:
                p = p.left
            elif len(num) != 0:
                p = node.pop().right
        else:
            p = node.pop().right
    return num