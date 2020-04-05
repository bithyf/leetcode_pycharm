class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(self, head: 'Node') -> 'Node':
    if head is None:
        return head
    oldnode = head
    visitednode = dict()

    def getclone(node):
        if node:
            if node not in visitednode:
                newnode = Node(node.val)
                visitednode[node] = newnode
            return visitednode[node]
        return None

    newnode = Node(oldnode.val)
    visitednode[oldnode] = newnode
    while oldnode:
        newnode.next = getclone(oldnode.next)
        newnode.random = getclone(oldnode.random)
        oldnode = oldnode.next
        newnode = newnode.next
    return visitednode[head]
