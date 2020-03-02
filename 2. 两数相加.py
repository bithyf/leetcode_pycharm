"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    headnode = ListNode(0)
    p = headnode
    add = 0
    while l1 is not None and l2 is not None:
        node = ListNode((l1.val + l2.val + add) % 10)
        add = (l1.val + l2.val + add) // 10
        p.next = node
        p = p.next
        l1 = l1.next
        l2 = l2.next
    while l1 is not None:
        node = ListNode((l1.val + add) % 10)
        add = (l1.val + add) // 10
        p.next = node
        p = p.next
        l1 = l1.next
    while l2 is not None:
        node = ListNode((l2.val + add) % 10)
        add = (l2.val + add) // 10
        p.next = node
        p = p.next
        l2 = l2.next
    if add != 0:
        node = ListNode(add)
        p.next = node

    return headnode.next





