"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
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


def printlistnode(head):
    p = head
    while p is not None:
        print(p.val)
        p = p.next


def rotateRight(head: ListNode, k: int) -> ListNode:
    if head is None:
        return head
    p1 = p2 = head
    i = 0
    while i < k:
        if p1.next is None:
            p1 = head
            k = k % (i + 1)
            i = 0
        else:
            p1 = p1.next
            i += 1
    if p1 == head:
        return head
    while p1.next is not None:
        p2 = p2.next
        p1 = p1.next
    p1.next = head
    head = p2.next
    p2.next = None
    return head

num = [1, 2, 3, 4, 5]
target = 101
listhead = listtolistnode(num)
printlistnode(rotateRight(listhead, target))
