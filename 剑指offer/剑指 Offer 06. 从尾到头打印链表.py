from listnode import ListNode


def reversePrint(head: ListNode):
    array = []
    while head:
        array.insert(0, head.val)
        head = head.next
    return array