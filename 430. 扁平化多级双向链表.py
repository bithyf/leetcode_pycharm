from listnode import Node


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        self.change(head)
        return p

    def change(self, node):
        if node.child is not None:
            p = node.next
            node.next = node.child
            node.next.prev = node
            rear = self.change(node.next)
            rear.next = p
            p.prev = rear
            node = rear

        if node.next is not None:
            return self.change(node.next)

        else:
            return node


