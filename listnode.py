# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


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
        print(p.val, end=" ")
        p = p.next
    print('')
