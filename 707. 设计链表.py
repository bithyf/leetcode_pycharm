class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index <= self.size:
            p = self.head
            while index >= 0:
                p = p.next
                index -= 1
            return p.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        p = ListNode(val)
        p.next = self.head.next
        self.head.next = p
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        p = self.head
        while p.next:
            p = p.next
        p.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        p = self.head
        while index > 0:
            p = p.next
            index -= 1
        node = ListNode(val)
        node.next = p.next
        p.next = node.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.size:
            p = self.head
            while index > 0:
                p = p.next
                index -= 1
            p.next = p.next.next

