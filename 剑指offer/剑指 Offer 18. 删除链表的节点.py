from listnode import ListNode


def deleteNode(self, head: ListNode, val: int) -> ListNode:
    p1 = p = ListNode(1)
    p.next = head
    while p.next:
        if p.next.val == val:
            p.next = p.next.next

        else:
            p = p.next
    return p1.next
