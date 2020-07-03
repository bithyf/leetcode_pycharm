"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(self, head: ListNode) -> ListNode:
    if head.next is None or head.next.next is None:
        return head
    p1 = head
    p2 = head.next
    ph = ListNode(0)
    p = ph
    while True:
        p1.next = p2.next
        p2.next = p1
        p.next = p2
        p = p1
        if p1.next is None or p1.next.next is None:
            break
        p1 = p1.next
        p2 = p1.next
    return ph.next
