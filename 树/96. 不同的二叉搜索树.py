def numTrees(self, n):
    numtree = [1]  # index个节点的二叉搜索树个数
    for node in range(1, n + 1):
        num = 0
        for left in range(node):
            num += numtree[left] * numtree[node - left - 1]
        numtree.append(num)

    return num


