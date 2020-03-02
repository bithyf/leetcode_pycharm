"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def listtolistnode(nums):
    head = ListNode(nums[0])
    p = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        p.next = node
        p = p.next

    return head


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    p1 = head
    i = 0
    while i < n and p1 is not None:
        i += 1
        p1 = p1.next
    if p1 is None:
        return head.next
    p2 = head
    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    return head


node = [1, 2, 3, 4, 5]
listnode = listtolistnode(node)
