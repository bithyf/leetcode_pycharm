def isValidSerialization(preorder):
    slots = 0
    # 上一个是',' 为1
    pre = 1
    for node in preorder:
        if pre == 1:
            pre = 0
            if node is not '#':
                slots += 2
            # print(slots)
        else:
            if node is ',':
                slots -= 1
                pre = 1
            if slots < 0:
                return False

    if slots == 0:
        return True
    return False

