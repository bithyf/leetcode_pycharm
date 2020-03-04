"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
"""
from listnode import ListNode


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
        ph = ListNode(0)
        ph.next = head
        p1 = ph
        i = 1
        while i < m:
            p1 = p1.next
            i += 1
        p2 = p1.next
        i += 1
        while i <= n:
            p = p2.next
            p2.next = p.next
            p.next = p1.next
            p1.next = p
            i += 1
        return ph.next

        # while i <= n:
        #     p2 = p2.next
        #     i += 1
        # p = p1.next
        # p1.next

