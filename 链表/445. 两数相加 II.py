"""
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
"""
from listnode import ListNode
from listnode import listtolistnode


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    p = l1
    length1 = length2 = 0
    while p:
        length1 += 1
        p = p.next
    p = l2
    while p:
        length2 += 1
        p = p.next

    if length1 >= length2:
        p1 = l1
        p2 = l2
    else:
        p1 = l2
        p2 = l1
        length1, length2 = length2, length1
    sumnode = ListNode(0)
    reminder = Sum(p1, p2, length1, length2, sumnode)
    if reminder is not 0:
        node = ListNode(reminder)
        node.next = sumnode
        sumnode = node
    return sumnode


def Sum(p1, p2, length1, length2, sumnode):

    if length1 - length2 != 0:
        node = ListNode(0)
        sumnode.next = node
        sump = p1.val + Sum(p1.next, p2, length1 - 1, length2, node)
        sumnode.val = sump % 10
        return sump // 10
    else:
        if p1:
            sump = p1.val + p2.val
            if p1.next:
                node = ListNode(0)
                sumnode.next = node
                sump += Sum(p1.next, p2.next, length1 - 1, length2 - 1, node)
            sumnode.val = sump % 10
            return sump // 10
        return 0


num1 = [7, 2, 4, 3]
num2 = [5, 6, 4]
l1 = listtolistnode(num1)
l2 = listtolistnode(num2)

node = addTwoNumbers(l1, l2)



