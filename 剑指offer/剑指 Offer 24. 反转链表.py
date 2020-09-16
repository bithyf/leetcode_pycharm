def reverseList(head):
    p = head
    while p.next:
        p1 = p.next
        p.next = p1.next
        p1.next = head
        head = p1
    return head