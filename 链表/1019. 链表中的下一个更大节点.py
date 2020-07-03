from listnode import ListNode


def nextLargerNodes(self, head: ListNode):
    largernum = []  # 存储 largernum（node）
    leftindex = [0]  # 存储  largernum（node）为零的点的下标
    leftnum = [head.val]   # 存储  largernum（node）为零的点的下标

    p = head.next
    i = 1
    while p:
        largernum.append(0)
        while len(leftnum) > 0 and p.val > leftnum[-1]:
            largernum[leftindex[-1]] = p.val
            leftindex.pop()
            largernum.pop()
        leftindex.append(i)
        largernum.append(p.val)

        p = p.next
        i += 1
    return largernum
