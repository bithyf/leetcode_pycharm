def mergeTwoLists(l1, l2):
    p1 = l1
    p2 = l2
    l = ListNode()
    p3 = l
    while p1 and p2:
        if p1.val >= p2.val:
            p3.next = p2
            p2 = p2.next
        else:
            p3.next = p1
            p1 = p1.next
        p3 = p3.next
    if p1:
        p3.next = p1
    if p2:
        p3.next = p2
    return l.next


