"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
"""
from listnode import ListNode
from listnode import listtolistnode, printlistnode


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head
    phead = ListNode(0)
    phead.next = head

    p1 = phead
    p2 = head
    while p2.next:
        if p2.val == p2.next.val:
            p2 = p2.next
            while p2.next and p2.val == p2.next.val:
                p2 = p2.next
            p1.next = p2.next
            p2 = p2.next
            if not p2:
                return phead.next
        else:
            p1 = p1.next
            p2 = p2.next
    return phead.next

