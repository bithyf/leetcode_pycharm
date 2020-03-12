"""
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
"""


from listnode import ListNode


def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    p1 = head
    p2 = p1.next
    while p2.next:
        p = p2.next
        p2.next = p.next
        p.next = p1.next
        p1.next = p
        p1 = p1.next
        p2 = p2.next
    return head