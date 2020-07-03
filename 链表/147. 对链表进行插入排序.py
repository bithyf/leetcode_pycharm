from listnode import ListNode


def insertionSortList(head: ListNode) -> ListNode:
    if head is None:
        return head
    p2 = head
    p1 = ListNode(0)
    p1.next = p2
    while p2.next:
        if p2.val <= p2.next.val:
            p2 = p2.next
            continue
        p = p1
        while p.next.val <= p2.next.val:
            p = p.next
        tp = p2.next
        p2.next = tp.next
        tp.next = p.next
        p.next = tp
    return p1.next

