def getKthFromEnd(head, k):
    p1 = p2 = head
    while k > 0 and p1:
        p1 = p1.next
        k -= 1
    if k > 0:
        return None
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2