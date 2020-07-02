from treenode import TreeNode


def getAllElements(root1: TreeNode, root2: TreeNode):
    List = []
    stack1 = []
    stack2 = []
    node1 = root1
    node2 = root2
    while node1 or len(stack1) > 0 or node2 or len(stack2) > 0:
        while node1:
            stack1.append(node1)
            node1 = node1.left
        while node2:
            stack2.append(node2)
            node2 = node2.left

        if len(stack1) != 0 and (len(stack2) == 0 or stack1[-1].val < stack2[-1].val):
            node1 = stack1.pop()
            List.append(node1.val)
            node1 = node1.right
        else:
            node2 = stack2.pop()
            List.append(node2.val)
            node2 = node2.right

    return List

    # list1 = []
    # list2 = []
    # num = []
    #
    # def tree2list(Tree):
    #     List = []
    #     stack = []
    #     node = Tree
    #     while node or len(stack) > 0:
    #         if node:
    #             stack.append(node)
    #             node = node.left
    #         else:
    #             node = stack.pop()
    #             List.append(node.val)
    #             node = node.right
    #     return List
    #
    # list1 = tree2list(root1)
    # list2 = tree2list(root2)
    #
    # print(list1, list2)
    # i = j = 0
    # while i < len(list1) and j < len(list2):
    #     if list1[i] > list2[j]:
    #         num.append(list2[j])
    #         j += 1
    #     else:
    #         num.append(list1[i])
    #         i += 1
    #
    # if i < len(list1):
    #     num.extend(list1[i:])
    # elif j < len(list2):
    #     num.extend(list2[j:])
    #
    # return num
    #
    #