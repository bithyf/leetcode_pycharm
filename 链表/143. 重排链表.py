"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
from listnode import ListNode


def reorderList(self, head: ListNode) -> None:
    if head is None or head.next is None:
        return head
    # p = head
    # length = 0
    # while p:
    #     length += 1
    #     p = p.next
    # i = 1
    # p = head
    # while i < (length + 1) // 2:
    #     p = p.next
    #     i += 1

    p = head
    p2 = head.next
    while True:
        if p2 is None or p2.next is None:
            break
        p = p.next
        p2 = p2.next.next

    p1 = p
    while p1.next:
        if p1 == p:
            p1 = p1.next
            continue
        p2 = p1.next
        p1.next = p2.next
        p2.next = p.next
        p.next = p2

    p1 = head
    p2 = p.next
    p.next = None
    while p2:
        p = p2.next
        p2.next = p1.next
        p1.next = p2
        p2 = p
        p1 = p1.next.next

