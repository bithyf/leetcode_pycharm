"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改109. 有序链表转换二叉搜索树给定的链表。
"""
from listnode import ListNode


def detectCycle(self, head: ListNode) -> ListNode:
    slow = fast = head
    if head is None or head.next is None:
        return None
    while True:
        if fast is None or fast.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    target = head
    while slow is not target:
        slow = slow.next
    return target

