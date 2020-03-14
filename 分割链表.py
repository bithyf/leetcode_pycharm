"""
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表。
"""
from listnode import ListNode


def splitListToParts(root: ListNode, k: int):
    length = 0
    p = root
    while p:
        length += 1
        p = p.next

    consult = length // k
    reminder = length % k

    nums = []
    p = root
    while reminder != 0:
        l1 = p
        for i in range(consult):
            p = p.next
        l2 = p.next
        p.next = None
        p = l2
        nums.append(l1)
        reminder -= 1
        k -= 1
    while k > 0:
        if p is None:
            l1 = None
            nums.append(l1)
        else:
            l1 = p
            for i in range(consult - 1):
                p = p.next
            l2 = p.next
            p.next = None
            p = l2
            nums.append(l1)
            reminder -= 1
            k -= 1
    return nums

