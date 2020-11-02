# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if Node is None: return None
        visit = []

        def travel(root):
            for vNode in visit:
                if vNode.val == root.val:
                    return vNode
            n = Node(root.val)
            visit.append(n)
            for neighbor in root.neighbors:
                n.neighbors.append(travel(neighbor))
            return n

        return travel(node)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.append([n2, n4])
n2.neighbors.append([n1, n3])
n3.neighbors.append([n2, n3])
n4.neighbors.append([n1, n3])

test = Solution()
test.cloneGraph(n1)
