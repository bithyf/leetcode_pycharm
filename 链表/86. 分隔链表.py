"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。
"""
from listnode import ListNode
from listnode import listtolistnode, printlistnode


def partition(self, head: ListNode, x: int) -> ListNode:
    ph = ListNode(0)
    ph.next = head
    p1 = p2 = ph
    while p2.next:
        if p2.next.val < x:
            if p1 == p2:
                p2 = p1 = p1.next
            else:
                p = p2.next.next
                p2.next.next = p1.next
                p1.next = p2.next
                p2.next = p
                p1 = p1.next
        else:
            p2 = p2.next
    return ph.next

