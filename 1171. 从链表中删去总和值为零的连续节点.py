"""

给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。
"""

from listnode import ListNode


def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    sum = 0