class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodeidx = {}
        new_node = []
        p = head
        i = 0
        while p:
            new_node.append(Node(p.val))
            nodeidx[p] = [i]
            i += 1
            p = p.next
        new_node.append(None)
        p = head
        while p:
            if p.random is None:
                nodeidx[p].append(None)
            else:
                nodeidx[p].append(nodeidx[p.random][0])
            p = p.next
        p = head
        i = 0
        while p:
            new_node[i].next = new_node[i + 1]
            new_node[i].random = new_node[nodeidx[p][1]]
            p = p.next
        return new_node[0]
