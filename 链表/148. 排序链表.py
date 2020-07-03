"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
"""
from listnode import ListNode
from listnode import listtolistnode, printlistnode


def sortList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    length = 1
    ph = ListNode(0)
    ph.next = head
    while True:
        p1 = ph
        p2 = ph
        i = 0
        while i < length:
            p2 = p2.next
            i += 1
            if p2.next is None:
                return ph.next
        # 一趟排序
        while True:
            i = 0
            # 两组排序
            while i < length and p2.next is not None:
                if p1.next.val >= p2.next.val:
                    p = p2.next
                    p2.next = p.next
                    p.next = p1.next
                    p1.next = p
                    i += 1
                p1 = p1.next
                if p1 == p2:
                    while i < length and p2.next is not None:
                        p2 = p2.next
                        i += 1
                    break
            p1 = p2
            i = 0
            while i < length and p2 is not None:
                p2 = p2.next
                i += 1
            if p2 is None:
                # printlistnode(ph.next)
                break

        length *= 2

    # return ph.next


nums = [5, 4]
head = listtolistnode(nums)

head = sortList(head)
printlistnode(head)



